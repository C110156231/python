a=input("輸入月及日為:")
b=a.split(" ")
if((int(b[0])==1 and int(b[1])>=21) or (int(b[0])==2 and int(b[1])<=18)):
	print("Aquarius")

if((int(b[0])==2 and int(b[1])>=19) or (int(b[0])==3 and int(b[1])<=20)):
	print("Pisces")

if((int(b[0])==3 and int(b[1])>=21) or (int(b[0])==4 and int(b[1])<=20)):
	print("Aries")

if((int(b[0])==4 and int(b[1])>=21) or (int(b[0])==5 and int(b[1])<=21)):
	print("Taurus")

if((int(b[0])==5 and int(b[1])>=22) or (int(b[0])==6 and int(b[1])<=21)):
	print("Gemini")

if((int(b[0])==6 and int(b[1])>=22) or (int(b[0])==7 and int(b[1])<=22)):
	print("Cancer")

if((int(b[0])==7 and int(b[1])>=23) or (int(b[0])==8 and int(b[1])<=23)):
	print("Leo")

if((int(b[0])==8 and int(b[1])>=24) or (int(b[0])==9 and int(b[1])<=23)):
	print("Virgo")

if((int(b[0])==9 and int(b[1])>=24) or (int(b[0])==10 and int(b[1])<=23)):
	print("Libra")

if((int(b[0])==10 and int(b[1])>=24) or (int(b[0])==11 and int(b[1])<=22)):
	print("Scorpio")

if((int(b[0])==11 and int(b[1])>=23) or (int(b[0])==12 and int(b[1])<=21)):
	print("Sagittarius")

if((int(b[0])==12 and int(b[1])>=22) or (int(b[0])==1 and int(b[1])<=20)):
	print("Capricorn")