a=list(input("輸入一整數序列為:").split())
b=int(len(a))/2

for i in range (len(a)):
    if a.count(a[i])>b:
        ans=a[i]
        print("過半元素為",str(ans))
        break
    else:
        print("NO")
        break