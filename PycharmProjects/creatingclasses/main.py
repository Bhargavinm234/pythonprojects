class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


#user_1 = User()
# user_1.id = "001"
# user_1.username = "Bhargavi"
# print(user_1.username)

user_1 = User("1","bhargavi")

user_2= User("2","angela")
print(user_2.name)
# print(user_2.followers)

user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)