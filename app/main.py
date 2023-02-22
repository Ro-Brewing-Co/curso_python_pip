import utils
import read_csv
import charts
import pandas as pd

def run():

      

  data = read_csv.read_csv("data.csv")    
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()




'''

Si solo se importa un módulo, y se intenta imprimir una variable y se ejecuta todo el módulo... se mete la variable o el conjunto en una función y se controla import main   print(main.data)... ya se puede ejecutar el print sin ejecutar todo el módulo. Luego, si se desea ejecutar el módulo, llama a la función en ña que metió las operaciones... main.run()



Se quiere ejecutar main.py como script sin necesidad de un tercer archivo, pero no es posible ...example.py controla la ejecución de main.py, si quiero tener la dualidad que quiere decir que se pueda ejecutar main.py en shell o terminal... se pone if __name__=="__main__" run() y así es posible ejecutarse desde la terminal el método de run(), pero si es ejecutado desde otro archivo, run() no se va a ejecutar........Desde example.py se ejecuta normal... si se llama desde main.py el run(), se ejecuta por el if... no se ejecutaría si no tuvierra el   if.


import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv("./app/app/data.csv") #por acá se obtiene la data del archivo .csv Sería e lnombre del módulo.función del módulo read_csv.read_csv(dirección del módulo con la data o ubicación del archivo)
  country = input("Type country => ") #Esto es para selecciónar o introducir el país

  result = utils.population_by_country(data, country) # Aquí aparece el resultado, que es dado por la función population_by_country que se encuentra en el módulo utils por eso utils.population_by_country(data, country)

  if len(result > 0): #debe ser mayor a cero 
    country = result[0] #el  = a result en la posición cero, que fue el que encontró y se enía a get_population que se encuentra en utils.py
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values) #Este es para generar una gráfica


  print(result)


if __name__ == "__main__":
  run()


def run():
  keys, values =   utils.get_population()
  print(keys, values)
  
  data = [
    {
      "country": "Colombia",
      "Population": 500
    },
    {
      "country": "Bolivia",
      "Population":   300
    }
  ]
  
  country = input("Type country => ")
  
  result = utils.population_by_country(data, country)
  print(result)

  #Sin el siguinete if, no es posible correr el run  desde este módulo main.py, este es un script

if __name__ == "__main__":
  run()

#El anterior if __name__ == "__name__": dice que corre run() si es ejecutado desde la terminal, de lo contrario no se ejecuta 

#El profesor dice que el archivo se puede correr desde otro módulo, como por ejemplo, desde el example.py... si se quiere correr desde main.py, se debe poner el if __name...

#Sin este if, se perdería la oportunidad de que se pueda correr como un script, es decir, directamente desde main.py





'''