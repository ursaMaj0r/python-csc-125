users = []
usernames = []

# load users
for line in open('classlist.txt'):
    users.append(line)

# generate username
for user in users:
    username = ""
    data = user.split(' ')
    if len(data) == 2:
        username = data[0]
        if username in usernames:
            username += (data[1][0])
            i = 1
            while username in usernames:
                username += str(i)
                username = username.replace(str(i-1), '')
                i += 1
    else:
        username = "{}{}".format(data[0], data[1])
    usernames.append(username)
    print(username.lower())
