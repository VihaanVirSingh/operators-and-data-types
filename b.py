name = input("Enter your name: ")
age = input("Enter your age: ")
S1 = "Hello, "
S2 = " welcome to your maths test"
print(S1 + name + S2)
print("     Question No. 1")
print("2**5 is equal to: " )
print(      "A 265    B 256    C 512   D 128"    )
ans1 = input("Your answer: ")
isAnswerCorrect1 = True if str(ans1) == "256" else False
print(isAnswerCorrect1)
M1 = 1 if str(isAnswerCorrect1) == "True" else 0

print("     Question No. 2")
print(" Extention used for python files is: " )
print(      "A .ppt    B .png    C .py   D .jpg"    )
ans2 = input("Your answer: ")
isAnswerCorrect2= True if str(ans2) == ".py" else False
print(isAnswerCorrect2)
M2 = 1 if str(isAnswerCorrect2) == "True" else 0

print("     Question No.3 ")
print("who is the father of india : " )
print(      "A. P M Modi     B. Mahatma Gandhi     C. Dr. B R Ambedkar    D. Dr. A P J Abdul Kalam "    )
ans3 = input("Your answer: ")
isAnswerCorrect3 = True if ans3 == "Mahatma Gandhi" else False
print(isAnswerCorrect3)
M3 = 1 if str(isAnswerCorrect3) == "True" else 0

print("     Question No.4 ")
print("Ful form of AI is: " )
print(      "A. Artificial Intelligence     B. Authorised Identity     C. Agent Instructions    D. Artifact Illusteration"    )
ans4 = input("Your answer: ")
isAnswerCorrect4 = True if str(ans4) == "Artificial Intelligence" else False
print(isAnswerCorrect4)
M4 = 1 if str(isAnswerCorrect4) == "True" else 0

print("     Question No.5 ")
print("In computer python is: " )
print(      "A. A type of snake     B. Programming language    C. Both A and B    D. None of the above "    )
ans5 = input("Your answer: ")
isAnswerCorrect5 = True if str(ans5) == "Programming language" else False
print(isAnswerCorrect5)
M5 = 1 if str(isAnswerCorrect5) == "True" else 0

TotalMark = (M1 + M2 + M3 + M4 + M5)
print()

A1 = "You have got "
A2 = " marks in this test"
print(A1 + str(TotalMark) + A2 )

C1 = "Result is:  "
res = "Pass" if TotalMark >= 3 else "Fail"
res2 = " Well done" if TotalMark >= 3 else " Try hard"
print(C1 + res + res2)