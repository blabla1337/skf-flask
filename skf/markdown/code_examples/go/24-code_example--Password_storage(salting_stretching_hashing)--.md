# Password Storage (salting/stretching/hashing)
-------

## Example:

	package main

	import (
		"crypto/rand"
		"crypto/subtle"
		"encoding/base64"
		"errors"
		"fmt"
		"log"
		"strings"

		"golang.org/x/crypto/argon2" 
	)

	// Constants used for Argon2id algorithm 
	// For explanation of values chosen, please see package documentation:
	// https://godoc.org/golang.org/x/crypto/argon2#IDKey
	const (
		saltLength uint32 = 16
		time uint32 = 1
		memory uint32 =  64 * 1024
		parallelism uint8 = 4
		keyLength uint32 = 32
	)

	// Password is a convenience struct for dealing with the various parameters
	// We use this to decode into the parameters we store along with the password 
	type Password struct {
		Hash []byte
		Salt []byte
		Time uint32
		Memory uint32
		Parallelism uint8
		KeyLength uint32
	}

	// SaltLength returns the length of the salt that was stored
	func (p *Password) SaltLength() int {
		return len(p.Salt)
	}

	// PasswordFromEncodedHash tries to deconstruct a decoded hash in the form
	// $argon2id$v=version$t=time,m=memory,p=parallelism$salt$hash
	// and create a new Password
	func PasswordFromEncodedHash(encodedHash string) (*Password, error) {
		var p Password

		vals := strings.Split(encodedHash, "$")
		if len(vals) != 6 {
			return nil, errors.New("invalid hash")
		}

		var version int
		if _, err := fmt.Sscanf(vals[2], "v=%d", &version); err != nil {
			return nil, err
		}
		if version != argon2.Version {
			return nil, errors.New("incompatible argon2 version")
		}

		if _, err := fmt.Sscanf(vals[3], "m=%d,t=%d,p=%d", &p.Memory, &p.Time,  &p.Parallelism); err != nil {
			return nil, err
		}

		salt, err := base64.RawStdEncoding.DecodeString(vals[4])
		if err != nil {
			return nil, err
		}

		hash, err := base64.RawStdEncoding.DecodeString(vals[5])
		if err != nil {
			return nil, err
		}
		p.KeyLength = uint32(len(hash))

		p.Salt = salt
		p.Hash = hash

		return &p, nil
	}

	// HashPassword derives a hash from the given password and salt
	func HashPassword(password string) (string, error) {
		// generate random salt
		salt, err := randomBytes(saltLength)
		if err != nil {
			return "", err
		}

		// use default constants defined above for Argon2id
		hash := argon2.IDKey([]byte(password), salt, time, memory, parallelism, keyLength)

		// base64 encode the salt and hashed password
		b64Salt := base64.RawStdEncoding.EncodeToString(salt)
		b64Hash := base64.RawStdEncoding.EncodeToString(hash)
		
		// encode the hash for storage
		encodedHash := fmt.Sprintf("$argon2id$v=%d$m=%d,t=%d,p=%d$%s$%s", argon2.Version, memory, time, parallelism, b64Salt, b64Hash)
		
		return encodedHash, nil
	}

	// VerifyPassword takes a password and an encoded hash and tries to verify they are the same
	func VerifyPassword(password, encodedHash string) error {
		p, err := PasswordFromEncodedHash(encodedHash)
		if err != nil {
			return err
		}

		// Derive the key from passed in password using same parameters
		otherHash := argon2.IDKey([]byte(password), p.Salt, p.Time, p.Memory, p.Parallelism, p.KeyLength)

		// Check that the contents of the hashed passwords are identical. Note
		// that we are using the subtle.ConstantTimeCompare() function for this
		// to help prevent timing attacks.
		if subtle.ConstantTimeCompare(p.Hash, otherHash) != 1 {
			return errors.New("failed to compare hashed passwords")
		}
		
		return nil
	}

	// randomBytes is a utility to use crypto/rand for random byte generation
	func randomBytes(n uint32) ([]byte, error) {
		b := make([]byte, n)
		if _, err := rand.Read(b); err != nil {
			return nil, err
		}
		return b, nil
	}

	func main() {
		password := "some secret password"
		
		// Argon2 should be considered as your first choice for new applications
		// https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Password_Storage_Cheat_Sheet.md
		hash, err := HashPassword(password)
		if err != nil {
			log.Fatalf("error hashing password: %s", err.Error())
		}

		// Verify original password returns true
		if err := VerifyPassword(password, hash); err != nil {
			log.Fatalf("passwords did not match: %s", err.Error())
		}

		fmt.Println(hash)
	}
