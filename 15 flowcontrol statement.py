# Conditional 
# if, if-else, if-elif-else

# Iteratie
# for, while-loop

# Transfer 
# pass, break, continue

# Homework

student_marks = [85, 92, 78, 63, 44, 91, 56, 73, -30, -40]

even_marks = []
odd_marks = []

for mark in student_marks:
    if mark % 2 == 0:
        even_marks.append(mark)
    else:
        odd_marks.append(mark)

print("Even Marks:", even_marks)
print("Odd Marks:", odd_marks)

