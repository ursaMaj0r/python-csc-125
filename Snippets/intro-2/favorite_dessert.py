#define variables
desserts = {}

# prompt for input
vote = input('Name:vote ')
while vote:
    voter,dessert = vote.split(':')
    
    if dessert in desserts:
        desserts[dessert].append(voter)
    else:
        desserts[dessert] = [voter]
    
    vote = input('Name:vote ')

for dessert in desserts:
    print(dessert, len(desserts[dessert]), 'vote(s):', ' '.join(desserts[dessert]))