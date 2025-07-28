print('introduce un numero grande')
num = input()
n= int(len(num))
#print (n)
sum=int(0)
mult = int(1)
for i in range(n):
    sum = sum + int(num[i])
    mult = mult * int(num[i])
print('El resultado de la multiplicacion de los digitos es ',mult)
print('El resultado de la suma del string es ',sum)

