import random

class bcolors:   
    GREEN = '\033[92m'  
    RED = '\033[91m'
    ENDC = '\033[0m'

options = ["Left", "Right"]

for i in range(100):
    result = random.choice(options)

    if result == "Left":
        print(bcolors.GREEN + "Left" + bcolors.ENDC)
    else:
        print(bcolors.RED + "Right" + bcolors.ENDC)


# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'