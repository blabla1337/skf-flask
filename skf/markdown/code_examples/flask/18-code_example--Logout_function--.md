# Logout function
-------

## Example:


    from flask_login import login_user, LoginManager, UserMixin, logout_user, login_required

    """
    This way, the logout functionality will revoke the complete session:
    """
  
    @app.route("/logout")
    @login_required
    def logout():
      logout_user()
      setLog(self.userId,"Logout User", "SUCCESS", datetime.utcnow(), "NULL")
      return render_template('index.html')