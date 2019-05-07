import time,sys

print(" __  __ _______   _________       _____  ______ ")
print("|  \/  |_   _\ \ / /__   __|/\   |  __ \|  ____|")
print("| \  / | | |  \ V /   | |  /  \  | |__) | |__   ")
print("| |\/| | | |   > <    | | / /\ \ |  ___/|  __|  ")
print("| |  | |_| |_ / . \   | |/ ____ \| |    | |____ ")
print("|_|  |_|_____/_/ \_\  |_/_/    \_\_|    |______|")
print("//version 1.0.0 - developed by darrenwhy")

yes = "powering on..."

no = "powering off..."

print(" ")
print("launch? - options: yes // no")
answer = input("answer: ")

if answer == "yes":
    print(" ")
    print(yes)
    print(" ")
for i in range(100+1):
    time.sleep(0.1)
    sys.stdout.write(('█'*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
    sys.stdout.flush()

# fix the code below, syntax error with the elif

elif answer == "no"
    print(no)
    sys.exit(0)
else:
    print("please enter yes or no")
