#Coffee machine#

list = ["espresso", "latte", "cappuccino"]
# declaring global variable water ,milk ,coffee_beans #
water = 400
milk = 540
coffee_beans = 120
dispo_cup = 9
money = 550

# declaring remaining function #
def remaining():
    status()

# declaring status function #
def status():
    print("water " + str(water))
    print("milk " + str(milk))
    print("coffee_beans " + str(coffee_beans))
    print("dispo_cup " + str(dispo_cup))
    print("money " + str(money))

# declaring espresso coffee function #
def espresso():
    global money
    global water
    global coffee_beans
    global dispo_cup
    num_cof = int(input("How many cups of coffee do you want?"))
    wat_need = num_cof * 250
    cof_bean_need = num_cof * 16
    num_cup = num_cof * 1
    price = num_cof * 4
    if water >= wat_need and coffee_beans >= cof_bean_need and dispo_cup >= num_cup:
        money = money + price
        water = water - wat_need
        coffee_beans = coffee_beans - cof_bean_need

        dispo_cup = dispo_cup - num_cup
        print("I have enough resource, making you a coffee")
        print("you have to pay " + str(price)+"$") # this line#
    elif water <= wat_need and coffee_beans >= cof_bean_need and dispo_cup >= num_cup:
        print("sorry, not enough water!")
    elif water >= wat_need and coffee_beans <= cof_bean_need and dispo_cup >= num_cup:
        print("sorry, not enough coffee beans!")
    elif water >= wat_need and coffee_beans >= cof_bean_need and dispo_cup <= num_cup:
        print("sorry, not enough disposible cup!")

# declaring latte coffee function #
def latte():
    global money
    global water
    global coffee_beans
    global dispo_cup
    num_cof = int(input("How many cups of coffee do you want?"))
    wat_need = num_cof * 350
    cof_bean_need = num_cof * 20
    mil_need = num_cof * 75
    price = num_cof * 7
    num_cup = num_cof * 1
    if water >= wat_need and coffee_beans >= cof_bean_need and milk >= mil_need and dispo_cup >= num_cup:
        money += price
        water -= wat_need
        coffee_beans -= cof_bean_need

        dispo_cup = dispo_cup - num_cup
        print("I have enough resource, making you a coffee")
        print("you have to pay "+str(price)+"$")
    elif water <= wat_need and coffee_beans >= cof_bean_need and dispo_cup >= num_cup:
        print("sorry, not enough water!")
    elif water >= wat_need and coffee_beans <= cof_bean_need and dispo_cup >= num_cup:
        print("sorry, not enough coffee beans!")
    elif water >= wat_need and coffee_beans >= cof_bean_need and dispo_cup <= num_cup:
        print("sorry, not enough disposible cup!")

# declaring cappuccino coffee function #
def cappuccino():
    global money
    global water
    global coffee_beans
    global dispo_cup
    num_cof = int(input("How many cups of coffee do you want?"))
    wat_need = num_cof * 200
    cof_bean_need = num_cof * 12
    mil_need = num_cof * 100
    num_cup = num_cof * 1
    price = num_cof * 6
    if water >= wat_need and coffee_beans >= cof_bean_need and milk >= mil_need and dispo_cup >= num_cup:
        money = money + price
        water = water - wat_need
        coffee_beans = coffee_beans - cof_bean_need
        dispo_cup = dispo_cup - num_cup
        print("I have enough resource, making you a coffee")
        print("you have to pay "+str(price)+"$")
    elif water <= wat_need and coffee_beans >= cof_bean_need and dispo_cup >= num_cup:
        print("sorry, not enough water!")
    elif water >= wat_need and coffee_beans <= cof_bean_need and dispo_cup >= num_cup:
        print("sorry, not enough coffee beans!")
    elif water >= wat_need and coffee_beans >= cof_bean_need and dispo_cup <= num_cup:
        print("sorry, not enough disposible cup!")

def buy():
    print("1 - espresso", "2 - latte", "3 - cappuccino")
    cof_name = int(input("What you want from above coffee list ?"))
    if cof_name == 1:
        espresso()
    elif cof_name == 2:
        latte()
    elif cof_name == 3:
        cappuccino()
    else:
        print("Input is wrong")

def fill():
    num_add_wat = int(input("How much ml of water do you want to add?"))
    global water
    water += num_add_wat

    num_add_mil = int(input("How much ml of milk do you want to add?"))
    global milk
    milk += num_add_mil

    num_add_cof_beans = int(input("How much grams of coffee beans do you want to add "))
    global coffee_beans
    coffee_beans += num_add_cof_beans
    num_cup_of_fill = int(input("How much cup do you what to add ?"))
    global dispo_cup
    dispo_cup = num_cup_of_fill + dispo_cup


# i have to declera worker function which will help me to repeat the function again and again #
# giving option to user for buy, fill and take #
def main():
    list2 = ["buy", "fill", "take", "remaining", "exit"]
    print(list2)
    option = input("what you want to do from above thing ?")
    # for calling function exit #
    if option == "exit":
        quit()
    # creating function remaining #
    elif option == "remaining":
        remaining()
        main()
    # creating function buy for user #
    elif option == "buy":
        buy()
        main()
    # It is for worker #
    elif option == "fill":
        fill()
        main()
    elif option == "take":
        global money
        print("I gave you " + str(money))
        money -= money

        main()
        
main()
