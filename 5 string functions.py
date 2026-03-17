# String method
# string 25 functions 

str = " Python is a high level programming language 1234567890 "
# 1. capitalize() : converts the first character of the string to uppercase and the rest to lowercase
print("Capitalize: ",str.capitalize())

# 2. casefold() : converts the string to lowercase
print("Casefold: ",str.casefold())

# 3. center() : returns a centered string of a specified width
print("Center: ",str.center(50,"*"))

# 4. count() : returns the number of occurrences of a substring in the string
print("Count: ",str.count("a"))

# 5. encode() : returns an encoded version of the string
print("Encode: ",str.encode("utf-8"))

# 6. endswith() : returns True if the string ends with a specified suffix, otherwise returns False
print("Endswith: ",str.endswith("0 "))

# 7. expandtabs() : returns a copy of the string where all tab characters are
# replaced with spaces
print("Expandtabs: ",str.expandtabs(4))

# 8. find() : returns the lowest index of the substring if it is found in
# the string, otherwise returns -1
print("Find: ",str.find("a"))

# 9. format() : formats the string using placeholders
print("Format: {} is a programming language".format("Python"))

# 10. format_map() : formats the string using a mapping
print("Format_map: {name} is a programming language".format_map({"name":"Python"}))

# 11. index() : returns the lowest index of the substring if it is found in
# the string, otherwise raises a ValueError
print("Index: ",str.index("a"))

# 12. isalnum() : returns True if all characters in the string are 
# alphanumeric, otherwise returns False
print("Isalnum: ",str.isalnum())

# 13. isalpha() : returns True if all characters in the string are alphabetic
# otherwise returns False
print("Isalpha: ",str.isalpha())

# 14. isdecimal() : returns True if all characters in the string are decimal
# characters, otherwise returns False
print("Isdecimal: ",str.isdecimal())

# 15. isdigit() : returns True if all characters in the string are digits
# otherwise returns False
print("Isdigit: ",str.isdigit())

# 16. isidentifier() : returns True if the string is a valid identifier, otherwise
# returns False
print("Isidentifier: ",str.isidentifier())

# 17. islower() : returns True if all characters in the string are lowercase,
# otherwise returns False
print("Islower: ",str.islower())

# 18. isnumeric() : returns True if all characters in the string are numeric,
# otherwise returns False
print("Isnumeric: ",str.isnumeric())

# 19. isprintable() : returns True if all characters in the string are printable
# otherwise returns False
print("Isprintable: ",str.isprintable())

# 20. isspace() : returns True if all characters in the string are whitespace,
# otherwise returns False
print("Isspace: ",str.isspace())

# 21. istitle() : returns True if the string is a titlecased string
# otherwise returns False
print("Istitle: ",str.istitle())

# 22. isupper() : returns True if all characters in the string are uppercase,
# otherwise returns False
print("Isupper: ",str.isupper())

# 23. join() : returns a string that is the concatenation of the strings in an
# iterable
print("Join: ",",".join(str))

# 24. ljust() : returns a left-justified string of a specified width
print("Ljust: ",str.ljust(50,"*"))

# 25. lower() : returns a copy of the string with all characters in lowercase
print("Lower: ",str.lower())



#     	##   String Functions  ##

#  1. upper()
#  	Purpose: Converts all characters to uppercase.
#  	Syntax: v_name.upper()

#  2. lower()
#  	Purpose: Converts all characters to lowercase.
#  	Syntax: v_name.lower()

#  3. capitalize()
#  	Purpose: Capitalizes the first character and lowercases the rest.
#  	Syntax: v_name.capitalize()

#  4. title()
#  	Purpose: Capitalizes the first character of each word.
#  	Syntax: v_name.title()

#  5. strip() / rstrip() / lstrip()
#  	Purpose: Removes leading/trailing whitespace (or specified characters).
#  	Syntax: 	
#   		v_name.strip()
#   		v_name.rstrip()
#   		v_name.ltrip()

#  6. split()
#  	Purpose: Splits the string into a list using a delimiter (default: whitespace).
#  	Syntax: v_name.split()

#  7. join()
#  	Purpose: Joins elements of an iterable (e.g., list) into a string.
#  	Syntax: "-".join(v_name)

#  8. find()  / rfind()
#  	Purpose: Returns the index of the first occurrence of a substring (or -1 if not found).
#  	Syntax: 	
#   		v_name.find()
#   		v_name.rfind()

#  9. replace()
#  	Purpose: Replaces occurrences of a substring with another substring.
#  	Syntax:  v_name.replace(old, new)

#  10. startswith() / endswith()
#  	Purpose: Checks if the string starts/ends with a specified substring.
#  	Syntax:
#    		v_name.startswith(Character/ word) 
#    		v_name.endswith(Character/ word)

#  11. count()
#  	Purpose: Counts occurrences of a substring.
#  	Syntax:	v_name.count(Character/ word)
   
#  12. index() / rindex()
#  	Purpose: Similar to find(), but raises an error if the substring is not found.
#  	Syntax: 	
#   		v_name.index(Character)
#   		v_name.rindex(Character)

#  13. isalpha() / isdigit() / isalnum() / isnumeric() /  isspace()  
#  	Purpose: Checks if all characters are alphabets, digits, or alphanumeric or space.
#  	Syntax: 	
#   		v_name.isalpha() 
#   		v_name.isdigit() 
#   		v_name.isalnum()
#   		v_name.isnumeric()
#   		v_name. isspace()

#  14. format()
#  	Purpose: Formats a string using placeholders ({}).
#  	Syntax: v_name.format(*args, **kwargs)

#  15. partition() / rpartition()
#  	Purpose: Splits the string into a tuple of three parts using a separator.
#  	Syntax: 	
#   		v_name.partition(sep)
#   		v_name.rpartition(sep)

#  16. casefold()
#  	Purpose: Converts to lowercase for case-insensitive comparisons (stronger than lower()).
#  	Syntax: v_name.casefold()

#  17. zfill()
#  	Purpose: Pads the string with leading zeros to reach a specified width.
#  	Syntax: v_name.zfill(size)
#  	Example:
#   		s = "42"
#   		print(s.zfill(5))  # Output: "00042"

#  18. isupper() / islower() /  istitle()  
#  	Purpose: Checks if all characters are alphabets, uppercase, or lowercase  or title  	Syntax: 	
#   	v_name. isupper() 
#   	v_name.islower() 
#   	v_name.istitle()

#  19. sorted()
#  	Purpose: sort the String .
#  	Syntax: sorted(v_name) 

#  20 . len()
#  	Purpose: sort the String .
#  	Syntax: len(v_name) 