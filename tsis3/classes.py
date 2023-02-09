class some_str:
        getString = input()
        printString = getString.upper()

to_upper = some_str()
print(to_upper.printString)

#2222222222222

class Shape:
    class Square:
        def __init__(self, length):
            self.AREA = length ** 2
        def area(self, num = 0):
            print("area =", num)

    def area(self, num = 0):
            print("area =", num)

length = int(input())
fig = Shape.Square(length)
fig.area(fig.AREA)

#333333333333

class Shape:
    class Square:
        def __init__(self, length):
            self.AREA = length ** 2
        def area(self, num = 0):
            print("area =", num)

    def area(self, num = 0):
            print("area =", num)

class Rectangle(Shape):
    def init(self, length, width):
        self.AREA = length * width
        self.area(self.AREA)


length, width = input().split()
length = int(length)
width = int(width)

rec = Rectangle()
rec.init(length, width)


#444444444444444444
class Points:
    def __init__(self, px = 0, py = 0):
        self.x = px
        self.y = py
    def show(self):
        print(self.x, self.y)

    def move(self, dx = 0, dy = 0):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = dx**2 + dy**2
        distance = distance ** 0.5
        print(distance)

x1, y1 = input().split()
x2, y2 = input().split()
x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)

point1 = Points(x1, y1)
point2 = Points(x2, y2)

point1.show()
point2.show()

point1.move(1, 1)
point2.move(2, 2)

point1.show()
point2.show()

point1.dist(point2)




#5555555555555555
class Account:
    owner = "NULL"
    balance = 0
    def __init__(self, name):
        owner = name

    def deposit(self, num = 0):
        if num >= 0:
            self.balance += num
            print("Getting richer:", num)

        else:
            print("Ain't that good hacker")

    def withdraw(self, num = 0):
        if num >= 0:
            if num <= self.balance:
                self.balance -= num
                print("Withdrawal:", num)

            else:
                print("you're too poor for that")

        else:
            print("Dummy?")


Person1 = Account("Person1")
Person2 = Account("Person2")

running = True
while running:
    command, *num = input().split()

    if len(num) != 0:
        num = int(num[0])

    if command == "Withdraw":
        Person1.withdraw(num)

    elif command == "Add":
        Person1.deposit(num)

    elif command == "End":
        running = False

    else:
        print("Denied")


#66666666666666
some = [1, 5, 6, 9, 65562, 9, 65, 6, 5, 3, 2, 7, 11, 13, 8]
filtered = []


def filter(num):
    i = 2
    while i <= num**0.5:
        if num % i == 0:
            return False
        i += 1
    return True

for num in some:
    if filter(num) == True:
        filtered.append(num)

print(filtered)