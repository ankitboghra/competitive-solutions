Modify the String

You are given with a string SS of length NN. You have to sort the string SS in such way that when individual characters are converted to their ASCII values, they should follow given rules:

Characters possessing prime ASCII value should come before characters possessing non-prime ASCII value.
If two characters are having prime ASCII value, character having less ASCII value should come before the other.
If two characters are having non-prime ASCII value, character having greater ASCII value should come before the other.
Input Format

The first line of the input contains NN, the length of string SS.
The second line of input contains string SS.
Constraints

1 <= NN <= 100000
33 <= ASCII values of characters <= 126
Output Format

Output the sorted string.
_______________________________________

def isprime(c):
    num=ord(c)
    if (num <= 1):
        return False

    for i in range(2, num):
        if (num % i == 0):
            return False 
    return True
    
n=int(input())
st=[c for c in input()]
prime=[]
nonprime=[]
for c in st:
    if(isprime(c)):
        prime.append(c)
    else:
        nonprime.append(c)

prime.sort();
nonprime.sort(reverse=True);

for c in prime:
    print(c,end='')
for c in nonprime:
    print(c,end='')
    