for item in "Python":
    print(item)

# defined by squre brackets

for item in ['John', 'Jane', 'Ken', 'Faith', 'Serah']:
    print(item)

for item in range(10):
    print(item)

#write a program to find the largest number in a list

numbers = [3, 6, 7, 30, 8, 9, 5]

max = numbers[0]
for number in numbers:
    if number > max:
        max =number
print(max)