# 1- What is the first output?

for i in range(10):
    if (i + 1) % 2 == 0:
        print("even")
    else:
        print("odd")

# ans: "odd"

# ----------------------------------------------------------

# 2- What is the output?

d = {0: 'a', 1: 'b', 2: 'c'}
for i in d:
    print(i)

# ans: 0   1   2

# ----------------------------------------------------------


t = (1, 2, 3)
print(len(t))

# ans: 3


# ----------------------------------------------------------


def add(a, b, c):
    return str(a) + str(b) + str(c)


print(add(1, 2, 3))

# ans: 123


# ----------------------------------------------------------


i = 1
while 1 < 3:
    print("good")
    break

# ans: good

# ----------------------------------------------------------

List = [1, 2, 3, 4]
List.append(5)
print(List)

# ans: [1, 2, 3, 4, 5]

# ----------------------------------------------------------

list1 = [1, 2, 3, 4]
list2 = []

for i in list1:
    list2.append(i)

list1.append(5)
print(list2)

# ans: [1, 2, 3, 4]

# ----------------------------------------------------------


# What is the data type of this object Var=(2)?

Var = 2
print(type(Var))

# ans: int


# ----------------------------------------------------------


def convert(a, b, c):
    return len(a) + len(b) + c


print(convert({2, 3, 49}, (2, 555, 1, 5, 7), 5000))
# ans: 3 + 5 + 5000 =5008
