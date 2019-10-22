# Librería de sistema cuántico de partícula en una línea

Es una librería la cual realiza la simulacion de unba partícula confinada a un conjunto discreto de posiciones en una línea. El simulador permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

# Como instalar la libreria  

Que cosas necesitas para instalar el software y como instalarlas 

Las cosas más básicas para poder usar la librería es tener Python 3.7 instalado en tu ordenador, para poder implementar la librería solo necesita crear una carpeta, guardar la librería con el nombre “ lisbre_uni3.py ”, en el programa que quieras usar la librería tienes que poner “ import lisbre_uni3”. 
 ```python
 import lib2
 ```

# Ejecución de librería 

En este caso la libreria coje matrices con numeros reales, como  con numeros complejos, en este caso el mismo programa reconoce el tipo de dato ingresado, prar que pueda leer los complejos lo mete en una tupla, y dependiendo de lo que este corriedno tiene que ingresar el numero de clicks, la matriz y el vector de clicks 
 ```python
 #Reales
  def test_proba(self):
        lis=[[(-3,-1)],
             [(0,-2)],
             [(0,1)],
             [(2,0)]]
        a=3
        c=0.0526
 ```

Las funciones que vamos a encontrar se encuentra: 

-  El sistema debe calcular la probabilidad de encontrarlo en una posición en particular
- El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.


# Pruebas
En estas podremos ver el tipo de entrada que recibe,y las diferentes salidas que puede votar:
```python
import unittest
import lib2

class MyTestCase(unittest.TestCase):
    #1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
    def test_proba(self):
        lis=[[(-3,-1)],
             [(0,-2)],
             [(0,1)],
             [(2,0)]]
        a=3
        c=0.0526
        self.assertEqual(lib2.proba(lis,a), c)
    #2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
    def test_transi(self):
        lista1=[[(1,0)],[(0,-1)]]
        lista2=[[(0,1)],[(1,0)]]
        lis1=(((2)**(1/2)/2),lista1)
        lis2=(((2)**(1/2)/2),lista2)
        c=-1.0
        self.assertEqual(lib2.transi(lis1,lis2), c)

        
if __name__ == '__main__':
    unittest.main()

```
# Hecho por:
- Juan Sebastian Cadavid P
- Ingeniero de Sistemas
- Escuela Colombiana de Ingeniería Julio Garavito
