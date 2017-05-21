#
# Given a list of people with their birth and end years (all between 1900 and 2000), 
# find the year with the most number of people alive.
#

#
# Variables
#
# Initialize array holding results
year=[0]*2001
list=(0)
# initialize dataset
""" 
 ssdm = Social Security Death Master file
 real data (with SS stripped)
"""
try:
    fi = open("ssdmfinal.txt", "r")
except IOError:
    print "Error: File does not exist."
    exit()
	  
fo = open("output.csv", "w")

line = fi.readlines()

# Calculate if birth and end date fall within the range
# Throw out any < 1900 ranges
for dates in (line):
	dates = dates.strip()
	people=(dates[37:56])
	end=int(people[0:4])
	birth=int(people[4:8])
	for years in range(1900,2001):
		if years - birth < 0:
			continue
		if years - birth >= 0 and years - end <= 0:
			year[years]=year[years]+1

# Print results to CSV file for graphing
for years in range(1900,2001):
		print years, year[years]
		fo.write("%s,%s\n" % (years, year[years]))
		
fi.close()
fo.close()

