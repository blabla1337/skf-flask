##Description:

	We remember visual information quicker and better comparing to text so a more complex password can be easely remembered.
	For the moment password crackers don't consider Emoji's and kanji characters in their tools, but even if they would (and will in the near future),
        using even a single Emoji in addition to a characters or/and numbers makes the range of possible passwords wider, which means it becomes harder to hack.

##Mitigation:
	
	Verify that Unicode characters are permitted in passwords. 
	A single Unicode code point is considered a character, so 8 emoji or 64 kanji characters should be valid and permitted.
