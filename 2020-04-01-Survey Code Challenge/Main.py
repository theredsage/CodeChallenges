import csv

# used to make finding columns easier + more flexible
csvheader = []
salarycolumn = int(0)
namecolumn = int(0)
gpacolumn = int(0)
professioncolumn = int(0)
agecolumn = int(0)
marriedcolumn = int(0)

# used for calculating average salary for requirement #1
totalsalarysum = float(0)
totalsalarycount = int(0)

# used for calculating average GPA for requirement #2
totalgpasum = float(0)
totalgpacount = int(0)

# used for calculating popular professions for requirement #3
popularprofessions = {}

# used for calculating the median married ages for requirement #4
marriedages = []


def getColumnIndex(name):
    """
    This gets the numerical index for the column you want to find in the CSV file
    This makes it more intuitive and easier to maintain as the structure of the code / file changes
    """
    global csvheader

    index = csvheader.index(name)
    # print(str(index))
    return index


def addSalaryToAve(row):
    """
    adds the current row's salary to the list for later computation using getSalaryAve()
    """
    global salarycolumn
    global totalsalarysum
    global totalsalarycount

    totalsalarysum += float(row[salarycolumn])
    totalsalarycount += int(1)


def getSalaryAve():
    """
    Does the average salary computation
    This is separated out from addSalaryToAve to save CPU cycles
    """
    global totalsalarysum
    global totalsalarycount

    salaryaverage = float(totalsalarysum) / float(totalsalarycount)

    #print(totalsalarysum)
    #print(totalsalarycount)
    #print(str(salaryaverage))

    return salaryaverage


def addGPAToAve(row):
    """
    For all people with last names starting with "A"
    adds the current row's GPA to the list for later computation using getGPAAve()
    """
    global totalgpasum
    global totalgpacount

    fullname = row[namecolumn].split(" ")
    lastinitial = fullname[1][0]
    #print(fullname)
    #print(lastinitial)

    if lastinitial == "A":
        # print(lastinitial)
        totalgpasum += float(row[gpacolumn])
        totalgpacount += int(1)


def getGPAAve():
    """
    Does the average GPA computation
    This is separated out from addGPAToAve to save CPU cycles
    """
    global totalgpasum
    global totalgpacount

    gpaaverage = float(totalgpasum) / float(totalgpacount)

    #print(totalgpasum)
    #print(totalgpacount)
    #print(str(gpaaverage))

    return gpaaverage


def addPopularProfession(row):
    """
    Creates a dictionary of popular professions to be used later by getPopularProfession()
    """
    global popularprofessions

    profession = row[professioncolumn]

    if profession not in popularprofessions:
        popularprofessions[profession] = int(1)
    else:
        popularprofessions[profession] += int(1)

    # print(profession, popularprofessions[profession])


def getPopularProfession():
    """
    Gets the most popular profession
    This is separated out from addPopularProfession to save CPU cycles
    """
    global popularprofessions

    profession = max(popularprofessions, key=popularprofessions.get)
    # print(profession, popularprofessions[profession])

    return profession


def addMedianMarriedAge(row):
    """
    If person is married, adds age to list to get median later in getPopularProfession()
    """
    global agecolumn
    global marriedcolumn
    global marriedages

    # print(row[marriedcolumn])
    if (row[marriedcolumn].lower() == 'true'):
        # print("married", row[agecolumn])
        marriedages.append(int(row[agecolumn]))


def getMedianMarriedAge():
    """
    Gets the median married age
    This is separated out from addPopularProfession to save CPU cycles
    """
    global marriedages
    # print(marriedages[-10:])

    marriedages.sort()

    # -1 addresses the base 0 vs total count issue
    totalmarried = len(marriedages) - 1

    median = int(totalmarried / 2)
    # print(marriedages[median])

    return marriedages[median]


if __name__ == "__main__":
    with open("survey_data.csv", 'r', newline='') as csvfile:
        csvtable = csv.reader(csvfile)

        # Separate out the header row from rest of the data
        for row in csvtable:
            csvheader = row
            # print(csvheader)

            # Columns used through the program - putting them here saves CPU cycles
            salarycolumn = getColumnIndex('salary')
            namecolumn = getColumnIndex('name')
            gpacolumn = getColumnIndex('gpa')
            professioncolumn = getColumnIndex('job')
            agecolumn = getColumnIndex('age')
            marriedcolumn = getColumnIndex('married')
            break

        # Roll through the remaining rows of data
        for row in csvtable:
            # print(row)
            # break

            # Does the data processing for each of the requirements listed below
            addSalaryToAve(row)
            addGPAToAve(row)
            addPopularProfession(row)
            addMedianMarriedAge(row)

        # Requirement 1 - Find the average salary
        print(f"1. {getSalaryAve():.2f}")
        # Requirement 2 - Find the average GPA (for all last names starting with "A")
        print(f"2. {getGPAAve():.2f}")
        # Requirement 3 - Find the most popular profession
        print("3.", getPopularProfession())
        # Requirement 4 - Median Age of Married People
        print("4.", getMedianMarriedAge())
