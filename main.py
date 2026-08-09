user_name = input('What is your name...')

print(f"Your name {user_name} has {len(user_name)} characters!")

# let's add a function
if len(user_name) <= 5:
    print("You have a short name")
else:
    print('You have a long name')
