<<<<<<< HEAD
import wikipedia

#Topic of their interest: ex- politics, art, literature, music etc
print("Choose the  topic of your interest: ")
list_of_topic=['Politics', 'Art', 'Science', 'Music', 'Literature']
for i in range(len(list_of_topic)):
    print(i+1,". ",list_of_topic[i])

choice=int(input())
choice-=1

list_of_Politics=["narendra modi", "rahul gandhi"]
list_of_Art=["madhubani painting", "kathak"]
list_of_Science=["mangalyan", "chandrayan"]
list_of_Music=["lata mangeshkar", "arijit singh"]
list_of_Literature=["william shakespeare", "pablo neruda"]
chosen=[]
#A/c to their choice, ask either directly make a list of the concerned topic or user can also add in the list
if(choice==0):
    chosen=list_of_Politics
elif(choice==1):
    chosen=list_of_Art
elif(choice==2):
    chosen=list_of_Science
elif(choice==3):
    chosen=list_of_Music
elif(choice==4):
    chosen=list_of_Literature
else:
    print("Invalid Choice")
    
    

k=len(chosen)
for i in range(k):
    print(i+1, ". ",chosen[i].upper(), " :")
    print(wikipedia.summary(chosen[i], sentences=2))
    print("")

print("Enter the SNO. of the data in which you are most interested :")
SNo=int(input())
SNo=SNo-1
=======
import wikipedia

#Topic of their interest: ex- politics, art, literature, music etc
print("Choose the  topic of your interest: ")
list_of_topic=['Politics', 'Art', 'Science', 'Music', 'Literature']
for i in range(len(list_of_topic)):
    print(i+1,". ",list_of_topic[i])

choice=int(input())
choice-=1

list_of_Politics=["narendra modi", "rahul gandhi"]
list_of_Art=["madhubani painting", "kathak"]
list_of_Science=["mangalyan", "chandrayan"]
list_of_Music=["lata mangeshkar", "arijit singh"]
list_of_Literature=["william shakespeare", "pablo neruda"]
chosen=[]
#A/c to their choice, ask either directly make a list of the concerned topic or user can also add in the list
if(choice==0):
    chosen=list_of_Politics
elif(choice==1):
    chosen=list_of_Art
elif(choice==2):
    chosen=list_of_Science
elif(choice==3):
    chosen=list_of_Music
elif(choice==4):
    chosen=list_of_Literature
else:
    print("Invalid Choice")
    
    

k=len(chosen)
for i in range(k):
    print(i+1, ". ",chosen[i].upper(), " :")
    print(wikipedia.summary(chosen[i], sentences=2))
    print("")

print("Enter the SNO. of the data in which you are most interested :")
SNo=int(input())
SNo=SNo-1
>>>>>>> a4964fe428be9e72c391e968ae0c1ea683af0357
print(wikipedia.summary(chosen[SNo]))