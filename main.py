user_name = input('What is your name...')

print(f"Your name {user_name} has {len(user_name)} characters!")

if len(user_name) <= 5:
    print("Your name is short")
else:
    print('You have a long name!')
