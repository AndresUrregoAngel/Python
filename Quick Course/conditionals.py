# _*_ coding:utf-8 _*_

'''Example exercices for
conditionals if, else, ifelse, case'''

## Example if and if-else

z= input('type the first number between 1 - 10:')
if (int(z) > 5):
    print('the number is greater than 5, your number is: ', z)

name = input('what is your name?')

if (name != 'Owen'):
    print('this name its not accepted')
else:
    print('your name is such a great alias')

### examples based on the project

answer = input('what is the auxiliar(to-be) for the pronom I in present?')

if (answer.lower == 'am'):
    print('you are right , the answer is I am')
else:
    print('you should practice a bit more the answer is: am ')

answer = input('Type and pronoun to give you the auxiliar in present (to-be)')
print('the pronoun provided is:{}'.format(answer.upper()))

if ( answer.upper() == 'I' ):
    print('the pronoun is I, the conjugation is : I am')
elif (answer.upper() == 'YOU'):
     print('the pronoun is YOU the conjugation is: You are')
elif (answer.upper() == 'HE'):
     print('the pronoun is HE the conjugation is: He is')
elif (answer.upper() == 'SHE'):
     print('the pronoun is SHE the conjugation is: She is')
elif (answer.upper() == 'IT'):
     print('the pronoun is IT the conjugation is: It is')
elif (answer.upper() == 'WE'):
     print('the pronoun is WE the conjugation is: We are')
elif (answer.upper() == 'THEY'):
     print('the pronoun is THEY the conjugation is: They are')
else:
     print('The pronoun you provided is not valide')

## Examples
