
dict=[]
def Load():
    print("Loading...")
    f=open('translate.txt', 'r')
    words=f.read().split('\n')
    for i in range(0,len(words),2):
        dict.append({'English':words[i].lower(),'Persian':words[i+1].lower()})
    f.close()
    print("Welcome!")

def show_menu():
    print('1_ Add a new word')
    print('2_ Translate English to Persian')
    print('3_ Translate Persian to English')
    print('4_ Exit')

def Add_New_Word():
    while True:
        English=input("Please enter new word in English: ")
        Persian=input("Please enter new word in Persian: ")
        dict.append({'English':English.lower(), 'Persian':Persian.lower()})
        print('New word added successfully!')
        A=input("Do you want to add another word?[Yes/No]")
        if A=='No' or A=='no' or A=='n' or A=='N':
            break

def English2Persian():

    user_input=input("English: ").split(' ')

    for i in range(len(dict)):
        for j in range(len(user_input)):
            if user_input[j]==dict[i]['English']:
                print(dict[i]['Persian'], end=' ')
    print('\n')

        
def Persian2English():
    user_input=input("Persian: ").split(' ')
    for i in range(len(dict)):
        for j in range(len(user_input)):
            if user_input[j]==dict[i]['Persian']:
                print(dict[i]['English'], end=' ')
    print('\n')

def Save_and_exit():
    f=open('translate.txt','w')
    for i in range(len(dict)):
        new=(dict[i]['English'] + '\n' + dict[i]['Persian']+ '\n')
        f.write(new)
    f.close()
    exit()

Load()

while True:
    show_menu()
    choice=int(input("Please select an option: "))
    if choice==1:
        Add_New_Word()

    elif choice==2:
        English2Persian()

    elif choice==3:
        Persian2English()

    elif choice==4:
        Save_and_exit()
