import os
# -----------------------------------
os.system('git add -A')
comname = str(input('What is the commit name?: '))
# -----------------------------------
cmdrun = str('git commit -m' + comname)
os.system(cmdrun)