import csv
from datetime import date




#File config
weight_file = 'C:/Users/Karol\Desktop/tracker/data/weight.csv'


def write_to_csv(filename, row):
    f = open(filename, 'a', newline='')
    writer = csv.writer(f)
    #writer.writerow(['Imie', 'Data', 'Waga'])
    writer.writerows(row)
    f.close()

def ask_for_user_input():
    print("Hello, i'm your life tracker. Who are you?")
    name = input("My name is: ")
    print(f'Siema {name}, ile ważysz?')
    new_weight = input()
    today = date.today()
    print(f'Rozumiem że waga jest dla dnia: {today} (TAK/NIE)?')    
    if(input()=="TAK"):
        new_entry = [name, today, new_weight]
        write_to_csv(weight_file, [new_entry])


ask_for_user_input()


