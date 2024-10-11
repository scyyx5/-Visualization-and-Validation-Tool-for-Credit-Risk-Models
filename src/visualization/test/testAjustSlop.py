import unittest
import sys
sys.path.insert(1, '../')
from adjustSlope import adjust_slope
from generateRandomTestCase import * 
import random


class TestAdjustSlop(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_basic(self):
        xList = [1, 2, 3, 4, 5]
        yList = [1, 2, 3, 4, 5]
        error = 0.5
        expected_output = [1, 1.5, 3.0, 4.5, 6.0]
        self.assertEqual(adjust_slope(xList, yList, error), expected_output)
    
    # Randomly generate a test case. Use the same x list and add randomly generated
    # positive value to all value in y list to get a follow-up test case.
    # All the value of the output list using original test cases will be 
    # less than the value of the output list using the follow-up test case.
    def test_metamorphic1(self):
        random.seed(1)
        for i in range(1000):
            xList = generateRRTCase(random.seed(0,100000),100,100,-100,100,0.5)
            yList1 = generateRRTCase(random.seed(0,100000),100,100,-100,100,0.5)
            yList2 = []
            for list in yList1:
                l = [a+random.uniform(0,10000) for a in list]
                yList2.append(l)

            for i in range(0,len(xList)):
                error = random.uniform(-100,100)
                adjusted_list1 = adjust_slope(xList[i],yList1[i],error)
                adjusted_list2 = adjust_slope(xList[i],yList1[i],error)
                for j in range(0,len(xList)):
                    self.assertTrue(adjusted_list1[j] <= adjusted_list2[j])


    # Randomly generate a test Case. The first n value of x list and y list for the 
    # follow-up test cases is the same as the original test case, while other value
    # in the follow-up test cases is randomly generated. 
    # The first n value in the resulted list from original test cases and the follow-up 
    # test cases is the same.
    def test_metamorphic2(self):
        random.seed(4)
        xList1 = generateRRTCase(random.seed(0,100000),100,100,-100,100,0.5)
        yList1 = generateRRTCase(random.seed(0,100000),100,100,-100,100,0.5)
        for i in range(0,len(xList1)):
            followedxList = []
            followedyList = []
            # assign same value as the original test cases for the first n value
            n = random.randint(1,100)
            for j in range(0,n):
                followedxList.append(xList1[i][j])
                followedyList.append(yList1[i][j])
            # randomly generate the rest of the value in the list
            for k in range(0,random.randint(1,500)):
                followedxList.append(random.uniform(-100,100))
                followedyList.append(random.uniform(-100,100))
            

            error = random.uniform(-100,100)
            adjustedList1 = adjust_slope(xList1[i],yList1[i],error)
            adjustedList2 = adjust_slope(followedxList,followedyList,error)

            for j in range(0,n):
                self.assertEqual(adjustedList1[j],adjustedList2[j])
    
    


suite1 = unittest.TestLoader().loadTestsFromTestCase(TestAdjustSlop)
unittest.TextTestRunner(verbosity=2).run(suite1)
