user_name = input('What is your name...')
user_age = input("What is your age?: ")

print(f"Your name {user_name} has {len(user_name)} characters!")
print(f"Your age is {user_age}")

if len(user_name) <= 5:
    print("Your name is short")
else:
    print('You have a long name!')
