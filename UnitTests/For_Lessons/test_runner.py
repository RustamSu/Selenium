import unittest
from UnitTests.For_Lessons import test_calc

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(test_calc.TestCalc))
# calcTestSuite.addTest(unittest.makeSuite(calc_tests.CalcExTests))
print("count of tests: " + str(calcTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)