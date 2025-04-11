#1. pwd
#2. ls
#3. cd ~/python_decal/judy_decal
#   git pull
#4. mv homework.py ~/personal_repo/homework/
#5. cat ~/personal_repo/homework/homework.py
#6. nano ~/personal_repo/homework/homeowrk.py
#7. git add homework.py
#   git commit -m "Completed HW5"
#   git push
#8. Judy's local repo is behind the remotre repo 
#   Fix:
#   git pull --rebase
#   git push
#9. cd ~/Recents/

#2.1
def checkDataType(x):
    returnt type(x).__name__

#2.2
def EvenOrOdd(n):
    return "Even" if n % 2 == 0 else "Odd"

#3
def SumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#4.1
def duplicateList(list):
    result = []
    for item in list:
        result.append(item)
        result.append(item)
    return result

#4.2
def square(num):
    return num * num
