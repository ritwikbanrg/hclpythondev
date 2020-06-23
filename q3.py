string=input("Enter String")
sList=[]
sList[:]=string
#print(sList)

i=0
ans=""
while (i<len(sList)-1):
    
    if (sList[i]==sList[i+1]):
        i+=2
    else:
        ans=ans+sList[i]
        i+=1
        
if(len(sList)%2==1):
    ans=ans+sList[-1]
print(ans)
