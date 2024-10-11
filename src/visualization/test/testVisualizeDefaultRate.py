import unittest
import pandas as pd
import sys
sys.path.insert(1, '../')
from visualizeDefaultRate import *
import unittest

import numpy as np
from sklearn.linear_model import Ridge
from generateRandomTestCase import *
import random,os

class TestVisualizeData(unittest.TestCase):
    def test_default_age1(self):
        data = pd.read_csv(f"../simDTS.csv")
        default_age(data,False,"None","English")
        self.assertTrue(os.path.exists('../../../res/dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age_predicted.html'))
    
    def test_default_age2(self):
        data = pd.read_csv(f"../simDTS.csv")
        default_age(data,True,"None","English")
        self.assertTrue(os.path.exists('../../../res/dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age_predicted.html'))

    def test_default_age3(self):
        data = pd.read_csv(f"../simDTS.csv")
        default_age(data,True,"redGreen","English")
        self.assertTrue(os.path.exists('../../../res/dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age_predicted.html'))
        
    def test_default_age4(self):
        data = pd.read_csv(f"../simDTS.csv")
        default_age(data,True,"blueYellow","English")
        self.assertTrue(os.path.exists('../../../res/dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age_predicted.html'))

    def test_default_age5(self):
        data = pd.read_csv(f"../simDTS.csv")
        default_age(data,True,"blueYellow","Chinese")
        self.assertTrue(os.path.exists('../../../res/dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age_predicted.html'))
        

    def test_default_cohort1(self):
        data = pd.read_csv(f"../simDTS.csv")
        default_cohort(data,False,"full","English")
        self.assertTrue(os.path.exists('../../../res/dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/dr_cal_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_cal_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_cal_predicted.html'))
    
    def test_default_cohort2(self):
        data = pd.read_csv(f"../simDTS.csv")
        default_cohort(data,True,"None","English")
        self.assertTrue(os.path.exists('../../../res/dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/dr_cal_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_cal_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_cal_predicted.html'))

    def test_default_cohort3(self):
        data = pd.read_csv(f"../simDTS.csv")
        default_cohort(data,True,"redGreen","English")
        self.assertTrue(os.path.exists('../../../res/dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/dr_cal_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_cal_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_cal_predicted.html'))
        
    def test_default_cohort4(self):
        data = pd.read_csv(f"../simDTS.csv")
        default_cohort(data,True,"blueYellow","English")
        self.assertTrue(os.path.exists('../../../res/dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/dr_cal_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_cal_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_cal_predicted.html'))

    def test_default_cohort5(self):
        data = pd.read_csv(f"../simDTS.csv")
        default_cohort(data,True,"blueYellow","Chinese")
        self.assertTrue(os.path.exists('../../../res/dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/dr_cal_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_cal_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_cal.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_cal_predicted.html'))
        
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestVisualizeData)
unittest.TextTestRunner(verbosity=2).run(suite1)