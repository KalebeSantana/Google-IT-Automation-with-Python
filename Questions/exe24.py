"""
<<<<<<< HEAD
Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". 
For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
"""

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
=======
Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of 
the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters 
using message[0] or message[-1]. Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
"""

def first_and_last(message):
    if message == "" or (message[0] == message[-1]):
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
>>>>>>> a59a59bbf31f35306e14af1a068a3447b55f7c09
