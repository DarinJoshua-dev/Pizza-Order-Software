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
    tot=0
    want_to_order=input('do you want to order?, answer in yes or no')
    if(want_to_order=='yes'):
        num=eval(input("How many pizzas do u want?"))
        tot=tot+num
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
        print("total no of pizzas ordered",tot)           
    else:
        exit(0)
