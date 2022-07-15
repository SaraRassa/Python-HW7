
from pyfiglet import Figlet

def show_menu():
    print('1_ Add product')
    print('2_ Edit product')
    print('3_ Delete product')
    print('4_ Search')
    print('5- Show list')
    print('6_ Buy')
    print('7_ Exit') 

def show_list():
    for i in range(len(products)):
        print(products[i]['id'],'\t',products[i]['name'],'\t',products[i]['price'],'\t',products[i]['count'],'\t')

products=[]

def load():
    print("Loading...")
    f= open('database.txt','r')
    rows=f.read().split('\n')
    for i in range(len(rows)):
        info=rows[i].split(',')
        products.append({'id':int(info[0]),'name':info[1],'price':float(info[2]),'count':int(info[3])})
    f.close()
    print("Welcome!!")

def add_product():
    id=int(input("Please enter id: "))
    name=input('Please enter name: ')
    price=float(input("Please enter price: "))
    count=int(input("Please enter count: "))
    products.append({'id':id, 'name':name, 'price':price, 'count':count})
    print("New product added successfully")

def show_edit_menu():
    print('1_ name')
    print('2_ price')
    print('3_ count')
    print('4_ end editing')

def edit_product():
    id=int(input("Please enter product id: "))
    for i in range(len(products)):
        if products[i]['id']==id:
            while True:
                show_edit_menu()
                choice=int(input("Please choose an option: "))
                if choice==1:
                    products[i]['name']=input("Please enter new name: ")
                elif choice==2:
                    products[i]['price']=float(input("Please enter new price: "))
                elif choice==3:
                    products[i]['count']=int(input("Please enter new count: "))
                elif choice==4:
                    break
                else:
                    print("Make sure you enter right number!!!")
    
def delete_product():
    id=int(input("Enter product id: "))
    for i in range(len(products)):
        if products[i]['id']==id:
            products.pop(i)
            print("Product removed!")
            break

def search_product():
        user_keyword=input("Please enter product name or id: ")
        for i in range(len(products)):
            if products[i]['name']==user_keyword or str(products[i]['id'])==user_keyword:
                print(products[i])
                break
        else:
            print("Not found!!")

def buy_product():
    basket=[]
    while True:
        id=int(input("Enter product id: "))
        for i in range(len(products)):
            if products[i]['id']==id:
                count=int(input("Enter count: "))
                if products[i]['count'] >= count:
                    basket.append({'name':products[i]['name'],
                                   'price':products[i]['price'], 
                                   'count':count}) 
                
                    products[i]['count'] -= count
                    print("Product added to basket successfully!")

                else:
                    print('This amount is not available!')

        choice=input("Do you want to continue? [yes/no] ")
        if choice=='n' or choice=='N':
            break
    print(basket)
    Total_price=0
    for i in range(len(basket)):
       Total_price= basket[i]['price'] * basket[i]['count'] + Total_price
    print("Total price= ", Total_price)
    print("Thank you for shopping")

def save_and_exit():
    f= open('database.txt','w')
    for i in range(len(products)):
        row = (str(products[i]['id']) + ',' + products[i]['name']+','+ str(products[i]['price']) +','+ str(products[i]['count'])+ '\n')
        f.write(row)
    f.close()
    exit()

load()
f = Figlet(font='standard')
print (f.renderText('Sara Store'))


while True:
    show_menu()
    choice=int(input("Select and option: "))

    if choice==1:
        add_product()

    elif choice==2:
        edit_product()

    elif choice==3:
        delete_product()
        
    elif choice==4:
        search_product()

    elif choice==5:
        show_list()

    elif choice==6:
        buy_product()

    elif choice==7:
        save_and_exit()
