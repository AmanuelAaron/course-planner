from cspbase import *
from course_database import *
cdat = dat

course_vars = []

def course_planner_csp(courses, summer, years):
	'''
	'''
	# Create variables for each course and add it to the CSP

	for course in courses:
		dom = cdat[course][2]
		course_vars.append(Variable(course, dom))
	
	course_planner_csp = CSP("course-planner", course_vars)
	
	# Add constraint if no summer courses allowed
	if not summer:
		for var in course_vars:
			cons = Constraint("No Summer", [var])
			dom = cdat[var.name][2]
			valid_vals = []
			for element in dom:
				if element[0][0] % 3 !=  0:
					valid_vals.append(element)
			print(valid_vals)
			cons.add_satisfying_tuples(valid_vals)
			course_planner_csp.add_constraint(cons)
	
	# Add constraints for prereqs
	for course in courses:
		prereqs = cdat[course][0]
		dom = cdat[course][2]
		c_var = find_var(course)
		if len(prereqs) > 0:
			for prereq in prereqs:
				p_var = find_var(prereq)
				cons = Constraint("PreReq", [c_var, p_var])
				######
				valid_vals = []
				for element in dom:
					for section in cdat[prereq][2]:
						if element[0][0] > section[0][0]:
							valid_vals.append((element, section))
				cons.add_satisfying_tuples(valid_vals)			
				######
				course_planner_csp.add_constraint(cons)

	# Add constraints for co-req
	
	# Add custom constraints
	#TBD
	
	return course_planner_csp, course_vars

def find_var(course):
	for var in course_vars:
		if var.name == course:
			return var
	return -1
