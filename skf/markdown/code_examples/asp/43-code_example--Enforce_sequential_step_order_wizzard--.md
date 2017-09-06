Enforce sequential step order (Wizzard)
-------

## Example:
	

	//Example as used in your controller:
	bool next = true;

	//We check for form submit
	if (Request.Form["submit"] != null)
	{   
		//If values are empty we return false and destroy session in else
		if (Request.Form["value1"] == "") { next = false; }
		if (Request.Form["value2"] == "") { next = false; }

		if (next == true)
		{   
			//If all went good the session can be set for step2
			Session["stepOrder"] = "step2";
		}else{
		   Session["stepOrder"] = "";
		   Session.Abandon();
		   Response.Redirect("/Home/Index", true);
		}
	}

	//If the seccond form was submitted and the session was succesfully set to step 2 we proceed
	if ((Request.Form["submit2"] != null) && (Session["stepOrder"] == "step2"))
	{
		if (Request.Form["value3"] == "") { next = false; }

		if (next == true)
		{
			Session["stepOrder"] = "final";
		}else{
			Session["stepOrder"] = "";
			Session.Abandon();
			Response.Redirect("/Home/Index", true);
		}
	}

	//Again we check for the new valid session for doing the final operation
	if ((Request.Form["final"] != null) && (Session["stepOrder"] == "final")) { /* Do final operation! */ }
	return View();

	/*
	If the user drops his session, he has to start over again, and since we assign different values to the same session
	we force the user to follow the sequential order because else he does not get the ssessions needed to proceed 
	*/

