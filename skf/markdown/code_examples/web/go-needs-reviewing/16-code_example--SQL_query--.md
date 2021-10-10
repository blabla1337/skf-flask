# SQL query
-------

## Example:

        
	/*
		The Go website has a blog about using prepared statements here:
		https://golang.org/doc/database/prepared-statements

		If you pass parameters to Query, Exec, QueryContext, ExecContext, the database/sql package
		will automatically use prepared statements for you underneath the hood. Only use
		PrepareContext when you explicitly want to create statements once and reuse the statement 
		for subsequent calls. This can be a useful optimization, but is not necessary to use prepared statements
		in Go. If you concatenate user input to your query string, you may still be vulnerable to SQLinjection,
		so be sure to only pass user data as parameters.
	*/

	type User struct {
		ID int
		First string
		Last string
		UserName string
	}

	type UserStore struct {
		db *sql.DB
	}

	// Define the SQL statement
	// Note: Parameter placeholders in prepared statements vary depending on the DBMS and driver you’re using. 
	// For example, the pq driver for Postgres requires a placeholder like $1 instead of ?.
	var userByUsernameStatement = "SELECT id, first, last, username FROM users WHERE id = ?"

	func (s *UserStore) UserByUserName(ctx context.Context, username string) (User, error) {
		stmt, err := s.db.PrepareContext(ctx, userByUsernameStatement)
		if err != nil {
			log.Fatal(err)
		}

		var user User

		if err := stmt.QueryRowContext(ctx, username).Scan(&user.ID, &user.First, &user.Last, &user.UserName); err != nil {
			if err == sql.ErrNoRows {
				// Handle the case of no rows returned if you do not expect your consumers to handle this error
			}
			return nil, err
		}
	}
		
	// Follow the same concept for INSERT, UPDATE, DELETE, etc.
	// Note: this statement assumes your database has the id column default value as an autoincrementing integer
	// In practice, do not expose this ID to the user and instead use another identifier on the User struct.
	var createUserStatement = "INSERT INTO users(id, first, last, username) VALUES(DEFAULT,?,?,?)"
	func (s *UserStore) CreateUser(ctx context.Context, user User) error {
		stmt, err := s.db.PrepareContext(ctx, userByUsernameStatement)
		if err != nil {
			log.Fatal(err)
		}

		if _, err := stmt.ExecContext(ctx, user.First, user.Last, user.UserName); err != nil {
			return err
		}

		return nil
	}
