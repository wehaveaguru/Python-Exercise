from english_words import get_english_words_set
import random
d=get_english_words_set(['web2'],lower=True)
d_list=list(d)

word=random.choice(d_list)
s=[]
for i in word:
    s+='_'
print(word)
for i in s:
    print(i,end='')

a=6
while True:
    guess=input("\n\nguess a letter ")
    for i in range(len(word)):
        if guess==word[i]:
            s[i]=guess
    
            continue
    if guess not in word:
        a-=1
    if a<=0:
        print(f"you lose. the word is {word}")
        break
    if "".join(s)==word:
        print('you win')
        break
    print("".join(s))
    
