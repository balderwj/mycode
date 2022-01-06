#!/usr/bin/env python3

prompt = "your score on the test is: "

testscore = float(input("Enter your test score to receive your grade>> "))

if testscore >= 90:
    prompt = prompt + 'you received an A great job!'

elif testscore >= 80:
    prompt = prompt + 'you received a B.. Almost there!'

elif testscore >= 70:
    prompt = prompt + 'you recieved a C..Need some work!'

else:
    prompt = prompt + 'you did not pass get back in the books!'

print(prompt)


