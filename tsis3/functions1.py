#1 A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def Gram_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
grams=2
print(Gram_to_ounces(grams))

#2 Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion:
def FarengeitToCelcius(F):
    C = (5 / 9) * (F - 32)
    return C
farengeit=20
print(FarengeitToCelcius(farengeit))

#3 Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? 
def solve(heads, legs):
    error="error"

    if heads>legs:
        print(error)
    elif legs%2!=0:
        print(error)
    else:
        num_rabbit=(legs-heads*2)/2
        num_chicken=(heads-num_rabbit)
        print(num_rabbit, num_chicken)
solve(35, 94)

#4 You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def filter_prime(num):
    prime = []
    a = 2
    for j in range(len(num)):
        if (num[j] == 1):
           pass
        elif (num[j] !=1 ): 
            while num[j] %a != 0:
                a+=1
            if (num[j] % 2 == 0 and num[j] !=2):
                pass
            elif (a == num[j]):
                prime.append(num[j])
    print(prime)

num = []
n = int(input())
for i in range (0 , n):
    number = int(input())
    num.append(number)
filter_prime(num)

    #5 Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations 

str = input()
perm = permutations(str)
for i in list(perm):
    for j in i:
        print(j, end = '')
    print("")

#6 Write a function that accepts string from user, return a sentence with the words reversed. 
slova=[]
slova=input().split()
for i in slova:
    print(slova[::-1])

#7 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
        
num = [3, 1, 3]
print(has_33(num))

#8
def spy_game(nums):
    new = [0, 0, 7]
    for i in nums:
        if len(new) == 0:
            return True
        if i == new[0]:
            new.pop(0)
    if len(new) == 0:
            return True
    else:
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#9
import math
def volume_counter(radius):
    print("Radius =", 4 / 3 * math.pi * radius ** 3) 
radius = float(input())
volume_counter(radius)

#10
def uniquer(list):
    new = []
    for i in range(len(list)):
        if len(new) == 0 or list[i] not in new:
            new.append(list[i])
    return new

ls = [1, 2, 3, 5, 6, 7, 8, 9, 11, 5, 6, 1, 1, 2, 3, 3, 3, 3, 4, 9]
print(uniquer(ls))

#11
def isPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

str = input()
print(isPalindrome(str))

#12
def histogram(list):
    for i in list:
        print("*"*i)

ls = [4, 9, 7]
histogram(ls)

#13
import random
r = random.randint(1, 20)

print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
guess = int(input())
count = 1

running = True
while running:
    if guess == r:
        print(f"Good job, {name}! You guessed my number in {count} guesses!")
        running = False
        continue
    elif guess < r:
        print("Your guess is too low.")
        print("Take a guess.")
        count += 1
    else:
        print("Your guess is too high.")
        print("Take a guess.")
        count += 1
    guess = int(input())

#14
def toGrams(num):
    print(num / 28.3495231)

def antiFar(num):
    print((num-32)*5/9)

def toCentimeter(num):
    print(num * 2.54)


print("Enter the number")
print("1)Convert ounces to gramms")
print("2)Convert Farenheit to Celcius")
print("3)Convert inches to centimeters")

mode = int(input())

if mode == 1:
    print("Enter the value")
    value = float(input())
    toGrams(value)
elif mode == 2: 
    print("Enter the value")
    value = float(input())
    antiFar(value)
elif mode == 3:
    print("Enter the value")
    value = float(input())
    toCentimeter(value)
else:
    print("An Error Occured")