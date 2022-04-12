class User:
    def __init__(self, user_id, username):
        print("new user being created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "William")
user_2 = User("001", "Christine")

user_1.follow(user_2)

print(user_1.id, user_1.username, f"Has {user_1.followers} followers,", f"Is following {user_1.following} people")
print(user_2.id, user_2.username, f"Has {user_2.followers} followers,", f"Is following {user_2.following} people")