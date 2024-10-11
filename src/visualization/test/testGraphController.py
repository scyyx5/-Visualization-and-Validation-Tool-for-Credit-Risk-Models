import unittest
import sys
sys.path.insert(1, '../')
from GraphController import GraphController


class TestGraphController(unittest.TestCase):
    def setUp(self):
        self.graph_controller = GraphController(filename="../simDTS", isDark=True, error="0", age_unit="Year", 
                                                cohort_unit="Month", separator=",", decimal=".")

    def test_initialize(self):
        self.assertEqual(self.graph_controller.isDark,True)
        self.assertEqual(self.graph_controller.error,"0")
        self.assertEqual(self.graph_controller.age_unit,"Year")
        self.assertEqual(self.graph_controller.cohort_unit,"Month")
        self.assertEqual(self.graph_controller.colorVision,"None")
        self.assertEqual(self.graph_controller.language,"English")

    def test_data_filter_greater_than(self):
        data = self.graph_controller.data_filter("x1",">","500")
        for i in data["x1"]:
            self.assertTrue(i > 500)
        self.assertTrue(len(self.graph_controller.data) >= len(data))

    def test_data_filter_less_than(self):
        data = self.graph_controller.data_filter("x1","<","500")
        for i in data["x1"]:
            self.assertTrue(i < 500)
        self.assertTrue(len(self.graph_controller.data) >= len(data))

    def test_data_filter_no_condition(self):
        data = self.graph_controller.data_filter("x1","None","500")
        self.assertTrue(all(data["t"] == self.graph_controller.data["t"]))
        self.assertEqual(len(self.graph_controller.data), len(data))

    def test_unit_year(self):
        graph_controller1 = GraphController(filename="../simDTS", isDark=True, error="0", age_unit="Year", 
                                                cohort_unit="Year", separator=",", decimal=".")
        self.assertEqual(graph_controller1.age_unit,"Year")
        self.assertEqual(graph_controller1.cohort_unit,"Year")

    def test_unit_day(self):
        graph_controller1 = GraphController(filename="../simDTS", isDark=True, error="0", age_unit="Day", 
                                                cohort_unit="Day", separator=",", decimal=".")
        self.assertEqual(graph_controller1.age_unit,"Day")
        self.assertEqual(graph_controller1.cohort_unit,"Day")


suite = unittest.TestLoader().loadTestsFromTestCase(TestGraphController)
unittest.TextTestRunner(verbosity=2).run(suite)