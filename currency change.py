print("currency change")


curr=input("usd,euro,jpy".lower())
num1=float(input("enter the value of currency you want to change:"))
if curr=="usd":
    print("rs= ",num1*87)
elif curr=="euro":
    print("rs=",num1*100)
elif curr=="jpy":
    print("rs =",num1*0.60)    
else:
    print("invalid currency")    
 