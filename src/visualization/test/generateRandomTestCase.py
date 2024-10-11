import random
import math
def generateRandomFloatTestCase(seed,numArg,lowerBound,upperBound):
    random.seed(seed)
    testCase = []
    for j in range(0,numArg):
        testCase.append(random.uniform(lowerBound, upperBound))
    return testCase

def generateRandomIntTestCase(seed,numArg,lowerBound,upperBound):
    random.seed(seed)
    testCase = []
    for j in range(0,numArg):
        testCase.append(random.randint(lowerBound, upperBound))
    return testCase



def generateRRTCase(seed,numTestCase,numArg,lowerBound,upperBound,targetExclusionRatio):
    random.seed(seed)
    testCase = []
    normalizedTestCase = []
    for i in range(0,numTestCase):
        normalizedCase = []
        zommCase = []
        while True:
            normalizedCase.clear()
            for j in range(numArg):
                normalizedCase.append(random.uniform(0, 1))
            if validCase(i, normalizedCase,normalizedTestCase,targetExclusionRatio,numArg):
                break
        zoom_temp = testCaseZoom(normalizedCase, lowerBound, upperBound)
        # print("Test case {}: {}".format(i + 1, zoom_temp))
        normalizedTestCase.append(normalizedCase)
        testCase.append(zoom_temp)
    return testCase


def testCaseZoom(lst, lower_bound, upper_bound):
    zoomData = []
    for i in range(len(lst)):
        zoomData.append((upper_bound - lower_bound) * lst[i] + lower_bound)
    return zoomData

def validCase(numTestCase,normalizedCase,normalizedTestCase,targetExclusionRatio,numArg):
    input_size = 1
    for i in range(numTestCase - 1):
        distance = getDistance(normalizedTestCase[i], normalizedCase)
        if distance <= get_radius(input_size * targetExclusionRatio / numTestCase, numArg):
            return False
    return True

def getDistance(lst1, lst2):
    sum = 0
    for i in range(len(lst1)):
        sum += (lst1[i] - lst2[i]) ** 2
    return sum ** 0.5

def get_radius(size, num_argument):
    radius = 0.0
    if num_argument % 2 == 1:
        radius = ((size * get_factorial(num_argument, 2)) /
                  (math.pow(math.pi, (num_argument - 1) / 2.0) *
                   math.pow(2, (num_argument + 1) / 2.0))) ** (1.0 / num_argument)
    else:
        radius = (size * get_factorial(num_argument // 2, 1)) ** (1.0 / num_argument) / math.sqrt(math.pi)
    return radius

def get_factorial(n, interval):
    factorial = 1
    for i in range(1, n+1, interval):
        factorial *= i
    return factorial