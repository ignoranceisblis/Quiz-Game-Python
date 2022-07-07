print("--- Welcome To The Game ---")
print("--- There are 4 different question ---")
print("--- All true answer has 10 point ---")
print("--- All wrong answer has -5 point ---")

point = 0
playing = input("Do you want to play(yes/no)? ---->")

if playing.lower() != 'yes':
    quit()

question = 1
print("----- Question {} -----".format(question))
answer = input("What does CPU stand for?\n")
if answer.lower() == "central processing unit":
    print('True')
    point = point +10
else:
    print("False")
    point = point -5
question = question +1
print("----- Question {} -----".format(question))
answer = input("What does GPU stand for?\n")
if answer.lower() == "graphics processing unit":
    print('True')
    point = point +10

else:
    print("False")
    point = point -5
question = question +1


print("----- Question {} -----".format(question))
answer = input("What does RAM stand for?\n")
if answer.lower() == "random access memory":
    print('True')
    point = point +10

else:
    print("False")
    point = point -5
question = question +1

print("----- Question {} -----".format(question))
answer = input("What does PSU stand for?\n")
if answer.lower() == "power supply":
    print('True')
    point = point +10

else:
    print("False")
    point = point -5
question = question +1

print("----- Game Statistics -----")
if (point== 40):
    print(" Well Done you gave true answer for all questions and your score is {} ".format(point))
else:
    print("Your score is {} ".format(point))

