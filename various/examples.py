votes =[2,
'{}[]()',
'{[}]}]']

print(votes)
braces = ['(',')']
for i in votes:
    if type(i) == int:
        pass
    else:

        for n in range(len(i)):
            print(i[n])

def electionWinner(votes):
    try:
        candidatename = []
        votescounting = []
        totalvotes = 0
        # Gather candidates name
        for name in votes:
            if type(name) == int:
                totalvotes = name
            elif name not in candidatename:
                candidatename.append(name)

        # Calculate individual votes
        for name in candidatename:
            qvote = 0
            for vote in votes:
                
                if type(vote) == int:
                    pass
                elif vote == name:
                    qvote += 1

            record = { 'candidate' : name , 'votes' : qvote }
            votescounting.append(record)

        # Find the winner
        winners = []
        candidatew = ''
        for i in votescounting:
            for j in votescounting:
                if i['votes'] <= j['votes']:
                    candidatew = j['candidate']
                else:
                    candidatew = i['candidate']
            winners.append(j['candidate'])
    except  Exception as error:
        print('there is an error in the method : {}'.format(error))
    
    else: 
        return winners
    


ltest = [2,4,5,6,7,82,4]
result = [i  for i in ltest if i > 5] # comprehension
x = lambda a : a + 5 #lambda example
print(x(5))

print(result)
