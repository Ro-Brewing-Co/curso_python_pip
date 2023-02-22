'''
def get_population():
  keys = ["Col", "bol"]
  values = [300, 400]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item["country"] == country, data))
  return result

'''



# Cualquier archivo que termine en .py se puede consderar un módulo y será posible llamarlos desde otro módulo con el import... por ejemplo, import mod en otro 


# Country_dict es el país que selecccionamos 

def get_population(country_dict):
  population_dict = {
    "2022": int(country_dict["2022 Population"]),
    "2020": int(country_dict["2020 Population"]),
    "2015": int(country_dict["2015 Population"]),
    "2010": int(country_dict["2010 Population"]),
    "2000": int(country_dict["2000 Population"]),
    "1990": int(country_dict["1990 Population"]),
    "1980": int(country_dict["1980 Population"]),
    "1970": int(country_dict["1970 Population"])
  }

  labels = population_dict.keys() #Aquí se pide un array de los valores de os años...
  values = population_dict.values() #Aquí los valores relacion ados con la polación por año de determinado país...
  return labels, values

  #El return debe ser un arrive con los los valores, con la población en los años...

def population_by_country(data, country):
  result = list(filter(lambda item: item["Country/Territory"] == country, data))
  return result
      
  