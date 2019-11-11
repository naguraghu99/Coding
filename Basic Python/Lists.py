# Lists
student_names = ['Mark', 'Ram', 'Raheem', 'Katarina', 'Jessica']
print (student_names[0])
print(student_names[2])
print (student_names[-1])

student_names.append(5)

print(student_names)

if 'arthi' in student_names:
    print ('arthi is existing')
if 'Mark' in student_names:
    print ('Mark is present')

print (len(student_names))

# Delete
#del student_names[2]
print (student_names)

# List slicing
print (student_names[1:])
print (student_names[1:-1])
print (student_names[1:-2])
print (student_names[1:3])

for name in student_names:
   print('Student name is {0}'.format(name))

for index in range(len(student_names),2):
    print ('Student name is {0}'.format(student_names[index]))

# Break and continue
for name in student_names:
    if name == 'Ram':
        continue
    if name == 'katarina':
        break
    print ('Found {0}'.format(name))

# Function overloading
def add (x):
    return x+y

def add (x,y=2):
    return x+y

print (add(5))
print (add(6,7))