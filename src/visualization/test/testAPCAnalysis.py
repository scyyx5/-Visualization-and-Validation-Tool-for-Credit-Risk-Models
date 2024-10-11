import unittest
import pandas as pd
import sys
sys.path.insert(1, '../')
from APCAnalysis import get_effect,visualize_effect,visualize_lexis_diagram,apc_analysis
import unittest
import numpy as np
from sklearn.linear_model import Ridge
from generateRandomTestCase import *
import random,os

class TestGetEffect(unittest.TestCase):
    def setUp(self):
        random.seed(2)
        # Define test data
        self.test_data = pd.DataFrame({
            't': generateRandomIntTestCase(random.randint(0,1000),5,0,100),
            'v': generateRandomIntTestCase(random.randint(0,1000),5,0,100),
            'y': generateRandomIntTestCase(random.randint(0,1000),5,0,100),
            'pd': generateRandomFloatTestCase(random.randint(0,1000),5,0,100)
            })
        
    def test_output_type(self):
        # Test that function returns a dictionary
        output = get_effect(self.test_data)
        self.assertIsInstance(output, dict)
        
    def test_output_keys(self):
        # Test that dictionary keys are present in the output
        output = get_effect(self.test_data)
        expected_keys = ['len_t', 'len_v', 'len_c', 'effect_list_predicted', 'effect_list_real', 'v', 't', 'c', 'default_rate', 'default_rate_real']
        for key in expected_keys:
            self.assertIn(key, output.keys())
        
    def test_output_values(self):
        # Test that the values of the dictionary are of the expected types
        output = get_effect(self.test_data)
        self.assertIsInstance(output['len_t'], int)
        self.assertIsInstance(output['len_v'], int)
        self.assertIsInstance(output['len_c'], int)
        self.assertIsInstance(output['effect_list_predicted'], Ridge)
        self.assertIsInstance(output['effect_list_real'], Ridge)
        self.assertIsInstance(output['v'], np.ndarray)
        self.assertIsInstance(output['t'], np.ndarray)
        self.assertIsInstance(output['c'], np.ndarray)
        self.assertIsInstance(output['default_rate'], list)
        self.assertIsInstance(output['default_rate_real'], list)
        
    def test_default_rate_dimensions(self):
        # Test that default_rate is a 2D array with expected dimensions
        output = get_effect(self.test_data)
        self.assertEqual(len(output['default_rate']), output['len_t'])
        self.assertEqual(len(output['default_rate'][0]), output['len_c'])
        
    def test_default_rate_real_dimensions(self):
        # Test that default_rate_real is a 2D array with expected dimensions
        output = get_effect(self.test_data)
        self.assertEqual(len(output['default_rate_real']), output['len_t'])
        self.assertEqual(len(output['default_rate_real'][0]), output['len_c'])
    
    # Given a dataset as test case. Generate follow-up test case by changing
    # all the value in the original dataset except the value for 't' and 'v'.
    # The result 'c', 'v','c' list of those two test cases will be the same.
    # Test 1000 times by random testing
    def test_metamorphic1(self):
        random.seed(0)
        for i in range(10):
            seed1 = random.randint(0,1000)
            seed2 = random.randint(0,1000)
            data1 = pd.DataFrame({
                't': generateRandomIntTestCase(seed1,1000,0,100),
                'v': generateRandomIntTestCase(seed2,1000,0,100),
                'y': generateRandomIntTestCase(random.randint(0,1000),1000,0,1),
                'pd': generateRandomFloatTestCase(random.randint(0,1000),1000,0,1)
            })
            data2 = pd.DataFrame({
                't': generateRandomIntTestCase(seed1,1000,0,100),
                'v': generateRandomIntTestCase(seed2,1000,0,100),
                'y': generateRandomIntTestCase(random.randint(0,1000),1000,0,1),
                'pd': generateRandomFloatTestCase(random.randint(0,1000),1000,0,1)
            })
            output1 = get_effect(data1)
            output2 = get_effect(data2)
            for i in range(0,len(output1["v"])):
                self.assertEqual(output1["v"][i],output2["v"][i])
            for i in range(0,len(output1["t"])):
                self.assertEqual(output1["t"][i],output2["t"][i]) 
            for i in range(0,len(output1["c"])):
                self.assertEqual(output1["c"][i],output2["c"][i]) 

        # Higher input default rate will generate higher apc effect
        def test_metamorphic2(self):
            data = pd.read_csv(f"../simDTS.csv")
            output1 = get_effect(data)
            data['pd'] = data['pd'] + 0.0000001
            output2 = get_effect(data)
            for i in range(0,len(output1['default_rate'])):
                self.assertTrue(output1['default_rate'] < output2["default_rate"])
            


class TestAPCAnalysis1(unittest.TestCase):
    def setUp(self):
        data = pd.read_csv(f"../simDTS.csv")
        apc_analysis(data)

    def test_visualize1(self):
        self.assertTrue(os.path.exists('../../../res/cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/periodeffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_periodeffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_periodeffect.html'))
    
    def test_visualize2(self):
        theme_name = ["hot_r","YlGnBu","OrRd","greys","yellows","greens","blues","Spectral","PiYG" ]
        for i in theme_name:
            self.assertTrue(os.path.exists('../../../res/apc_lexis_diagram_' + i +'.html'))
            self.assertTrue(os.path.exists('../../../res/real_apc_lexis_diagram_' + i +'.html'))


class TestAPCAnalysis2(unittest.TestCase):
    def setUp(self):
        data = pd.read_csv(f"../simDTS.csv")
        apc_analysis(data,language = "Chinese")

    def test_visualize1(self):
        self.assertTrue(os.path.exists('../../../res/cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/periodeffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_periodeffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_periodeffect.html'))
    
    def test_visualize2(self):
        theme_name = ["hot_r","YlGnBu","OrRd","greys","yellows","greens","blues","Spectral","PiYG" ]
        for i in theme_name:
            self.assertTrue(os.path.exists('../../../res/apc_lexis_diagram_' + i +'.html'))
            self.assertTrue(os.path.exists('../../../res/real_apc_lexis_diagram_' + i +'.html'))


class TestAPCAnalysis3(unittest.TestCase):
    def setUp(self):
        data = pd.read_csv(f"../simDTS.csv")
        apc_analysis(data,language = "Chinese",colorVision="full",isDark=True)

    def test_visualize1(self):
        self.assertTrue(os.path.exists('../../../res/cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/periodeffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_periodeffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_periodeffect.html'))
    
    def test_visualize2(self):
        theme_name = ["hot_r","YlGnBu","OrRd","greys","yellows","greens","blues","Spectral","PiYG" ]
        for i in theme_name:
            self.assertTrue(os.path.exists('../../../res/apc_lexis_diagram_' + i +'.html'))
            self.assertTrue(os.path.exists('../../../res/real_apc_lexis_diagram_' + i +'.html'))

            

class TestVisualizeEffect(unittest.TestCase):
    def setUp(self):
        # Define test data
        self.test_data = pd.DataFrame({
            't': np.asarray(generateRandomIntTestCase(1,5,0,100)),
            'v': np.asarray(generateRandomIntTestCase(6,5,0,100)),
            'y': np.asarray(generateRandomIntTestCase(3,5,0,100)),
            'pd': np.asarray(generateRandomFloatTestCase(8,5,0,100))
        })
    
    def test_file_exists1(self):
        visualize_effect("test",np.asarray(generateRandomIntTestCase(1,100,0,100)),
                         np.asarray(generateRandomFloatTestCase(64,1,0,1)),
                         np.asarray(generateRandomFloatTestCase(452,1,0,1)),
                         False,"None",random.uniform(0, 2),"English")
        self.assertTrue(os.path.exists('../../../res/testeffect.html'))

    def test_file_exists2(self):
        visualize_effect("test",np.asarray(generateRandomIntTestCase(1,100,0,100)),
                         np.asarray(generateRandomFloatTestCase(31,1,0,1)),
                         np.asarray(generateRandomFloatTestCase(351,1,0,1)),
                         True,"None",random.uniform(0, 2),"English")
        self.assertTrue(os.path.exists('../../../res/testeffect.html'))
    
    def test_file_exists3(self):
        visualize_effect("test",np.asarray(generateRandomIntTestCase(1,100,0,100)),
                         np.asarray(generateRandomFloatTestCase(0,1,0,1)),
                         np.asarray(generateRandomFloatTestCase(6,1,0,1)),
                         True,"redGreen",random.uniform(0, 2),"English")
        self.assertTrue(os.path.exists('../../../res/testeffect.html'))

    def test_file_exists4(self):
        visualize_effect("test",np.asarray(generateRandomIntTestCase(1,100,0,100)),
                         np.asarray(generateRandomFloatTestCase(43,1,0,1)),
                         np.asarray(generateRandomFloatTestCase(515,1,0,1)),
                         True,"blueYellow",random.uniform(0, 2),"English")
        self.assertTrue(os.path.exists('../../../res/testeffect.html'))

    def test_file_exists5(self):
        visualize_effect("test",np.asarray(generateRandomIntTestCase(43154,100,0,100)),
                         np.asarray(generateRandomFloatTestCase(54134,1,0,1)),
                         np.asarray(generateRandomFloatTestCase(5413,1,0,1)),
                         True,"blueYellow",random.uniform(0, 2),"Chinese")
        self.assertTrue(os.path.exists('../../../res/testeffect.html'))
    def test_file_exists6(self):
        visualize_effect("age",np.asarray(generateRandomIntTestCase(43154,100,0,100)),
                         np.asarray(generateRandomFloatTestCase(54134,1,0,1)),
                         np.asarray(generateRandomFloatTestCase(5413,1,0,1)),
                         True,"blueYellow",random.uniform(0, 2),"Chinese")
        self.assertTrue(os.path.exists('../../../res/ageeffect.html'))

    def test_file_exists7(self):
        visualize_effect("period",np.asarray(generateRandomIntTestCase(43154,100,0,100)),
                         np.asarray(generateRandomFloatTestCase(54134,1,0,1)),
                         np.asarray(generateRandomFloatTestCase(5413,1,0,1)),
                         True,"blueYellow",random.uniform(0, 2),"Chinese")
        self.assertTrue(os.path.exists('../../../res/periodeffect.html'))
    
    def test_file_exists8(self):
        visualize_effect("cohort",np.asarray(generateRandomIntTestCase(43154,100,0,100)),
                         np.asarray(generateRandomFloatTestCase(54134,1,0,1)),
                         np.asarray(generateRandomFloatTestCase(5413,1,0,1)),
                         True,"blueYellow",random.uniform(0, 2),"Chinese")
        self.assertTrue(os.path.exists('../../../res/cohorteffect.html'))
        
        



        
#if __name__ == '__main__':
    #unittest.main()
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestGetEffect)
unittest.TextTestRunner(verbosity=2).run(suite1)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestVisualizeEffect)
unittest.TextTestRunner(verbosity=2).run(suite2)
suite3 = unittest.TestLoader().loadTestsFromTestCase(TestAPCAnalysis1)
unittest.TextTestRunner(verbosity=2).run(suite3)
suite4 = unittest.TestLoader().loadTestsFromTestCase(TestAPCAnalysis2)
unittest.TextTestRunner(verbosity=2).run(suite4)
suite5 = unittest.TestLoader().loadTestsFromTestCase(TestAPCAnalysis3)
unittest.TextTestRunner(verbosity=2).run(suite5)