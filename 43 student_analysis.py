# 1. Calculate the average student marks from the file.

# import os
# def avg_marks(file):
#     base_dir = os.path.dirname(__file__)
#     path = os.path.join(base_dir, file)
#     total = 0.0
#     count = 0
#     with open(path, 'r') as f:
#         for line in f:
#             line = line.strip()
#             if not line:
#                 continue
#             parts = line.split(',')
#             marks = parts[-1].strip()
#             try:
#                 m = float(marks)
#             except ValueError:
#                 continue
#             total += m
#             count += 1

#     if count == 0:
#         return 0.0
#     return total / count

# if __name__ == '__main__':
#     print(avg_marks('student_records.txt'))



# 2. Create functions for the following:
# calculate total paid fees

# calculate total remaining fees

# calculate course wise total paid fees by course name

# calculate remaining fees by branch name


# def _read_fee_records(file_name='student_records.txt'):
#     import os

#     base_dir = os.path.dirname(__file__)
#     path = os.path.join(base_dir, file_name)
#     records = []

#     with open(path, 'r', encoding='utf-8') as f:
#         lines = [line.strip() for line in f if line.strip()]

#     if not lines:
#         return records

#     header = [h.strip() for h in lines[0].split(',')]
#     try:
#         paid_index = header.index('paid_fees')
#         remaining_index = header.index('remaining_fees')
#         course_index = header.index('course_name')
#         branch_index = header.index('branch_name')
#     except ValueError:
#         return records

#     for line in lines[1:]:
#         parts = [p.strip() for p in line.split(',')]
#         if len(parts) <= max(paid_index, remaining_index, course_index, branch_index):
#             continue
#         try:
#             paid = float(parts[paid_index])
#             remaining = float(parts[remaining_index])
#         except ValueError:
#             continue

#         records.append({
#             'paid': paid,
#             'remaining': remaining,
#             'course': parts[course_index],
#             'branch': parts[branch_index],
#         })

#     return records


# def calculate_total_paid_fees(file_name='student_records.txt'):
#     records = _read_fee_records(file_name)
#     return sum(record['paid'] for record in records)
# print(calculate_total_paid_fees())


# def calculate_total_remaining_fees(file_name='student_records.txt'):
#     records = _read_fee_records(file_name)
#     return sum(record['remaining'] for record in records)
# print(calculate_total_remaining_fees())


# def calculate_course_wise_paid_fees(file_name='student_records.txt'):
#     totals = {}
#     records = _read_fee_records(file_name)
#     for record in records:
#         totals.setdefault(record['course'], 0.0)
#         totals[record['course']] += record['paid']
#     return totals
# print(calculate_course_wise_paid_fees())

# def calculate_branch_wise_remaining_fees(file_name='student_records.txt'):
#     totals = {}
#     records = _read_fee_records(file_name)
#     for record in records:
#         totals.setdefault(record['branch'], 0.0)
#         totals[record['branch']] += record['remaining']
#     return totals
# print(calculate_branch_wise_remaining_fees())


# if __name__ == '__main__':
#     print('Total paid fees:', calculate_total_paid_fees())
#     print('Total remaining fees:', calculate_total_remaining_fees())
#     print('Course wise paid fees:', calculate_course_wise_paid_fees())
#     print('Branch wise remaining fees:', calculate_branch_wise_remaining_fees())
    
# 603@thekiranacademy.com

# import os

# def total_remaining_fees(file, branchname):
#     f = open(file,'r')
#     sum = 0
#     for data in f:
#         data = data.strip('\n')
#         l = data.split(",")
#         rf = l[-2]
#         branch = l[2]
#         if branch.lower() == branchname.lower():
#             if rf.isnumeric():
#                 sum = sum + int(rf) 
#     return sum 

# if __name__ == '__main__':
#     print(total_remaining_fees('student_records.txt', 'karve nagar'))   


# import os

# def total_remaining_fees(file_name, branch_name):
#     base_dir = os.path.dirname(__file__)
#     path = os.path.join(base_dir, file_name)

#     total = 0.0
#     with open(path, 'r', encoding='utf-8') as f:
#         for line in f:
#             line = line.strip()
#             if not line:
#                 continue
#             parts = [part.strip() for part in line.split(',')]
#             if len(parts) < 3:
#                 continue

#             branch = parts[2]
#             remaining = parts[-2]

#             if branch.lower() == branch_name.lower():
#                 try:
#                     total += float(remaining)
#                 except ValueError:
#                     continue

#     return total

# if __name__ == '__main__':
#     print(total_remaining_fees('student_records.txt', 'karve nagar'))


# import os

# def total_fees_all_branches(file_name):
#     base_dir = os.path.dirname(__file__)
#     path = os.path.join(base_dir, file_name)

#     total = 0.0
#     with open(path, 'r', encoding='utf-8') as f:
#         for line in f:
#             line = line.strip()
#             if not line or line.lower().startswith('reg_no'):
#                 continue
#             parts = [p.strip() for p in line.split(',')]
#             if len(parts) < 8:
#                 continue

#             try:
#                 paid = float(parts[6])
#                 remaining = float(parts[7])
#             except ValueError:
#                 continue

#             total += paid + remaining

#     return total

# if __name__ == '__main__':
#     print(total_fees_all_branches('student_records.txt'))



# import os
# print(os.getcwd())
# os.chdir('C:/kiran Academy/5 Data Analysis')
# def total_remaining_fees(file, branchname):
#     f = open(file,'r')
#     sum = 0
#     for data in f:
#         data = data.strip('\n')
#         l = data.split(",")
#         rf = l[-2]
#         branch = l[2]
#         if branch.lower() == branchname.lower():
#             if rf.isnumeric():
#                 sum = sum + int(rf) 
#     return sum 

# # if __name__ == '__main__':
# print(total_remaining_fees('student_records.txt', 'karve nagar'))

# l1 = [1, 1, 2, 4, 3, 9, 4, 16]
# sqrt = {}
# for i in l1:
#     sqrt[i] = i ** 2
# print(sqrt)

l1 = [1, 1, 2, 4, 3, 9, 4, 16]

d = {}

for i in range(0, len(l1), 2):

    d[l1[i]] = l1[i + 1]

print(d)