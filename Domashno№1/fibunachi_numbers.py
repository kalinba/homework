"""
1. Напишете програма,която взима число n от input
и генерира редица на фибоначи до този елемент като я принтира на екрана.
Пример n = 10 - 1, 1, 2, 3, 5, 8

"""
n=int(input("Please enter a number:"))
num1=0
num2=1
sum=num1+num2
print(num1)
print(num2)
while n>=sum :
    print(sum)
    num1=num2
    num2=sum
    sum=num1+num2
