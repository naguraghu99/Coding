# Python Dictonary

student = {
    'name' : 'Srinath',
    'age'  : 25,
    'feedback': None
}

# List of dicts
list_student = [
    {'name' : 'Srinath','age'  : 25,'feedback': None},
    {'name' : 'Nagu','age'  : 30,'feedback': None}
]

print (student.keys())
print (student.values())


try:
    print (student['class'])
except Exception as e:
    print ('Could not find the key ',e)

print ((3,5,"Mark"))

set_s = set([3,2,3,1,5])
print (set_s)