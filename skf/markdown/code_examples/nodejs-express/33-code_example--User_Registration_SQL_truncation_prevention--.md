# User registration SQL truncation prevention

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
In order to prevent Column truncation SQL injection we have to make sure that the applications structural logic does not mismatches with the database structural logic.

To achieve this imagine the follow example of a database structure of a users table:

`TABLE users`
| Name | Type | Extra |
| --- | --- | --- |
| userID | Int(11) | AUTO_INCREMENT |
| Username | char(21) |  |
| Password | Varchar(255) |  |
| PrivilegeID | Int(11) |  |

TODO: ensure that the username field the application processes is max 21 characters long as well.

## Considerations
TBA
