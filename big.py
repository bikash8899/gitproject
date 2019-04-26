#Prog to count highest occurance of a word 
counts = {}
inp = input("Enter a line of text: ")
lst = inp.split()
for word in lst:
    counts[word]=counts.get(word,0)+1

bigword = None
bigcount = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)
