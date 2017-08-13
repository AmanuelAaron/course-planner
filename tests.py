from course_planner import *
from course_database import *
import time

c_dat = dat

#Test Case 1
courses1 = ["CSC108", "CSC148"]
summer1 = False
years1 = 1
unavbl1 = ["MM"]
#Test Case 2
courses2 = ["CSC108", "CSC148", "CSC165"]
summer2 = True
years2 = 1
unavbl2 = ["MM"]
#Test Case 3
courses3 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236"]
summer3 = False
years3 = 2
unavbl3 = []
#Test Case 4
courses4 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258"]
summer4 = True
years4 = 2
unavbl4 = []
#Test Case 5
courses5 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258", "CSC384", "CSC369"]
summer5 = False
years5 = 3
unavbl5 = []
#Test Case 6
courses6 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258", "CSC384", "CSC369", "CSC373", "CSC343", "CSC309"]
summer6 = True
years6 = 3
unavbl6 = []
#Test Case 7
courses7 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258", "CSC384", "CSC369", "CSC373", "CSC343", "CSC309", "CSC300", "CSC495", "CSC411"]
summer7 = False
years7 = 4
unavbl7 = []
#Test Case 8
courses8 = ["CSC108", "CSC148", "CSC165", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258", "CSC384", "CSC369", "CSC373", "CSC343", "CSC309", "CSC300", "CSC495", "CSC411", "CSC412", "CSC420"]
summer8 = True
years8 = 4
unavbl8 = []
if __name__ == "__main__":
	print("Test Case 1")
	s_time = time.process_time()
	sols = find_sols(courses1, summer1, years1, unavbl1, c_dat)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	print("------------------------------------------")

	print("Test Case 2")
	s_time = time.process_time()
	sols = find_sols(courses2, summer2, years2, unavbl2, c_dat)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	print("------------------------------------------")

	print("Test Case 3")
	s_time = time.process_time()
	sols = find_sols(courses3, summer3, years3, unavbl3, c_dat)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	print("------------------------------------------")

	print("Test Case 4")
	s_time = time.process_time()
	sols = find_sols(courses4, summer4, years4, unavbl4, c_dat)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	print("------------------------------------------")

	print("Test Case 5")
	s_time = time.process_time()
	sols = find_sols(courses5, summer5, years5, unavbl5, c_dat)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	print("------------------------------------------")

	print("Test Case 6")
	s_time = time.process_time()
	sols = find_sols(courses6, summer6, years6, unavbl6, c_dat)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	print("------------------------------------------")

	print("Test Case 7")
	s_time = time.process_time()
	sols = find_sols(courses7, summer7, years7, unavbl7, c_dat)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
	print("------------------------------------------")

	print("Test Case 8")
	s_time = time.process_time()
	sols = find_sols(courses8, summer8, years8, unavbl8, c_dat)
	f_time = time.process_time()
	print("Solutions found: " + str(len(sols)))
	print("CPU time used: " + str(f_time - s_time))
