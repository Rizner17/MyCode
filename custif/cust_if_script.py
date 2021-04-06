#!/usr/bin/env python3

"""AJRodriguez | Lab 19 custom if/elif/else script
    Grading Scale
"""

message = 'Will the student pass? '

# wrap connection in a float() to accept decimals as numbers
score = int(input("What was the student's test result?"))

# if input value was higher or equal to 90
if score >= score >= 90:
    message = message + 'Yes, this student has recieved an A.'
elif score <= 89 and score >=80:
    message = message + 'Yes, the student passed with a B.'
elif score <= 79 and score >= 70:
    message = message + 'Yes, but the student got a C and needs some work.'
elif score <= 69 and score >= 60:
    message = message + 'No, this student scored a D and is in danger of failing.'
else:
    message = message + 'This student has received and F and will have to retake the test.'
print(message)
