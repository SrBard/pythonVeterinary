import csv

from sqlalchemy import false, true



def read_file(file:str)->list:
    
    list= []

    try:
        with open(file,'r',encoding='UTF-8') as fh:
            csv_reader = csv.reader(fh)
            for row in csv_reader:
                list.append(row)
    except IOError:
        print(f"No se pudo leer el archivo {file}")
   
    return list

def verify_password_user(password:str,user:str)->bool:
    list = read_file("Users.csv")
    flag = false
    for row in list:
        if  password == row[3] and user == row[2]:
            flag=true

    return flag
             
    
    
