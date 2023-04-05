from random import randint

minimum_number=1

maximum_number=20

number_of_attemps=0

user_name=input("enter your username: ")


random_number=randint(minimum_number,maximum_number)

print(random_number)

print(f"welcome {user_name} you have to guess a number from {minimum_number} to {maximum_number}")

