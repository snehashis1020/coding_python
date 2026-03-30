first=0;
second=1;
print("fibonacci series")
num=int(input("enter the length of esries"))
print(first)
print(second)
for i in range(2,num):
     next=first+second
     print(next)
     first=second
     second=next
