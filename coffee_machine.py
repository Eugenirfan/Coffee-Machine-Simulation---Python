MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins= {
    "pennies":.01,
    "nickels":.05,
    "dimes":.10,
    "quarters":.25,
    }
import sys
def register(choice):
    tender=0
    for i in coins:
        nos=int(input("How many "+i+" do you have: "))
        value=coins[i]*nos
        tender+=value
    if tender<(MENU[choice]['cost']):
        print("Not enough money, try again")
        sys.exit()
    else:    
        balance= tender-(MENU[choice]['cost'])
    
        return balance
    
current_water=500
current_milk=300
current_coffee=300

def resources(choice):
    global current_water,current_milk,current_coffee
    if choice in MENU:
        process_water=(MENU[choice]['ingredients']['water'])
        if current_water<process_water:
            print("water is low at"+str(current_water)+" ml")
            sys.exit()
        else:
            current_water-=process_water
        try:
            process_milk=(MENU[choice]['ingredients']['milk'])
            if current_milk<process_milk:
                print("Milk is low at"+str(current_milk)+" ml")
                sys.exit()
            else:
                current_milk-=process_milk
        except KeyError:
            remaining_milk=current_milk
        process_coffee=(MENU[choice]['ingredients']['coffee'])
        if current_coffee<process_coffee:
            print("Coffee is low at"+str(current_coffee)+" ml")
            sys.exit()
        else:
            current_coffee-=process_coffee
        return current_water,current_milk,current_coffee


def main():
   
    
    balance=0  
    choice=input("What would you like to have? (espresso, latte, cappuccino):\n ").lower()
    if choice=="report":
        print (str(current_water)+"ml Water",str(current_milk)+"ml Milk",str(current_coffee)+"ml Coffee")
        main()
        
    else:
        resources(choice)
        balance=register(choice)
        if balance<0:
            print("Not enough Money, Try Again")
        print("Thank you. Here is your "+str(choice)+" and your balance "+str(balance))
        main()
        
           
main()
    
    
    
        
