# Directory listing
-------

## Example:


    """
    To disable or prevent directory access, add following line in your .htaccess file. If
    user points the browsers to a directory that does not have an index file, then a
    "403 Forbidden" error will be displayed:
    Add this line of code to your .htaccess file:
    """

    Options -Indexes

	//Python code to display the files from the uploads folder

	@app.route('/uploads/<filename>')
	def uploaded_file(filename):
    	try:
        	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    	except Exception as e:
        	return redirect(url_for('upload')) 

