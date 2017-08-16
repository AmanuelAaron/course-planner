from course_planner import *
from course_database import *
import time
import copy



''' # of courses test'''
#Test Case 1
courses1 = ["CSC108", "CSC148"]
summer1 = True
years1 = 1
unavbl1 = []
#Test Case 2
courses2 = ["CSC108", "CSC148", "CSC165"]
summer2 = True
years2 = 1
unavbl2 = []
#Test Case 3
courses3 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer3 = True
years3 = 2
unavbl3 = []
#Test Case 4
courses4 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258"]
summer4 = True
years4 = 2
unavbl4 = []
#Test Case 5
courses5 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258", "CSC384", "CSC369"]
summer5 = True
years5 = 3
unavbl5 = []
#Test Case 6
courses6 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258", "CSC384", "CSC369", "CSC373", "CSC343", "CSC309"]
summer6 = True
years6 = 3
unavbl6 = []
#Test Case 7
courses7 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258", "CSC384", "CSC369", "CSC373", "CSC343", "CSC309", "CSC300", "CSC495", "CSC411"]
summer7 = True
years7 = 4
unavbl7 = []
#Test Case 8
courses8 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258", "CSC384", "CSC369", "CSC373", "CSC343", "CSC309", "CSC300", "CSC495", "CSC411", "CSC412", "CSC420"]
summer8 = True
years8 = 4
unavbl8 = []

''' # of unavailable days test'''
#Test Case 1
courses9 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer9 = True
years9 = 4
unavbl9 = ["MM"]
#Test Case 2
courses10 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer10 = True
years10 = 4
unavbl10 = ["MM", "FN"]
#Test Case 3
courses11 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer11 = True
years11 = 4
unavbl11 = ["FN", "MM", "WD"]
#Test Case 4
courses12 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer12 = True
years12 = 4
unavbl12 = ["FN", "MM", "WD", "TM"]
#Test Case 5
courses13 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer13 = True
years13 = 4
unavbl13 = ["FN", "MM", "WD", "TM", "JE"]
#Test Case 6
courses14 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer14 = True
years14 = 4
unavbl14 = ["FN", "MM", "WD", "TM", "JE", "FE"]
#Test Case 7
courses15 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer15 = True
years15 = 4
unavbl15 = ["FN", "MM", "WD", "TM", "JE", "FE", "WN"]
#Test Case 8
courses16 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer16 = True
years16 = 4
unavbl16 = ["FN", "MM", "WD", "TM", "JE", "FE", "WN", "TD"]

'''# of solutions found '''
#Test Case 1
courses17 = ["CSC108", "CSC148"]
summer17 = True
years17 = 2
unavbl17 = []
#Test Case 2
courses18 = ["CSC108", "CSC148", "CSC165"]
summer18 = True
years18 = 2
unavbl18 = []
#Test Case 2
courses19 = ["CSC108", "CSC148", "CSC165", "CSC207"]
summer19 = True
years19 = 2
unavbl19 = []
#Test Case 3
courses20 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer20 = True
years20 = 2
unavbl20 = []
