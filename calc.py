# -----------------------------------
import math
import os
# -----------------------------------
def add(x, y):# adding
	return float(x) + float(y)
# -----------------------------------
def sub(x, y): #subtracting
	return float(x) - float(y)
# -----------------------------------
def mlt(x, y): #multiplying
	return float(x) * float(y)
# -----------------------------------
def div(x, y): #dividing
	return float(x) / float(y)
# -----------------------------------
def com(x, y):
	if x > y:
		return '>'
	elif x == y:
		return '='
	elif x < y:
		return '<'
	else:
		return 'Bad Input. Try Again'
# -----------------------------------
def rnd(x):
	numround = float(x) - int(x)
	if numround < 0.5:
		return math.floor(x)
	else:
		return math.ceil(x)
# -----------------------------------
def pwr(x, y):
	return math.pow(x, y)
# -----------------------------------
print('---------------')
print('Choose an operation:')
print('---------------')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('---------------')
print('5.Compare')
print('6.Round')
print('7.Powers')
print('---------------')
# -----------------------------------
oper = input('Enter choice (1/2/3/4/5/6/7):')
# -----------------------------------
num1 = float(input('Number 1?:'))
if not oper == '6' and not oper == '0':
	num2 = float(input('Number 2?:'))
# -----------------------------------+
if oper == '1':
	print(num1,'+',num2,'=',add(num1, num2))
elif oper == '2':
	print(num1,'-',num2,'=',sub(num1, num2))
elif oper == '3':
	print(num1,'*',num2,'=',mlt(num1, num2))
elif oper == '4':
	print(num1,'/',num2,'=',div(num1, num2))
elif oper == '5':
	print(num1,com(num1, num2),num2)
elif oper == '6':
	print(num1,'~=',rnd(num1))
elif oper == '7':
	print(num1,'**',num2,'=',pwr(num1, num2))
else:
	print('Bad Input. Try Again')
# -----------------------------------