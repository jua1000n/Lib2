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
