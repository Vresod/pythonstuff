import os

cpus = os.cpu_count()

if cpus == 1:
	print('You have',cpus,'CPU.')
else:
	print('You have',cpus,'CPUS.')