import unittest
import pandas as pd
import sys
sys.path.insert(1, '../')
from drawLexisDiagram import *
import unittest
import numpy as np
from sklearn.linear_model import Ridge
from generateRandomTestCase import *
import random,os

class TestDrawLexisDiagram(unittest.TestCase):
    def test_draw_lexis_diagram_real1(self):
        data = pd.read_csv(f"../simDTS.csv")
        draw_Lexis_Diagram_Real(data,"English")
        theme_name = ["hot_r","YlGnBu","OrRd","greys","yellows","greens","blues","Spectral","PiYG" ]
        for i in theme_name:
            self.assertTrue(os.path.exists('../../../res/lexis_diagram_' + i + '.html'))

suite1 = unittest.TestLoader().loadTestsFromTestCase(TestDrawLexisDiagram)
unittest.TextTestRunner(verbosity=2).run(suite1)