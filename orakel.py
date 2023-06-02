import random 
import time

full=["⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"*2,"0"]
broken=["⬛⬛⬛⬛⬛⬛⬛⬛⬛        "*2,"1"]

cache=""

print("\n")
for i in range(6):
    choice=random.choice([full,broken])
    for i in choice[0]:
        print(i, end="",flush=True)
        if i!=" ":
            time.sleep(0.025)
    print('\n')
    cache+=choice[1]
    
print(cache)