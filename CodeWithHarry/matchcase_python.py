week_number = int(input("Enter the week number: "))

# match case is used to compare the value of week_number with the cases

match week_number:
    case 1:
        print("Monday")  # using break is not necessary in match case
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _ if week_number > 7:
        print("Invalid Input")  # default case
    case _ if week_number == 0:
        print("It's 0th day")
