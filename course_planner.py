from course_database import *
from course_planner_csp import *
from propagators import *
from orderings import *
from filter import *
import time

COURSES = []
SUMMER = False
YEARS = 0
UNAVBL = []
PREF_TIME = []
PROF_PREF = 1
format_database()
CURR_DAT = dat.copy()
SOL = []
PROP = prop_FC

def find_sols(courses, summer, years, unavbl, c_dat):
	
	sols = []
	soln = dict()
	while soln != None:
		csp, var_array = course_planner_csp(courses, summer, years, unavbl, c_dat)
		solver = BT(csp)
		soln = solver.bt_search(PROP)
		if soln != None:
			sols.append(soln)
			for course in soln.keys():
				c_dat[course][2].remove(soln[course])
	return sols

def one_sol(courses, summer, years, unavbl, c_dat):
	csp, var_array = course_planner_csp(courses, summer, years, unavbl, c_dat)
	solver = BT(csp)
	soln = solver.bt_search(PROP)
	return soln != None

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
		if (inp in dat.keys()):
			if inp in COURSES:
				print("You have already entered this course")
			elif set(dat[inp][3]).intersection(set(COURSES)) != set():
				print("You cannot take " + inp + " with any of these courses:")
				print(dat[inp][3])
			else:
				COURSES.append(inp)
		elif(inp != 'done'):
			print("Course not in database")
		elif inp == 'done':
			if len(COURSES) < 2:
				print("Too few courses. Please add more")
				inp = ""

	print("")
	print("What times are you unavailable Enter 'done' when finished:")
	print("(FORMAT : M,T,W,J,F = Mon, Tues, Wed, Thur, Fri")
	print("		M,D,E,N = Morning, Day, Evening, Night")
	print(" Example: I am unavailble Monday Morning -> 'MM')")
	inp = ""
	while(inp != 'done'):
		inp = input("")
		if (inp[0] in ["M", "T", "W", "J", "F"] and inp[1] in ["M","D","E","N"]):
			UNAVBL.append(inp)
		elif(inp != 'done'):
			print("invalid input")

	print("")
	print("What are your preferred timeslots? Enter 'done' when finished:")
	print("(FORMAT : M,T,W,J,F = Mon, Tues, Wed, Thur, Fri")
	print("		M,D,E,N = Morning, Day, Evening, Night")
	print(" Example: I prefer to take classes on Tuesday Evenings -> 'TE')")
	inp2 = ""
	while(inp2 != 'done'):
		inp2 = input("")
		if (inp2[0] in ["M", "T", "W", "J", "F"] and inp2[1] in ["M","D","E","N"]):
			PREF_TIME.append(inp2)
		elif(inp2 != 'done'):
			print("invalid input")
	print("")
	PROF_PREF = input("Rate the importance of the quality of professors from 1-5\n1 being not important and 5 being very important: ")
	PROF_PREF = int(PROF_PREF)
	soln = dict()
	s_time = time.process_time()
	while soln != None:
		csp, var_array = course_planner_csp(COURSES, SUMMER, YEARS, UNAVBL, CURR_DAT)
		if csp == None:
			break
		solver = BT(csp)
		soln = solver.bt_search(PROP)
		if soln != None:
			SOL.append(soln)
			for course in soln.keys():
				CURR_DAT[course][2].remove(soln[course])
		if float(time.process_time() - s_time) > 8:
			break
	f_time = time.process_time()
	t_time = f_time - s_time
	print("# of Solutions Found: " + str(len(SOL)))
	print("CPU time used: " + str(t_time))
	sol = get_best_solution(SOL, PREF_TIME, PROF_PREF)
	print("Your best solution is: ")
	print(sol)

		
