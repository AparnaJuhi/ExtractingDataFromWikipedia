import wikipedia

#Topic of their interest: ex- politics, art, literature, music etc




#A/c to their choice, ask either directly make a list of the concerned topic or user can also add in the list



#Now,view the summary of each topic added to the list, and then ask the topic which user wanna explore now
print("Here's a list of information in which you might be interested in")
li=['google','narendra modi']
k=len(li)
for i in range(k):
    print(i+1, ". ",li[i].upper(), " :")
    print(wikipedia.summary(li[i], sentences=2))
    print("")

print("Enter the SNO. of the data in which you are most interested :")
SNo=int(input())
SNo=SNo-1
print(wikipedia.summary(li[SNo]))