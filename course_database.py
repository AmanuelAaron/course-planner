'''
FORMAT
	course name : [prereqs, co-reqs, sections, exclusions]
'''

dat = {"CSC108": [[], [], [((1,'M','M',"Mdfsa"),), ((1,'W','N',"Mdfsa"),), ((2,'T','E',"Mdfsa"),), ((3,'F','D',"Mdfsa"),)], []],
		"CSC148": [["CSC108"], [], [((2,'M','E',"Mdfsa"),), ((3,'M','M',"Mdfsa"),), ((2,'M','N',"Mdfsa"),), ((3,'F','M',"Mdfsa"),), ((4,'J','M',"Mdfsa"),)], []],
		"CSC165": [[], [], [((1,'M','M',"Mdfsa"),), ((3,'M','M',"Mdfsa"),), ((1,'M','N',"Mdfsa"),), ((3,'F','M',"Mdfsa"),), ((4,'J','M',"Mdfsa"),)], []],
		"CSC207": [["CSC148"], [], [((2,'M','E',"Mdfsa"),), ((3,'M','M',"Mdfsa"),), ((2,'M','N',"Mdfsa"),), ((3,'F','M',"Mdfsa"),), ((4,'J','M',"Mdfsa"),)], []],
		"CSC209": [["CSC207"], [], [((2,'M','E',"Mdfsa"),), ((3,'M','M',"Mdfsa"),), ((2,'M','N',"Mdfsa"),), ((3,'F','M',"Mdfsa"),), ((5,'J','M',"Mdfsa"),)], []],
		"CSC236": [["CSC165"], [], [((2,'M','E',"Mdfsa"),), ((3,'M','M',"Mdfsa"),), ((2,'M','N',"Mdfsa"),), ((3,'F','M',"Mdfsa"),), ((4,'J','M',"Mdfsa"),)], []],
		"CSC263": [["CSC236"], [], [((2,'M','E',"Mdfsa"),), ((3,'M','M',"Mdfsa"),), ((2,'M','N',"Mdfsa"),), ((3,'F','M',"Mdfsa"),), ((4,'J','M',"Mdfsa"),)], []],
		"CSC258": [["CSC148"], [], [((2,'M','E',"Mdfsa"),), ((3,'M','M',"Mdfsa"),), ((2,'M','N',"Mdfsa"),), ((3,'F','M',"Mdfsa"),), ((4,'J','M',"Mdfsa"),)], []],
		"MAT137": [[], ["CSC148"], [((1,'M','E',"Mdfsa"),), ((5,'M','M',"Mdfsa"),), ((2,'M','N',"Mdfsa"),), ((3,'F','M',"Mdfsa"),), ((4,'J','M',"Mdfsa"),)], ["MAT135"]],
		"MAT135": [[], ["CSC148"], [((1,'M','E',"Mdfsa"),), ((5,'M','M',"Mdfsa"),), ((2,'M','N',"Mdfsa"),), ((3,'F','M',"Mdfsa"),), ((4,'J','M',"Mdfsa"),)], ["MAT137"]]
		}
