### Bracer balance

votes =["{}[]()","{[}]}]"]
print(votes[-1],votes.pop())
opening = tuple('({[')
closing = tuple(')}]')
mapping = dict(zip(opening, closing)) # zip appends two lost in set or dict
print(mapping['{'])
print(mapping)
queue = []

print(range(len(votes)))
for i in range(len(votes)):
    for letter in votes:
        print(letter[i])
    if letter in opening:
        queue.append(mapping[letter])
    elif letter in closing:
        if not queue or letter != queue.pop(): # pop removes the last element on a list
            print('false')

            
# Elections challenge
def electionWinner(votes):
    try:
      
        votescounting = []
        # Gather candidates name
        candidatename = [item for item in votes if type(item) != int  ]

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
                if i['votes'] == j['votes']:
                    candidatew = i['candidate']
                elif i['votes'] < j['votes']:
                    candidatew = j['candidate']
            winners.append(candidatew)
        
   
    except  Exception as error:
        print('there is an error in the method : {}'.format(error))
    
    else: 
        return winners[:1]

votes = [6,'Pablo','Pablo','Alice','Allison','Alice','Allison','Ashley','Ashley','Raul','Raul','Raul','Pablo','Pablo']

result = electionWinner(votes)
print(result)
    


ltest = [2,4,5,6,7,82,4]
result = [i  for i in ltest if i > 5] # comprehension
result = [ i + 10 if i < 5 else  i for i in ltest ] # comprehension with if/else
x = lambda a : a + 5 #lambda example
print(x(5))

print(result)
