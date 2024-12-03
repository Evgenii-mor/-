number1=(int(input(" Введите  число  ")))
number2=(int(input("Введите  число ")))
number3=(int(input("Введите  число ")))
if number1 == number2 and number2== number3:
    print(3)
if number1== number2 or number2== number3:
    print(2)
if not number1== number2 and not number2==number3:
    print(0)
