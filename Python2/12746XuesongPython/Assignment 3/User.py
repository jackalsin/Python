class User:
    name = ''

    def __init__(self, name):
        self.name = name
        self.friends = list()
    # Send the request to view another user's friend list
    # Print a list of all friends of that user if they are friends.
    # Print a list of only mutual friends if they are not friends.
    def requestProfile(self, user):
        reqList = list(user.friends)
        if self.name in set(reqList):
            print reqList
        else:
            print list(set(self.friends).intersection(set(reqList)))

    def __repr__(self):
        return "name = " + self.name + ", friends = " + str(self.friends)