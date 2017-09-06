# Enforce sequential step order (Shopping)
-------

## Example:


    """
    Whenever an functionality consists out of following several steps to achieve some goal i.e,
    "User adds items to chart", "User enters shipping information", "User pays for goods",
    "Items will be shipped." You want to make sure the user can not skip the payment step in
    order to receive his goods.


    ----------	----------  -----------  ----------------
    | Items  |	|  Cart	 |	|checkout |	 | CostumerInfo	|
    ----------	----------  -----------	 ----------------
    |itemID  |	|cartID  |	|PaymentID|  |ConsumerID    |
    |price	 |	|itemID  |	|itemID   |	 |name          |
    |name  	 |	|sesionID|	|Token    |	 |address	    |
    ----------	----------  |sessionID|  |sessionID   	|
                            |Verified |  |consumerToken |
                            -----------	 ----------------		

    As you can see above we have a very simplified database structure for your average
    webshop. Now we can walk through the different steps needed to enforce the user to take
    all steps before payment.

    We wont cover the entire shopping cart functions since that would become a rather big
    example so let's cover the basics of enforcing the sequential steps.

    Step1: would be, the user adding items to his cart.

    Step2: would be, the user adding his items to checkout. Whenever he is done shopping
            "add to checkout" generates a random token for the added items which
            are inserted into the payment table in the database

    """

    def checkTokens():

        //First we build the checktokens function because we want to check the checkout tokens
        //Multiple times throughout the steps
    
        rows = checkout.query.filter_by(sessionID=session['id']).all()
        for x in rows:

            //Here we check for a different token or new session token
            if x.token == session['token']:

                costumerinfo.query.filter_by(sessionID=session['id']).delete()
                db.session.commit()

                checkout.query.filter_by(sessionID=session['id']).delete()
                db.session.commit()

                return redirect(url_for('checkout'))

    //As soon as the user visits your website you start sessions in order to asign sessionId

    """
    On submit we send al the shopping cart data to another table in the database, but
    this time al the items also contain the same random token. Now an attacker cannot sneak
    in new items since these tokens will be evaluated on the payment page.

    next, the user lands on a page where he has to fill in his customer info:

    NOTE: do not forget the CSRF token in order to prevent attackers from changing his
    shipping info.
    """

    //Then we proceed to check if the post values where not empty
    	
    check = True
    error = ""

    if request.method == 'POST':
        if request.form['customerName'] == "" : 
            check = False
            error += "Customer name is required"

        if request.form['customerAddress'] == "":
            check = False
            error += "Customer address is required"

        if check != True:
            return error
        else:
            return redirect(url_for('summary'))
            //In this step we also insert at the customer data into the database

    """        
    Then we select al the customer info and shopping items on sessionID from the
    database and display it on screen in order for the user to verify if all the
    information displayed is correct.
    """

    //When the user has verified we again check the checkout tokens to see if no new items where added
    checkTokens()    

    """
    After that the user verifies this information then he will be redirected to the payment
    page like ideal, Paypall etc.

    Whenever the payment returns true you set the "verified" column on the checkout
    table to TRUE and you send the customer the invoice and send him his items.
    """

    verified = True

    data = checkout.query.filter_by(sessionID=session['id']).first()
    data.verified = verified
    db.session.commit()

    customer = customer.query.filter_by(sessionID=session['id']).delete()
    db.session.commit()

    checkout = checkout.query.filter_by(sessionID=session['id']).delete()
    db.session.commit()

    cart = cart.query.filter_by(sessionID=session['id']).delete()
    db.session.commit()

    