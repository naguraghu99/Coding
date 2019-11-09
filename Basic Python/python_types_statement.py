# This example is to illustrate the data types in python

def add(a,b):
    return a+b


def main():
    print (add(5,6))

    # Python is not a strongly typed language
    print (add('srinath',' raghunathan'))

    answer = 42
    pi = 3.14159

    print (answer+pi)  # Don't worry about conversion

    # Strings
    s = 'hello world'
    print (s.capitalize())
    print (s.replace('e','o'))
    print (s.isalpha())
    print (s.isdigit())

    name = 'PythonNagu'
    machine = 'HAL'

    print ('Nice to meet you {0}. I am {1}'.format(name, machine))

    number = 5
    if number:
        print('Number is defined and truthy')

    text = 'Python'
    if text:
        print('Text is defined and truthy')

    python_course = None

    if python_course:
        print('This will not be excuted as python_course is none')
    
    a = 1
    b = 2

    'bigger' if b > a else 'smaller'

    


if __name__ == '__main__':
    main()