##Description:

The attraction of bcrypt is that you can tune its work factor to counter increases in computing technology, so that it's very slow to brute-force compared to an MD5/SHA/CRC, all of which are extremely fast to compute. When bcrypt was introduced, the cost factor was 6 for normal users and 8 for super users. Chances are you’re just using the default bcrypt cost factor. Bcrypt-ruby and most other implementations set this to 10, meaning 2^10 key expansion rounds. With advances in computing technology, it is highly recommended to tune the work factor cost periodically to combat brute force attacks.


##Mitigation:

If a developer uses bcrypt, they should ensure the work factor SHOULD be as large as verification server performance will allow, typically at least 13.
