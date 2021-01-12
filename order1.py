def u1(us1):
    small=0
    large=0
    medium=0
    thin=0
    thick=0
    size=0
    topping=[]
    item=[]
    num=0
    base=0
    counter=0
    i=1
    tot1=0
    want_to_order=input('Do you want to order?, answer in yes or no')
    if(want_to_order=='yes'):
        num=eval(input("How many pizzas do you want?"))
        tot1=tot1+num
        while(i<=num):
            print("enter",i,"order" )
            size=input('choose the size of your pizza:small or medium or large')
            if ((size=='small')or(size=='large')or(size=='medium')):
                base=input('choose the size of your pizza base:thin or thick')
                if ((base=='thin')or(base=='thick')):
                    print("Choose three toppings for the pizza:")           
                    for counter in range (1,4):
                        toppings=input('choose any 1 toppings from :pepperoni ,chicken ,extra cheese ,mushrooms ,spinach ,olives ')
                        topping.append(toppings)
            print(size, ',' ,base ,',', topping)
            topping=[]
            i+=1
        print("total no of pizzas ordered",tot1)
    else:
        exit(1)
def u2(us2):
    small=0
    large=0
    medium=0
    thin=0
    thick=0
    size=0
    topping=[]
    item=[]
    num=0
    base=0
    counter=0
    i=1
    tot2=0
    want_to_order=input('Do you want to order?, answer in yes or no')
    if(want_to_order=='yes'):
        num=eval(input("How many pizzas do u want?"))
        tot2=tot2+num
        while(i<=num):
            print("enter",i,"order" )
            size=input('choose the size of your pizza:small or medium or large')
            if ((size=='small')or(size=='large')or(size=='medium')):
                base=input('choose the size of your pizza base:thin or thick')
                if ((base=='thin')or(base=='thick')):
                    print("Choose three toppings for the pizza:")           
                    for counter in range (1,4):
                        toppings=input('choose any 1 toppings from :pepperoni ,chicken ,extra cheese ,mushrooms ,spinach ,olives ')
                        topping.append(toppings)
            print(size, ',' ,base ,',', topping)
            topping=[]
            i+=1
        print("total no of pizzas ordered",tot2)
    else:
        exit(1)
def u3(us3):
    small=0
    large=0
    medium=0
    thin=0
    thick=0
    size=0
    topping=[]
    item=[]
    num=0
    base=0
    counter=0
    i=1
    tot3=0
    want_to_order=input('Do you want to order?, answer in yes or no')
    if(want_to_order=='yes'):
        num=eval(input("How many pizzas do u want?"))
        tot3=tot3+num
        while(i<=num):
            print("enter",i,"order" )
            size=input('choose the size of your pizza:small or medium or large')
            if ((size=='small')or(size=='large')or(size=='medium')):
                base=input('choose the size of your pizza base:thin or thick')
                if ((base=='thin')or(base=='thick')):
                    print("Choose three toppings for the pizza:")           
                    for counter in range (1,4):
                        toppings=input('choose any 1 toppings from :pepperoni ,chicken ,extra cheese ,mushrooms ,spinach ,olives ')
                        topping.append(toppings)
            print(size, ',' ,base ,',', topping)
            topping=[]
            i+=1
        print("total no of pizzas ordered",tot3)
    else:
        exit(1)
def confirm(co):
    if(co=="yes"):
        print("NEXT CUSTOMER")
    else:
        exit(1)
us1=input("enter user 1 name:")
print(u1(us1))
co=input("Do want to move to next customer(yes/no):")
confirm(co)
us2=input("enter user 2 name:")
print(u2(us2))
co=input("Do want to move to next customer(yes/no):")
confirm(co)
us3=input("enter user 3 name:")
print(u3(us3))

