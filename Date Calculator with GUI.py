import tkinter as tk

# Frame Creation

window = tk.Tk()
window.title("Date Calculator")

frameInstruction = tk.Frame(master = window)
instruction = tk.Label(master = frameInstruction, text = "Enter current date numerically.")
instruction.grid(row=0, column=0)

frameEntry = tk.Frame(master = window)

frameEnterDay = tk.Frame(master = frameEntry)
frameEnterMonth = tk.Frame(master = frameEntry)
frameEnterYear = tk.Frame(master = frameEntry)
enterDay = tk.Entry(master = frameEnterDay, width = 7)
enterMonth = tk.Entry(master = frameEnterMonth, width = 7)
enterYear = tk.Entry(master = frameEnterYear, width = 7)
enterDay.grid(row=0, column=0)
enterMonth.grid(row=0, column=1)
enterYear.grid(row=0, column=2)

frameDay = tk.Frame(master = frameEntry, width = 7)
frameMonth = tk.Frame(master = frameEntry, width = 7)
frameYear = tk.Frame(master = frameEntry, width = 7)
labelDay = tk.Label(master = frameDay, text = "Day")
labelMonth = tk.Label(master = frameMonth, text = "Month")
labelYear = tk.Label(master = frameYear, text = "Year")
labelDay.grid(row=1, column=0)
labelMonth.grid(row=1, column=1)
labelYear.grid(row=1, column=2)

frameInst2 = tk.Frame(master = window)
labelInst = tk.Label(master = frameInst2, text = "Enter how many days after this date you want.")
labelInst.grid(row=0, column=0)

frameDaysLater = tk.Frame(master = window)
totalEntry = tk.Entry(master = frameDaysLater, width = 7)
totalEntry.grid(row=0, column=0)


# Functions

def IsLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def validate():
    noLeapDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 0 adjusts for indexing from 0, not 1
    LeapDays = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ["","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    day = enterDay.get()
    month = enterMonth.get()
    year = enterYear.get()
    totalDays = totalEntry.get()

    if day.isnumeric() and month.isnumeric() and year.isnumeric() and totalDays.isnumeric():
        day = int(day)
        month = int(month)
        year = int(year)
        totalDays = int(totalDays)

        proceed = False

        if month >= 1 and month <= 12:
            leapYear = IsLeapYear(year)
            if leapYear:
                if day >= 1 and day <= LeapDays[month]:
                    proceed = True
            else:
                if day >= 1 and day <= noLeapDays[month]:
                    proceed = True

        if proceed == True:
            dateDisplay["text"] = calculate(day, month, year, noLeapDays, LeapDays, months, totalDays)


def calculate(day, month, year, noLeapDays, LeapDays, months, totalDays):
    daysLeft = totalDays # working value, reduces with each iteration to 0
    workingDay = day
    workingMonth = month
    workingYear = year

    while daysLeft != 0:
        if IsLeapYear(workingYear):
            daysInMonth = LeapDays[workingMonth]
        else:
            daysInMonth = noLeapDays[workingMonth]
            
        if daysLeft <= (daysInMonth - workingDay): # date in this month
            workingDay += daysLeft
            daysLeft = 0

        else:
            remainingInMonth = daysInMonth - workingDay
            daysLeft = daysLeft - remainingInMonth - 1 # extra 1 counts first day of next month
            workingDay = 1
            workingMonth = (workingMonth + 1) % 12
            if workingMonth == 0:
                workingMonth = 12 # as 12 mod 12 is 0
            elif workingMonth == 1:
                workingYear = workingYear + 1

    finalDate = str(workingDay) + " " + months[workingMonth] + " " + str(workingYear)
    return finalDate        
            

# Remaining frames

frameButton = tk.Frame(master = window)
button = tk.Button(master = frameButton, text = "Get Date", command = validate, bg = "#1E7800")
button.grid(row=0, column=0)

frameDisplay = tk.Frame(master = window)
dateDisplay = tk.Label(master = frameDisplay, text = "")
dateDisplay.grid(row=0, column=0)


# Put frames in grid

frameInstruction.grid(row=0, column=0, padx=10)
frameEntry.grid(row=1, column=0, padx=10)

frameDay.grid(row=1, column=0, padx=10)
frameMonth.grid(row=1, column=1, padx=10)
frameYear.grid(row=1, column=2, padx=10)
frameEnterDay.grid(row=2, column=0, padx=10)
frameEnterMonth.grid(row=2, column=1, padx=10)
frameEnterYear.grid(row=2, column=2, padx=10)

frameInst2.grid(row=2, column=0, padx=10)
frameDaysLater.grid(row=3, column=0, padx=10)
frameButton.grid(row=4, column=0, padx=10)
frameDisplay.grid(row=5, column=0, padx=10)


window.mainloop()
