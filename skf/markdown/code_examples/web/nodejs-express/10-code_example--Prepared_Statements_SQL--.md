# Encoder (SQL - Parameterized Inputs)

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
Execute prepared statement with parameterized user inputs using [`mysql` module](https://www.npmjs.com/package/mysql):
```js
const sqlQuery = 'SELECT * FROM accounts WHERE username=? AND password=?';

connection.query(sqlQuery, [username, passwordHash], (err, rows, fields) => {
	// handle both success and failure for query result 
});

connection.end();
```

## Considerations
TBA
	
