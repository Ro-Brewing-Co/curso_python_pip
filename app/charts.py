import matplotlib.pyplot as plt  #Esta es una libreria que no está incorporado en python #Visualización de datos con python #En packages que está en Tools al lado izquierdo se busca el paquete nuevo y luego se instala

#se puede poner un alias a matplotlib.pyplot con as plt y así se puede llamar todo con plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values) #Esto es para las barras, que lavels sea eje x y values sea en eje y y que salgan barras
  plt.savefig(f"./imgs/{name}.png")#Para graficar y se grafica en output, se llama en python
  plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels) #Se debe indicar que son los labels, así funciona python labels=labels
    ax.axis("equal") #Equal para que sea en el centro 
    plt.savefig("pie.png")
    plt.close()


if __name__ == "__main__":  
  labels = ["a", "b", "c"]
  values = [10, 40, 800]
  generate_pie_chart(labels, values)
  generate_bar_chart(labels, values)





