print("welcome to roller coster ride")
height=int(input("please enter your height in m"))


if height >=120:
    print("you can ride the rollercoster ride")
    age = int(input("enter your age:"))
    if age <=12:
        print("You can ride the rollercoster ride by paying 50 Rs")
    elif age <= 18:
        print("You can ride the rollercoster ride by paying 100 Rs")
    elif age<=22:
        print("You can ride the rollercoster ride by paying 120 Rs")
    else:
        print("you can ride rollercoster ride by paying 150Rs")


else:
     print("you cannot ride the rollercoster ride you need to grow taller")

