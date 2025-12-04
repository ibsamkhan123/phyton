import math #import math module
#using ceil and floor function of math module
print('The floor and ceiling values are 23.56: ' +str(math.ceil(23.56))+ ', '+ str(math.floor(23.56)))

x= 10
y = 15

#using copysign function
print('the value of x after copying the sign from y is: ' +str(math.copysign(x, y)))

#using fabs and gcd functions
print('Absolute value of -96 and 56 are: ' +str(math.fabs(-96)) + ', ' + str(math.fabs(56)))

print('the GCD of 23 and 56 is: ' + str(math.gcd(23,56)))