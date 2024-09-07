n=int(input("enter a number: "))
if n%2==0:
    half=n//2
else:
    half=n//2+1
space=half-1
for c in range(1,half+1):
    for d in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for d in range(2*c-1):
        print(str(num),end="")
        num=num+1
    print()
space=1
for c in range(1,half):
    for d in range(1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for d in range(1,2*(half-c)):
        print(str(num),end="")
        num=num+1
    print()