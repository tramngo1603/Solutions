def collatz(number):
    if number <= 1:
        return number
    print(number)
    if int(number % 2) == 0:
        return collatz(int(number // 2))
    else:
        return collatz(3*int(number) +1)

number = int(input('Enter number:'))
print(collatz(number))
