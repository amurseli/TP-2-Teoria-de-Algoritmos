import unittest
from src.logic import coins_game 
import random

class TestCoinsGame(unittest.TestCase):

    def test_two_coins(self):
        arr = [1, 3]

        sophia_gain, mateo_gain, _ = coins_game(arr)
        self.assertEqual( sophia_gain , 3)  
        self.assertEqual( mateo_gain , 1)  

    def test_basic_case(self):
        arr = [1, 2, 3, 4, 5]
        sophia_gain, mateo_gain, _ = coins_game(arr)
        
        self.assertEqual( sophia_gain , 9)  
        self.assertEqual( mateo_gain , 6)  

    def test_large_numbers(self):
        arr = [100, 1, 100, 1]
        sophia_gain, mateo_gain, _ = coins_game(arr)
        
        self.assertEqual( sophia_gain , 200)  
        self.assertEqual( mateo_gain , 2)   

    def test_empty_coins_array(self):
        arr = []
        sophia_gain, mateo_gain, _ = coins_game(arr)
        
        self.assertEqual( sophia_gain , 0)  
        self.assertEqual( mateo_gain , 0)  

    def test_single_coin(self):
        arr = [1]
        sophia_gain, mateo_gain, _ = coins_game(arr)
        
        self.assertEqual( sophia_gain , 1)  
        self.assertEqual( mateo_gain , 0)  

    def test_exploracion_caso1(self):
        arr = [4,10,2]
        sophia_gain, mateo_gain, _ = coins_game(arr)
        
        self.assertEqual( sophia_gain , 6)  
        self.assertEqual( mateo_gain , 10)  

    def test_exploracion_caso1(self):
        arr = [4,10,2]
        sophia_gain, mateo_gain, _ = coins_game(arr)
        
        self.assertEqual( sophia_gain , 6)  
        self.assertEqual( mateo_gain , 10)  
    
    def test_exploracion_caso2(self):
        arr = [5,15,3,7]
        sophia_gain, mateo_gain, _ = coins_game(arr)
        
        self.assertEqual( sophia_gain , 22)  
        self.assertEqual( mateo_gain , 8)  

    def test_exploracion_caso3(self):
        arr = [4,10,5,2]
        sophia_gain, mateo_gain, _ = coins_game(arr)
        
        self.assertEqual( sophia_gain , 12)  
        self.assertEqual( mateo_gain , 9)  
    
    def test_exploracion_caso3(self):
        arr = [10, 5, 7, 8, 15, 1]
        sophia_gain, mateo_gain, _ = coins_game(arr)
        
        self.assertEqual( sophia_gain , 32)  
        self.assertEqual( mateo_gain , 14)

    def test_volumen(self):
        arr = [i for i in range(5000)]
        sophia_gain, _, _ = coins_game(arr)

        self.assertEqual(sophia_gain, 6250000)


    def test_volumen_random(self):
        arr = [i for i in range(10000)]
        random.seed(42)  
        random.shuffle(arr)  
        sophia_gain, _, _ = coins_game(arr)

        self.assertEqual(sophia_gain, 28430591)



if __name__ == "__main__":
    unittest.main()