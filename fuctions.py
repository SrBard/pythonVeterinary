import csv


def read_file(file:str)->list:
    '''Lee un archivo CSV y regresa una lista de registros
    '''
    list= []

    try:
        with open(file,'r',encoding='UTF-8') as fh:
            csv_reader = csv.reader(fh)
            for row in csv_reader:
                list.append(row)
    except IOError:
        print(f"No se pudo leer el archivo {row}")
   
    return lista
