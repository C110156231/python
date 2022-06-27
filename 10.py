nm1=input("輸入N及M為:").split()
N=nm1[0]
M=nm1[1]
nm2=input("輸入正矩陣第一列為:").split()
nm3=input("輸入正矩陣第二列為:").split()

for i in range(0,3,1):
    print("輸出陣列數值第"+str(i+1)+"列為:"+ nm2[i]+" "+nm3[i])