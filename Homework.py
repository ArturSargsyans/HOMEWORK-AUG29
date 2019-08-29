def GettingTheNumber():
    while True:
        numberofintegers = input("Please enter how many integers you want to have in the list")
        if numberofintegers.isdigit():
            break
        else:
            print("INSERT A NUMBER!")
    return int(numberofintegers)

def MakingTheList(numberofintegers):
    list = []
    previousnumber=0
    for integer in range(numberofintegers):
        while True:
            integer = input("the number")
            if integer.isdigit():
                break
            else:
                print("INSERT A NUMBER!")
        integer = int(integer)
        integer = integer + previousnumber
        previousnumber = integer
        list.append(integer)

    print(list)

def main():
    number = GettingTheNumber()
    MakingTheList(number)

main()