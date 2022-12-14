# The validate_users function is used by the system to check if a list of users is valid or
# invalid. A valid user is one that is at least 3 characters long. For example,
# ['taylor', 'luisa', 'jamaal'] are all valid users. When calling it like in this example,
# something is not right. Can you figure out what to fix?

def is_valid(user):
    if len(user) >= 3:
        return 1
    return 0

def validate_users(users):
  for user in users:
    if is_valid(user):
        print(user + " is valid") # purplecat is valid
    else:
        print(user + " is invalid") # pu is invalid

validate_users(["purplecat", "pu"])