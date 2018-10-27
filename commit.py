import os
import time
# -----------------------------------
os.system('git add -A')
comname = str(input('What is the commit name?: '))
# -----------------------------------
os.system('git commit -m \"' + comname + '\"')
os.system('git push')
os.system('cls')