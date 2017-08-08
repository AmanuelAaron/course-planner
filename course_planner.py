import course_database
from course_planner_csp import *
from propagators import *
from orderings import *

COURSES = []
SUMMER = False
YEARS = 0

if __name__ == "__main__":
	yrs = input("How many long do you plan on going to school(years):")
	YEARS = int(yrs)
	
	print("")
	
	smr = input("Do you plan on taking summer courses(y/n):")
	SUMMER = (smr == 'y')
	
	print("")
	
	print("Enter each course you plan on taking one at a time. Enter 'done' when finished:")
	inp = ""
	while(inp != 'done'):
		inp = input("")
		if (inp in course_database.dat.keys()):
			COURSES.append(inp)
		elif(inp != 'done'):
			print("Course not in database")
	
	csp, var_array = course_planner_csp(COURSES, SUMMER, YEARS)
	solver = BT(csp)
	solver.bt_search(prop_GAC)
