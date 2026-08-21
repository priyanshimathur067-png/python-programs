 #Mutual Followers
my_followers = set(input("Enter your followers: ").split(","))
friend_followers = set(input("Enter friend's followers: ").split(","))

my_followers = {x.strip() for x in my_followers}
friend_followers = {x.strip() for x in friend_followers}

mutual = my_followers & friend_followers
only_me = my_followers - my_followers

print("\nMutual followers:", mut- friend_followers
only_friend = friend_followers ual)
print("Only your followers:", only_me)
print("Only friend's followers:", only_friend)