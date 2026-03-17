	# 							## String Functions Practices ##
		
	# 1. Write a Python program to convert the given string "hello world" to uppercase.
str = "hello world"
print("Upper: ",str.upper())

  	# 2. Convert the string "Python Programming" to lowercase.
str = "Python Programming"
print("Lower :",str.lower())

	# 3. Capitalize the first letter of "hello python learners".
str = "hello python learners"
print("Capitalize :",str.capitalize())

	# 4. Convert "welcome to python" to title case.
str = "welcome to python"
print("Title: ",str.title())

	# 5. Remove leading and trailing spaces from the string " Python String Functions " using strip().
str = " Python String Functions "
print("Strip: ",str.strip())

	# 6. Remove only trailing spaces from "Hello World " .
str = "Hello World "
print("Rstrip: ",str.rstrip())

	# 7. Remove only leading spaces from " Learn Python".
str = " Learn Python"
print("Lstrip: ",str.lstrip())

	# 8. Split the string "apple banana grape" into a list using split().
str = "apple banana grape"
print("Split: ",str.split())

	# 9. Join the list ['Python', 'is', 'fun'] into a single string using join() with space as a separator.
list1 = ['Python', 'is', 'fun']
print("Join: "," ".join(list1))

	# 10. Convert the list ['A', 'B', 'C'] into a single string "A-B-C" using join().
list2 = ['A', 'B', 'C']
print("Join: ","-".join(list2))

	# 11. Find the index of the first occurrence of "Python" in "I love Python programming".
str = "I love Python programming"
print("Index of Python: ",str.find("Python"))

	# 12. Find the last occurrence of "o" in "Hello World".
str = "Hello World"
print("Last occurrence of o: ",str.rfind("o"))

	# 13. Replace "Java" with "Python" in the string "I love Java".
str = "I love Java"
print("Replace Java with Python: ",str.replace("Java","Python"))

	# 14. Check if the string "Hello World" starts with "Hello".
str = "Hello World"
print("Starts with Hello: ",str.startswith("Hello"))

	# 15. Check if the string "example.txt" ends with ".txt".
str = "example.txt"
print("Ends with .txt: ",str.endswith(".txt"))

	# 16. Count the occurrences of "o" in "Hello, how are you?".
str = "Hello, how are you?"
print("Count of o: ",str.count("o"))

	# 17. Find the index of "r" in "programming".
str = "programming"
print("Index of r: ",str.index("r"))

	# 18. Try finding the index of "z" in "python" using index(), and observe the error.
try:
    str = "python"
    print("Index of z: ",str.index("z"))
except ValueError:
    print("ValueError raised because 'z' is not found in 'python'")

    #   19. find the last occurrence of "e" in "experience".
str = "experience"
print("Last occurrence of e: ",str.rfind("e"))

    #   20. find the first occurrence of "e" in "experience".
print("First occurance :",str.find("e"))

    #   21. Check if the string "Python" contains only alphabets.
str = "Python"
print("is python contains only alphabets:",str.isalpha())

    #   22. Verify if "12345" contains only digits.
str = "12345"
print("is 12345 contains only digits:",str.isdigit())

    #   23. Check if "Python123" is alphanumeric.
str = "Python123"
print("Is python123 is alphanumeric:",str.isalnum())

    #   24. Test if the string " " consists of only spaces.
str = " "
print("Is string with only spaces:",str.isspace())

    #   25. Check if "12345" is numeric using.
str = "12345"
print("is string numeric:",str.isnumeric())

    #   26. Use format() to insert "Python" and "fun" into the string "{} is {}!".
print("{} is {}!".format("Python","fun"))

    #   27. Partition the string "python-programming-language" at "-".
str = "python-programming-language"
print("Partition the string at -:",str.partition("-"))

    #   28. Use rpartition() to split "one-two-three" from the right sing "-".
str = "one-two-three"
print("Rpartition the string at -:",str.rpartition("-"))

    #   29. Convert "PYTHON" to lowercase using casefold().
str = "PYTHON"
print("To lower case using casefold:",str.casefold())

    #   30. Convert "42" into a 5-character string padded with zeros using zfill().
str = "42"
print("Zero-padded string:",str.zfill(5))

    #   31. Check if "HELLO" is in uppercase.
str = "HELLO"
print("Is hello uppercase:",str.isupper())

    #   32. Verify if "hello" is in lowercase.
str = "hello"
print("Is hello lowercase:",str.islower())

    #   33. Check if "Python Programming" follows title case.
str = "Python Programming"
print("IS str follows title case:",str.istitle())

    #   34. Sort the characters of "banana" alphabetically.
str = "banana"
print("Sorted characters of banana:",sorted(str))

    #   35. Find the length of the string "Data Science".
str = "Data Science"
print("Length of th string data science:",len(str))

    #   36. Sort the characters of "The Kiran  Academy" alphabetically in descending Order.
str = "The Kiran  Academy"
print("Sorted characters of The Kiran Academy in descending order:",sorted(str))


# Slicing
# String iteration 
# # String method
# a = "Instagram"
# # -9    -8  -7  -6  -5  -4  -3  -2  -1
# #  I    N   S   T   A   G   R   A   M
# #  0    1   2   3   4   5   6   7   8
# # print(a[0:5]) # start index is included and end index is excluded

# # Case 1: Starting index is optional and default value is 0
# print(a[:5]) 
# print(a[3:6])

# # Case 2: End index is also optional and default value is length of string
# print(a[6:]) # start index is included and end index is excluded

# # Case 3: Both starting and end index is optional and default value of starting index is 0 and end index is length of string
# print(a[:]) # start index is included and end index is excluded

# # Prints blank space because starting and end index is same
# print(a[3:3]) 
# # Prints single character because end index is one more than starting index
# print(a[3:4])
# # prints string from starting index to end
# print(a[6:19]) 
# # print string with step valueof 2
# print(a[0:9:2])
# print(a[:9:2])
# print(a[::2])

# # print from 3 to 5
# print(a[3:6:1])
# # print from 6 to 4
# # 
# print(a[6:3:-1])

# # prints reverse of string
# print(a[::-1])
# print(a[-1:-10:-1])

# print(a[-6:8:1]) 
# print(a[-6:8:2]) 
# print(a[-6:8:5]) 

# Task :
# 5 positive + positive index
# 5 positive + negative index
# 5 negative + negative index
# 5 negative + positive index

# 5 on +ve step size >1 2 3 4 5
# 5 on -ve step size >-1 -2 -3 -4 -5

a = "Bhushan Khedekar"
#  -15  -14  -13  -12  -11  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
#  B     H    U    S    H    A    N    K    H    E    D    E    K    A    R
#  0     1    2    3    4    5    6    7    8    9   10   11   12   13   14

# 5 positive + positive index
print(a[0:15])
print(a[0:7])
print(a[7:15])
print(a[0:15:2])
print(a[1:5])

# 5 positive + negative index
print(a[0:-8])
print(a[7:-1])
print(a[0:-1])
print(a[0:-1:2])
print(a[: :-1])

# 5 negative + negative index
print(a[-9::-1])
print(a[-1:-9:-1])
print(a[-1:-15:-1])
print(a[-1:-15:-2])
print(a[:-16:-1])

# 5 negative + positive index
print(a[-1:0:1])
print(a[-9:15:1])
print(a[-9:15:2])
print(a[-9:15:3])
print(a[-9:15:4])

# 5 on +ve step size >1 2 3 4 5
print(a[0:15:1])
print(a[0:15:2])
print(a[0:15:3])
print(a[0:15:4])
print(a[0:15:5])

# 5 on -ve step size >-1 -2 -3 -4 -5
print(a[14:0:-1])
print(a[14:0:-2])
print(a[14:0:-3])
print(a[14:0:-4])
print(a[14:0:-5]) 
