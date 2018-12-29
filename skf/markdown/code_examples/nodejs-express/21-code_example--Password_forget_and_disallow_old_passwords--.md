# Password forget and disallow old passwords
-------

## Example:


	/*
	Whenever you are developing a password forget function, these are the steps to follow
	in order to create hardened defenses.

	TABLE users
	--------------------------------------------------------------------------------------
	| userID | userName |          password          |   EmailAddress   |    access     |
	-----------------------------------------------------------------   
	|   1    | Admin    | <securely hashed password> | info@admin.com   |     TRUE      |
	-----------------------------------------------------------------       
	|   2    | User     | <securely hashed password> | info@user.com    |     FALSE     |
	-----------------------------------------------------------------    
	|   3    | Guest    | <securely hashed password> | info@guest.com   |     TRUE      |
	--------------------------------------------------------------------------------------


	TABLE passwordForget
	------------------------------------------------------------------------------------------------
	| forgotPasswordID |        Token            |  UserID |   Active   |     ol_password_hashes   |
	------------------------------------------------------------------------------------------------
	|        1         |    c3ab8ff13720e....    |    1    |    YES     |      <......>            |
	------------------------------------------------------------------------------------------------
	|        2         |    7dd39466b3c89....    |    1    |    NO      |      <......>            |
	------------------------------------------------------------------------------------------------
	|        3         |    83d4a3960714c....    |    3    |    NO      |      <......>            |
	------------------------------------------------------------------------------------------------


	As you can see we also store the old passwords into the password forget table, this
	we do in order to prevent the user from using old passwords later on in the process.

	Also use a CRON job to make sure the generated tokens for the password reset are
	expire after a certain amount of time like 20 minutes.
	*/

	app.post('/forgot', function(req, res, next) {
	  async.waterfall([
	    function(done) {
	      crypto.randomBytes(20, function(err, buf) {
	        var token = buf.toString('hex');
	        done(err, token);
	      });
	    },
		function(token, done) {
      		User.findOne({ email: req.body.email }, function(err, user) { // get user by email
		        if (!user) {
    		      req.flash('Success', 'You should receive an email with your password reset link shortly');
          	return res.redirect('/forgot');
        }
        user.resetPasswordToken = token;
        user.resetPasswordExpires = Date.now() + PASSWORD_EXPIRY_TOKEN_DURATION; // 1 hour
        user.save(function(err) {
          done(err, token, user);
        });
      });
    },
    function(token, user, done) {
		send_reset_password_email()
        }
      });
    }
  ], function(err) {S
    if (err) return next(err);
    res.redirect('/forgot');
  });
});


app.get('/reset/:token', function(req, res) {
  User.findOne({ resetPasswordToken: req.params.token, resetPasswordExpires: { $gt: Date.now() } }, function(err, user) {
    if (!user) {
      req.flash('error', 'Password reset token is invalid or has expired.');
      return res.redirect('/forgot');
    }
    res.render('reset', {
      user: req.user
    });
  });
});

app.post('/reset/:token', function(req, res) {
  async.waterfall([
    function(done) {
      User.findOne({ resetPasswordToken: req.params.token, resetPasswordExpires: { $gt: Date.now() } }, function(err, user) {
        if (!user) {
          req.flash('error', 'Password reset token is invalid or has expired.');
          return res.redirect('back');
        }
		if (req.body.password ){
			hash = password_hash(req.body.password)
        user.resetPasswordToken = undefined;
        user.resetPasswordExpires = undefined;

        user.save(function(err) {
          req.logIn(user, function(err) {
            done(err, user);
          });
        });
      });
    },
    function(user, done) {
      send_pass_change_confirmation_email()
    }
  ], function(err) {
    res.redirect('/');
  });
});
