K=int(input())
x=input().split()

list=[int(i) for i in x]

unique=set(list)

a=sum(unique)* K
b=sum(list)

res=(a-b)/(K-1)

print(int(res))
