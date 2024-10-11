import unittest
import sys
sys.path.insert(1, '../')
from GraphController import *
from visualizeDefaultRate import *
from drawLexisDiagram import *
from APCAnalysis import *
import os


class TestAll(unittest.TestCase):
    def setUp(self):
        self.graph_controller = GraphController(filename="../simDTS", isDark=True, error="0", age_unit="Year", 
                                                cohort_unit="Month", separator=",", decimal=".")

    def test_default_age(self):
        default_age(self.graph_controller.data)
        self.assertTrue(os.path.exists('../../../res/dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age_predicted.html'))

    def test_default_cohort(self):
        default_cohort(self.graph_controller.data)
        self.assertTrue(os.path.exists('../../../res/dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_dr_age_predicted.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age.html'))
        self.assertTrue(os.path.exists('../../../res/exp_dr_age_predicted.html'))
    
    def test_draw_lexis_diagram_real(self):
        draw_Lexis_Diagram_Real(self.graph_controller.data)
        theme_name = ["hot_r","YlGnBu","OrRd","greys","yellows","greens","blues","Spectral","PiYG" ]
        for i in theme_name:
            self.assertTrue(os.path.exists('../../../res/lexis_diagram_' + i + '.html'))

    def test_apc_analysis(self):
        apc_analysis(self.graph_controller.data)
        self.assertTrue(os.path.exists('../../../res/cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/periodeffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/sinh_periodeffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_cohorteffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_ageeffect.html'))
        self.assertTrue(os.path.exists('../../../res/exp_periodeffect.html'))
        theme_name = ["hot_r","YlGnBu","OrRd","greys","yellows","greens","blues","Spectral","PiYG" ]
        for i in theme_name:
            self.assertTrue(os.path.exists('../../../res/apc_lexis_diagram_' + i +'.html'))
            self.assertTrue(os.path.exists('../../../res/real_apc_lexis_diagram_' + i +'.html'))
    
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestAll)
unittest.TextTestRunner(verbosity=2).run(suite1)