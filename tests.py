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
#Test Case 9
courses9 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer9 = True
years9 = 4
unavbl9 = ["MM"]
#Test Case 10
courses10 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer10 = True
years10 = 4
unavbl10 = ["MM", "FN"]
#Test Case 11
courses11 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer11 = True
years11 = 4
unavbl11 = ["FN", "MM", "WD"]
#Test Case 12
courses12 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer12 = True
years12 = 4
unavbl12 = ["FN", "MM", "WD", "TM"]
#Test Case 13
courses13 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer13 = True
years13 = 4
unavbl13 = ["FN", "MM", "WD", "TM", "JE"]
#Test Case 14
courses14 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer14 = True
years14 = 4
unavbl14 = ["FN", "MM", "WD", "TM", "JE"]
#Test Case 15
courses15 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer15 = True
years15 = 4
unavbl15 = ["FN", "MM", "WD", "TM", "JE", "FE"]
#Test Case 16
courses16 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer16 = True
years16 = 4
unavbl16 = ["FN", "MM", "WD", "TM", "JE", "FE", "WN"]

''' Summer test'''

if __name__ == "__main__":
	c_dat1 = copy.deepcopy(dat)
	c_dat2 = copy.deepcopy(dat)
	c_dat3 = copy.deepcopy(dat)
	c_dat4 = copy.deepcopy(dat)
	c_dat5 = copy.deepcopy(dat)
	c_dat6 = copy.deepcopy(dat)
	c_dat7 = copy.deepcopy(dat)
	c_dat8 = copy.deepcopy(dat)
	c_dat9 = copy.deepcopy(dat)
	c_dat10 = copy.deepcopy(dat)
	c_dat11 = copy.deepcopy(dat)
	c_dat12 = copy.deepcopy(dat)
	c_dat13 = copy.deepcopy(dat)
	c_dat14 = copy.deepcopy(dat)
	c_dat15 = copy.deepcopy(dat)
	c_dat16 = copy.deepcopy(dat)
	print("Test Case 1")
	s_time = time.process_time()
	sols = find_sols(courses1, summer1, years1, unavbl1, c_dat1)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")
	
	print("Test Case 2")
	s_time = time.process_time()
	sols = find_sols(courses2, summer2, years2, unavbl2, c_dat2)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 3")
	s_time = time.process_time()
	sols = find_sols(courses3, summer3, years3, unavbl3, c_dat3)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 4")
	for c in dat["CSC108"][2]:
		if not c in  c_dat4["CSC108"][2]:
			print(c)
	s_time = time.process_time()
	sols = find_sols(courses4, summer4, years4, unavbl4, c_dat4)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	print("------------------------------------------")

	print("Test Case 5")
	s_time = time.process_time()
	sols = find_sols(courses5, summer5, years5, unavbl5, c_dat5)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	print("------------------------------------------")

	print("Test Case 6")
	s_time = time.process_time()
	sols = find_sols(courses6, summer6, years6, unavbl6, c_dat6)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 7")
	s_time = time.process_time()
	sols = find_sols(courses7, summer7, years7, unavbl7, c_dat7)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 8")
	s_time = time.process_time()
	sols = find_sols(courses8, summer8, years8, unavbl8, c_dat8)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")
	
	print("Unavailable Days Tests")
	print("")
	print("Test Case 9")
	s_time = time.process_time()
	sols = find_sols(courses9, summer9, years9, unavbl9, c_dat9)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 10")
	s_time = time.process_time()
	sols = find_sols(courses10, summer10, years10, unavbl10, c_dat10)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 11")
	s_time = time.process_time()
	sols = find_sols(courses11, summer11, years11, unavbl11, c_dat11)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 12")
	s_time = time.process_time()
	sols = find_sols(courses12, summer12, years12, unavbl12, c_dat12)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 13")
	s_time = time.process_time()
	sols = find_sols(courses13, summer13, years13, unavbl13, c_dat13)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 14")
	s_time = time.process_time()
	sols = find_sols(courses14, summer14, years14, unavbl14, c_dat14)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 15")
	s_time = time.process_time()
	sols = find_sols(courses15, summer15, years15, unavbl15, c_dat15)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
	print("------------------------------------------")

	print("Test Case 16")
	s_time = time.process_time()
	sols = find_sols(courses16, summer16, years16, unavbl16, c_dat16)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	
