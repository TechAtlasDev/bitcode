from matplotlib import pyplot as plt

class Graph:
  def __init__(self, x="X", y="Y", title="Grafico"):
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.grid(True)
  
  def graficar_secuencia_puntos(self, secuencia_puntos:list[float], y=None):
    y = range(len(secuencia_puntos)) if y is None else y
    plt.plot(y, secuencia_puntos, marker='o', linestyle='-')
    plt.show()