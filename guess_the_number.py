import random


random_no=int(random.random()*100)
print(random_no)
number_of_attempts=10
for i in range(number_of_attempts):
    print(i)       
    gussed=int(input("enter the no"))
    if random_no==gussed:
        print("correct guess")
        break
    elif random_no>gussed:
        print("gussed no is too low")
    elif random_no<gussed:
        print("gussed no is too high")