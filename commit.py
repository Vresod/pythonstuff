import os
import time
# -----------------------------------
os.system('git add -A')
comname = str(input('What is the commit name?: '))
# -----------------------------------
cmdrun = str('git commit -m' + comname)
os.system(cmdrun)
os.system('git push')
os.system('cls')
os.system('git log')
time.sleep(5)
os.system('q')
