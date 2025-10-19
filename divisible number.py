print("Enter A Number (Numerator): ")
numn = int(input())
print("Enter A Number (Denominator): ")
numd = int(input())

if numn%numd==0:
   print("\n" +str(numn)+" is divisible by" +str(numd))
else:
     print("\n" +str(numn)+" is not divisible by" +str(numd))