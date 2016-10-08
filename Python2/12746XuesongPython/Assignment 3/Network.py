from User import User

def friend(A, B): # Friend a pair of users
    bFriends = set(B.friends)
    if A.name not in bFriends:
        B.friends.append(A.name)
    if B.name not in set(A.friends):
        A.friends.append(B.name)

def unfriend(A, B): #Unfriend a pair of users
    if A.name in set(B.friends):
        print B.name + " unfriends with " + A.name
        B.friends.remove(A.name)
    if B.name in set(A.friends):
        print A.name + " unfriends with " + B.name
        A.friends.remove(B.name)


Amy = User('Amy')
Billy = User('Billy')
Catherine = User('Catherine')
David = User('David')

friend(Amy, Billy)
friend(Catherine, David)
friend(Amy, Catherine)
friend(Billy, Catherine)
David.requestProfile(Amy)
friend(David, Amy)
David.requestProfile(Amy)
