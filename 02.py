a = int(input("輸入一個度數(正整數):"))

if a<=120:
    b=a*2.10
    c=a*2.10
elif a>120 and a<= 330:
    b=120*2.10+(a-120)*3.02
    c=120*2.10+(a-120)*2.68
elif a>331 and a<=500:
    b=120*2.10+210*3.02+(a-330)*4.39
    c=120*2.10+210*2.68+(a-330)*3.61
elif a>501 and a<=700:
    b=120*2.10+210*3.02+170*4.39+(a-500)*4.97
    c=120*2.10+210*2.68+170*3.61+(a-500)*4.01
else:
    b=120*2.10+210*3.02+170*4.39+200*4.97+(a-700)*5.63
    c=120*2.10+210*2.68+170*3.61+200*4.01+(a-700)*4.50

print("Summer months:%.2f"%(b))
print("Non-Summer months:%.2f"%(c))