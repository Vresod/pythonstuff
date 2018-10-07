# -----------------------------------
import datetime
# -----------------------------------
year = int(input('What year are we testing for?: '))
# -----------------------------------
wasisbase = datetime.datetime.now().year
if year < wasisbase:
	wasis = 'was'
elif year == wasisbase:
	wasis = 'is'
else:
	wasis = 'will be'
# -----------------------------------
if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print(year,wasis,'a leap year.')
		else:
			print(year,wasis,'not a leap year.')
	else:
		print(year,wasis,'a leap year.')
else:
	print(year,wasis,'not a leap year.')