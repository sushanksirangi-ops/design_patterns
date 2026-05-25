def auth_required(func):
    def wrapper(user_authenticated):
        if not user_authenticated:
            print("Access Denied")
            return
        print("Authentication Successful")
        return func(user_authenticated)

    return wrapper