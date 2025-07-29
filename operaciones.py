print('introduce un numero grande')
num = input()
n= int(len(num))
#suma
sum=int(0)
#multiplicacion 
mult = int(1)
#division contra el ultimo digito diferente de cero
div=0
dividendo=0
d = -1
#resta de impares
resta = 0
sumadeimpares = 0
sumadepares=0
for i in range(n):
    sum = sum + int(num[i])
    mult = mult * int(num[i])
    if num[d] == '0':
        d = d-1
    else:
        dividendo = sum + int(num[i])
        div= dividendo / int(num[d])
    if int(num[i]) % 2 != 0:
        sumadeimpares = sumadeimpares + int(num[i])
    else:
        sumadepares = sumadepares + int(num[i])
resta = sumadepares-sumadeimpares
print('El resultado de la suma de los digitos es ',resta)
print('El resultado de la multiplicacion de los digitos es ',mult)
print('El resultado de la suma del string es ',sum)
print('El resultado de la division de la suma de los digitos entre el ultimo digito diferente de cero es ',div)
