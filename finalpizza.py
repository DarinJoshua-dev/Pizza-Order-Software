import itertools
total1=0
ob1=0
ob2=0
ob3=0
ob4=0
ob5=0
ob6=0
def confirm(co):                                                   
    small=0
    large=0
    medium=0
    thin=0
    thick=0
    size=0
    topping=[]
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    num=0
    base=0
    counter=0
    i=1
    global total1
    global ob1,ob2,ob3,ob4,ob5,ob6
    total=0
    want_to_order=input('Do you want to order?, answer in yes or no: ')
    if(want_to_order=='yes'):
        num=eval(input("How many pizzas do you want? "))
        total=total+num
        while(i<=num):
            print("Enter",i,"order" )
            size=input('Choose the size of your pizza:small or medium or large: ')
            if ((size=='small')or(size=='large')or(size=='medium')):
                base=input('Choose the size of your pizza base:thin or thick:')
                if ((base=='thin')or(base=='thick')):
                    print("Choose three toppings for the pizza:")           
                    for counter in range (1,4):
                        toppings=input('Choose any 1 toppings from :pepperoni ,chicken ,extra cheese ,mushrooms ,spinach ,olives: ')
                        topping.append(toppings)
                        if(toppings=='pepperoni'):
                            count1=count1+1
                        if(toppings=='chicken'):
                            count2=count2+1
                        if(toppings=='extra cheese'):
                            count3=count3+1
                        if(toppings=='mushrooms'):
                            count4=count4+1
                        if(toppings=='spinach'):
                            count5=count5+1
                        if(toppings=='olives'):
                            count6=count6+1
            print("Size is", size, ',' ,"Base is", base ,',',"Toppings are", topping)
            topping=[]
            i+=1
        print("Total no of pizzas ordered by the present customer",total)
        total1=total+total1
        ob1=ob1+count1
        ob2=ob2+count2
        ob3=ob3+count3
        ob4=ob4+count4
        ob5=ob5+count5
        ob6=ob6+count6
    else:
        print("The total number of pizzas ordered by all the customers upto current status for the day=",total1)
        exit(1)
j=0
k=1
star=input("Type (enter/exit) to start GemPizza software: ")
if(star=="exit"):
    tot=0
    print("The total number of pizzas ordered by all the customers in the day is=",tot)
    quit(1)
for j in itertools.repeat(1):
    if(star=="enter"):
        co=input("Do you want to confirm your present or next customer?(yes/no): ")
        if(co=="yes"):
            user=input("Enter the customer name: ")
            print("CUSTOMER SERVICE",k)
            k=k+1
            confirm(co)
            lists=[ob1,ob2,ob3,ob4,ob5,ob6]
            full=(ob1+ob2+ob3+ob4+ob5+ob6)
            if(ob1>=max(lists)):
                print("The most popular Topping is pepperoni in  percentage = ")
                print(abs((max(lists)/full)*100),"%")
            elif(ob1<=min(lists)):
                print("The least popular Topping  is pepperoni in percentage = ")
                print(abs((min(lists)/full)*100),"%")
            if(ob2>=max(lists)):
                print("The most popular Topping is chicken in  percentage = ")
                print(abs((max(lists)/full)*100),"%")
            elif(ob2<=min(lists)):
                print("The least popular Topping is chicken in percentage = ")
                print(abs((min(lists)/full)*100),"%")
            if(ob3>=max(lists)):
                print("The most popular Topping is extra cheese in  percentage = ")
                print(abs((max(lists)/full)*100),"%")
            elif(ob3<=min(lists)):
                print("The least popular Topping is extra cheese in percentage = ")
                print(abs((min(lists)/full)*100),"%")
            if(ob4>=max(lists)):
                print("The most popular Topping is mushrooms in  percentage = ")
                print(abs((max(lists)/full)*100),"%")
            elif(ob4<=min(lists)):
                print("The least popular Topping  is mushrooms in percentage = ")
                print(abs((min(lists)/full)*100),"%")
            if(ob5>=max(lists)):
                print("The most popular Topping is spinach in  percentage = ")
                print(abs((max(lists)/full)*100),"%")
            elif(ob5<=min(lists)):
                print("The least popular Topping is spinach in percentage = ")
                print(abs((min(lists)/full)*100),"%")
            if(ob6>=max(lists)):
                print("The most popular Topping is olives in  percentage = ")
                print(abs((max(lists)/full)*100),"%")
            elif(ob6<=min(lists)):
                print("The least popular Topping is olives in percentage = ")
                print(abs((min(lists)/full)*100),"%") 
            print("The total number of pizzas ordered by all the customers upto current status=",total1)
        if(co=='no'):
             print("The total number of pizzas ordered by all the customers in the day is=",total1)
             quit(1)


       
    

