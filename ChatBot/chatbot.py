BOT_NAME = "Drus"
BIRTH_YEAR = "2023"

print("Hello! My name is " + BOT_NAME)
print("I was created in " + BIRTH_YEAR)
user_name = str(input("Please, remind me your name: "))
print("What a great name you have, " + user_name + "!")
print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105 # 1 4 5

print("Your age is " + str(age) + "; that's good time to start programming!")
print("Now i Will prove to you that I can count to any number you want")

number = int(input())
if number > 0:
    for i in range(number+1):
        print(str(i) + " !")
    print("Completed, have a nice day!")
else:
    print("Number is negative or 0")

print("Let's test your knowledge of biology.\nHow many pairs of chromosomes does a human have?")
print("1. 25\n2. 24\n3. 17\n4. 23")
answer = int(input())
while answer != 4:
    print("Please, try again.")
    answer = int(input())
print("Congratulations, have a nice day!")