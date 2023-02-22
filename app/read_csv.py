import csv

def read_csv(path): #path es la ubicación del archivo
  with open(path, 'r') as csvfile: #donde está el path y r es permiso solo de lectura csvfile es el archivo que se quiere abrir
    reader = csv.reader(csvfile, delimiter=',') #csv.reader se crea un lector del archivo... se utiliza el módulo importado csv y se envía el archivo (csvfile) con un delimitador
     #La coma se usa como delimitador porque así se está separando en el archivo...Otros podrían estar separados por ; u otro símbolo.
    header = next(reader) #Esto es para obtener la primera fila de forma manual...Si se hace un print(header) y nos muestra solo los nombres de los datos...como si fuera el nombre de todas las columnas...
    data = [] #Se necesita retornar una lista con todos los diccionarios... por esto se llama un data = []
    for row in reader: #para iterar en cada fila, leer fila a fila
      iterable = zip(header, row) #el zip va a ser la unión del header con el row...lo une en un arrive de tuplas en donde la primer posición será de columnas y la segunda de row. Es posible pasar al formato de lista con print(list(iterable))
      country_dict = {key: value for key, value in iterable} #Aquí se genera un diccionario value in iterable es para que se vaya a iterable y  saque el segundo valor de ahí... value for key es el head ... se sacan clave valor...
      data.append(country_dict) #se agrega por cada interacción de country_dict
    return data

if __name__ == '__main__': #Para ejecutar este archivo con un script desde la terminal (shell)
  data = read_csv('data.csv') #Esto es para leer el csv... por esto se le da la ruta.
  print(data[0])
'''
import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])


  Reto clase 38

  Para resolver este desafío, debes utilizar el archivo data.csv que contiene los datos de los gastos de una empresa. El archivo tiene dos columnas: el nombre del área y el total de gastos del año.

Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa. Para leer el archivo CSV, puedes utilizar la función open y el módulo csv de Python. Una vez que hayas leído los datos, puedes calcular el total de gastos implementando la lógica que consideres necesaria.

Ejemplo

Input: data.csv
Administration,10
Marketing,20
Purchasing,10
Human Resources,20

Output:
60

Solución:

data.csv

Administration,200
Marketing,201
Purchasing,114
Human Resources,203
Shipping,121
IT,103
Public Relations,204
Sales,145
Executive,100
Finance,108

main.py

import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path, "r") as csvfile:
      total = sum(int(s[1]) for s in csv.reader(csvfile))
   
   return total

response = read_csv('./data.csv')
print(response)

  '''
