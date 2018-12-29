# Encoder (SQL - ESAPI)
-------

## Example:

	
	// Execute prepared statement with parameterized user inputs
	var query = 'SELECT * FROM accounts WHERE username=? AND password=?';
	connection.query(query, [username, passwordHash],
	function (err, rows, fields) {	
	console.log("Results = " + JSON.stringify(rows));
	});
	connection.end();
	