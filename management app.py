from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import calendar
import tkinter as tk
import datetime

__author__ = 'Group O'      

class toDoList(Frame):
    def __init__(self):
        self.master = Tk()
        self.content = ttk.Frame(self.master,padding=(12,12,12,12))
        self.Frame = ttk.Frame(self.content, borderwidth=5, relief="sunken", width=280, height=520)
        self.master.title("Personal Scheduler version 2.0 - Updated 17-April 2020 - 14.32")
        self.master.configure(background='light gray')  
        self.highList = []
        self.lowList = []
        
        self.content.grid(column=7, row=0, rowspan=20, sticky=(N, S, E, W))
        self.Frame.grid(column=0, row=0, columnspan=3, rowspan=20, sticky=(N, S, E, W))
        Button(self.master,width = 20,borderwidth=10)
        
        Label(self.master, text= "Task Management").grid(row=1, column=7, sticky=E, padx = 20)
        Button(self.master, text="Add a task", width = 20,borderwidth=3,command=self.addTask).grid(row=2, column=7, sticky=E, padx = 20)
        Button(self.master, text="Edit a task",borderwidth=3,width = 20, command = self.editTasks).grid(row=3, column=7, sticky=E, padx = 20)
        Button(self.master, text="Remove a task",borderwidth=3,width = 20, command = self.remove).grid(row=4, column=7, sticky=E, padx = 20)
        Button(self.master, text="Change priority of task",borderwidth=3,width = 20, command = self.changePriority).grid(row=5, column=7, sticky=E, padx = 20)
        
        Label(self.master, text= "Tasks analysis").grid(row=6, column=7, sticky=E, padx = 20)
        Label(self.master, text= "View by:").grid(row=7, column=7, sticky=E, padx = 120)
        options = ["Day","High","Low","All"]
        self.viewOptions = StringVar(self.master)
        self.viewOptions.set(options[3])
        OptionMenu(self.master, self.viewOptions, *options).grid(row=7, column=7, sticky=E, padx = 20)
        
        Button(self.master, text="View incompleted tasks",borderwidth=3,width = 20, command=self.getViewIncompleteDropDown).grid(row=8, column=7, sticky=E, padx = 20)
        Button(self.master, text="View complete tasks",borderwidth=3,width = 20, command=self.getViewcOompletedDropDown).grid(row=9, column=7, sticky=E, padx = 20)
        Button(self.master, text="View all tasks",borderwidth=3,width = 20, command=self.getViewDropDown).grid(row=10, column=7, sticky=E, padx = 20)

        Label(self.master, text= "File Management").grid(row=11, column=7, sticky=E, padx = 20)   
        Button(self.master, text="Save tasks",borderwidth=3,width = 20, command=self.saveFile).grid(row=12, column=7, sticky=E, padx = 20)
        Button(self.master, text="Load tasks",borderwidth=3,width = 20, command=self.load).grid(row=13, column=7, sticky=E, padx = 20)
        Button(self.master, text="Quit",borderwidth=3,width = 20, command =quit).grid(row=15, column=7, sticky=E, padx = 20)
    
        Label(self.master, text= "Year").grid(row=1, column=7,sticky=W,padx=20)
        years = ["select","2014","2015","2016","2017","2018","2019","2020"]
        self.yearOption = StringVar(self.master)
        self.yearOption.set(years[0])
        OptionMenu(self.master, self.yearOption, *years).grid(row=2, column=7,sticky=W,padx=20)
        
        Label(self.master, text= "Months").grid(row=3, column=7,sticky=W,padx=20)  
        Button(self.master, text="January",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("January")).grid(row=4, column=7, sticky=W,padx=20)
        Button(self.master, text="February",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("February")).grid(row=5, column=7, sticky=W,padx=20)
        Button(self.master, text="March",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("March")).grid(row=6, column=7, sticky=W,padx=20)
        Button(self.master, text="April",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("April")).grid(row=7, column=7, sticky=W,padx=20)
        Button(self.master, text="May",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("May")).grid(row=8, column=7, sticky=W,padx=20)
        Button(self.master, text="June",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("June")).grid(row=9, column=7, sticky=W,padx=20)
        Button(self.master, text="July",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("July")).grid(row=10, column=7, sticky=W,padx=20)
        Button(self.master, text="August",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("August")).grid(row=11, column=7, sticky=W,padx=20)
        Button(self.master, text="September",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("September")).grid(row=12, column=7, sticky=W,padx=20)
        Button(self.master, text="October",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("October")).grid(row=13, column=7, sticky=W,padx=20)
        Button(self.master, text="November",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("November")).grid(row=14, column=7, sticky=W,padx=20)
        Button(self.master, text="December",borderwidth=3,width = 9, command=lambda: self.jumpToMonth("December")).grid(row=14, column=7, sticky=W,padx=20)

        self.cal = calendar.HTMLCalendar(calendar.SUNDAY)
        self.day = 1
        self.year = 2016
        self.month = 7
        self.wid = []
        self.setup()
        self.master.mainloop()

    def jumpToMonth(self, Month):
        Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        x = Months.index(Month)+1
        year = int(self.yearOption.get())
        self.year = year
        self.month = x
        self.clear()
        self.setup()

    def addTask(self):
        self.priority = 0
        #add a label to show which date they are adding it to
        self.top = Toplevel(self.master)
        self.top.title("Add Task - "+str(self.day)+"."+str(self.month)+"."+str(self.year))
        #self.addTaskWindow = Tk()
        #self.addTaskWindow.geometry("300x400")
        Label(self.top, text ="Enter the task name").grid(row=0, column=4,pady=5)
        self.taskName = StringVar()
        Entry(self.top, textvariable=self.taskName).grid(row=0, column=5)        
        Label(self.top, text ="Enter the task priority").grid(row=1, column=4,pady=5)

        #self.priority = StringVar()
        #Entry(self.top, textvariable=self.priority).grid(row=1, column=5)
        
        Button(self.top, text="High",borderwidth=3,width = 4, command=self.High).grid(row=1, column=5, sticky=E)
        Button(self.top, text="Low",borderwidth=3,width = 4, command=self.Low).grid(row=1, column=5, sticky=W)
        
        Label(self.top, text ="Enter the task time estimate").grid(row=2, column=4,pady=5)
        self.timeEstimate = StringVar()
        Entry(self.top, textvariable=self.timeEstimate).grid(row=2, column=5)
        Button(self.top, text="Add task", command=self.addTaskSave).grid(row=3, column=4, columnspan=2,pady=5)

    def High(self):
        self.priority = 1

    def Low(self):
        self.priority = 2

    def addTaskSave(self):
        newTask = []
        tn = self.taskName.get()
        #p = self.priority.get()
        newTask.append(tn)
        newTask.append(self.priority)
        newTask.append(int(self.timeEstimate.get()))
        isCompleted = False
        day = self.day
        month = self.month
        year = self.year
        newTask.append(isCompleted)
        newTask.append(day)
        newTask.append(month)
        newTask.append(year)
        if self.priority == 1:
                self.highList.append(newTask)
                self.top.destroy()
                return self.highList
        elif self.priority ==2:
                self.lowList.append(newTask)
                self.top.destroy()
                return self.lowList
        else:
                messagebox.showerror("Error!!!!", "Invalid priority, please either 1 or 2")


    def viewIncompletedTasks(self):
        self.top = Toplevel(self.master)
        self.top.title("View All Incomplete Tasks")
        self.listbox = Listbox(self.top, selectmode=SINGLE, width = 100, height = 20)
        self.listbox.grid(row=4, column=4, rowspan=8)
        self.listbox.insert(END, "High Priority Tasks:")
        for elem in self.highList:
            if elem[3] == False:
                task = "Task name: " + elem[0] + ", Time estimate: " + str(elem[2]) + "mins, " + ", Date: " + str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                self.listbox.insert(END, task)
        self.listbox.insert(END, "Low Priority Tasks:")
        for item in self.lowList:
            if item[3] == False:
                task = "Task name: " + item[0] + ", Time estimate: " + str(item[2]) + "mins, " + ", Date: " + str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                self.listbox.insert(END, task)

    def viewcompletedTasks(self):
        self.top = Toplevel(self.master)
        self.top.title("View All Incomplete Tasks")
        self.listbox = Listbox(self.top, selectmode=SINGLE, width = 100, height = 20)
        self.listbox.grid(row=4, column=4, rowspan=8)
        self.listbox.insert(END, "High Priority Tasks:")
        for elem in self.highList:
            if elem[3] == True:
                task = "Task name: " + elem[0] + ", Time estimate: " + str(elem[2]) + "mins " + ", Date: " + str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                self.listbox.insert(END, task)
        self.listbox.insert(END, "Low Priority Tasks:")
        for item in self.lowList:
            if item[3] == True:
                task = "Task name: " + item[0] + ", Time estimate: " + str(item[2]) + "mins " + ", Date: " + str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                self.listbox.insert(END, task)
                

    def viewAllTasks(self):
        #self.top = Toplevel(self.master)
        #self.title("View All Incomplete Tasks")
        self.listbox = Listbox(self.master, selectmode=SINGLE, width = 61, height = 13)
        self.listbox.grid(row=8, column=0, rowspan=9, columnspan=7)
        self.listbox.insert(END, "High Priority Tasks:")
        complete = ""
        for elem in self.highList:
            if elem[3] == True:
                complete = "Completed"
            else:
                complete = "Incompleted"
            task = "Task name: " + elem[0] + ", Time estimate: " + str(elem[2]) + "mins, Status: " + complete + ", " + ", Date: " + str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
            self.listbox.insert(END, task)
        self.listbox.insert(END, "Low Priority Tasks:")
        for item in self.lowList:
            if item[3] == True:
                complete = "Completed"
            else:
                complete = "Incompleted"
            task = "Task name: " + item[0] + ", Time estimate: " + str(item[2]) + "mins, Status: " + complete + ", " + ", Date: " + str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
            self.listbox.insert(END, task)
            

    def changePriority(self):
        self.top = Toplevel(self.master)
        self.top.title("Change Priority")
        Label(self.top,text="Task name:").grid(row = 5, column = 8)
        Label(self.top,text="Priority:").grid(row = 6, column = 8)
        self.taskName=StringVar()
        self.taskNameEntry = Entry(self.top, textvariable = self.taskName).grid(row = 5, column = 9)
        priorityOptions = ["High", "Low"]
        self.var = StringVar(self.master)
        self.var.set(priorityOptions[0])
        self.dropdown = OptionMenu(self.top, self.var, *priorityOptions)
        self.dropdown.grid(row=6, column=9, columnspan = 2)
        self.b1 = Button(self.top, text = "OK" , command =self.setPriority).grid(row=7, column=9, columnspan=2)

    def setPriority(self):
        self.tn = str(self.taskName.get())
        self.priority = str(self.var.get())
        i = self.search(self.tn)
        if self.found == True:
            if self.priority == "High":
                self.highList[i][1] = 2
                self.lowList.append(self.highList[i])
                self.highList.remove(self.highList[i])
                self.top.destroy()
                return self.lowList
            else:
                self.lowList[i][1] = 1
                self.highList.append(self.lowList[i])
                self.lowList.remove(self.lowList[i])
                self.top.destroy()
                return self.highList
     
    def search(self, tn):
        self.found = False
        self.notExists = False
        while self.found == False and self.notExists == False:
            if self.priority == "High":
                if self.highList:
                    for self.x in range(len(self.highList)):
                            i = 0
                    if self.highList[i][0] == tn:
                        self.found = True
                        return self.x
                        i+=1
                    if self.found == False:
                        messagebox.showerror("ERROR","Task not found")
                        self.notExists = True
                else:
                    messagebox.showerror("ERROR","Task not found")
                    self.notExists = True
            else:
                if self.lowList:
                    for self.x in range(len(self.lowList)):
                        i = 0
                    if self.lowList[i][0] == tn:
                        self.found = True
                        return self.x
                        i+=1
                    if self.found == False:
                        messagebox.showerror("ERROR","Task not found")
                        self.notExists = True
                else:
                    messagebox.showerror("ERROR","Task not found")
                    self.notExists = True

    def remove(self):
        self.top = Toplevel(self.master)
        self.top.title("Remove Task")
        Label(self.top,text="Task name:").grid(row = 0, column =8)
        Label(self.top,text="Priority:").grid(row = 1, column = 8)
        self.removeTaskName=StringVar()
        self.taskNameEntry = Entry(self.top, textvariable = self.removeTaskName).grid(row = 0, column = 9)
        self.rVar = StringVar(self.master)
        self.rVar.set("High")
        self.dropdown = OptionMenu(self.top, self.rVar, "Low", "High")
        self.dropdown.grid(row=1, column=9, columnspan = 2)
        self.b1 = Button(self.top, text = "OK" , command = self.removeClicked).grid(row=3, column=8, columnspan=2)

    def removeClicked(self):
        #self.priority = self.whichList()
        self.priority = str(self.rVar.get())
        self.rtn = str(self.removeTaskName.get())
        self.i = self.search(self.rtn)
        if self.found == True:
            if self.priority == "High":
                self.highList.remove(self.highList[self.i])
                self.top.destroy()
                return self.highList
            else:
                self.lowList.remove(self.lowList[self.i])
                self.top.destroy()
                return self.lowList


    def load(self):
        tempList = []
        complete = False
        #loadFile()
        fileName = askopenfilename(title='Select File')
        tempList = [line.rstrip().split(",") for line in open(fileName)]
        self.highList = []
        self.lowList = []
        for i in range(len(tempList)):
            if tempList[i][3] == "False":
                complete = False
            else:
                complete = True
            tempList[i][1] = int(tempList[i][1])
            tempList[i][2] = int(tempList[i][2])
            tempList[i][3] = complete
            tempList[i][4] = int(tempList[i][4])
            tempList[i][5] = int(tempList[i][5])
            tempList[i][6] = int(tempList[i][6])
            if tempList[i][1] == 1:
                self.highList.append(tempList[i])
            else:
                self.lowList.append(tempList[i])

    #def loadFile(self):
    #self.loadFileWindow = Tk()
    #self.loadFileWindow.geometry("200x100")
    #self.loadFileWindow.title("Load")
    #self.fn = StringVar()
    #Entry(self.master,textvariable=self.fn).grid(row = 0, column = 3)
    #self.fnLabel = Label(self.master,text="File name:").grid(row = 0, column = 2)
    #self.filename = str(self.fn.get())
    #self.b1 = Button(self.master, text = "OK" , command =self.load).grid(row=1, column=2, columnspan=2)
     
    def save(self):
        self.fileName = str(self.fn.get()) + ".txt"
        myFile = open(self.fileName, "w")
        line = ""
        print(self.lowList[0])
        for i in range(len(self.highList)):
            line = ""
            for task in range(len(self.highList[i])):
                if task != 6:
                #print("i" + str(i))
                #print("t" + str(task))
                    line = line + str(self.highList[i][task]) + ","
                else:
                    line = line + str(self.highList[i][task])
            line = line + "\n"
            myFile.write(line)
        line = ""
        for c in range(len(self.lowList)):
            line = ""
            for info in range(len(self.lowList[c])):
                if info != 6:
                  #  print(c)
                   # print(info)
                    line = line + str(self.lowList[c][info]) + ","
                else:
                    line = line + str(self.lowList[c][info])
            line = line + "\n"
            myFile.write(line)
        myFile.close()
        self.top.destroy()
     

    def saveFile(self):
        self.top = Toplevel(self.master)
        self.top.title("Save File")
        #self.saveFileWindow = Tk()
        #self.saveFileWindow.geometry("200x100")
        #self.saveFileWindow.title("Save")
        self.fn = StringVar()
        Entry(self.top,textvariable=self.fn).grid(row = 4, column = 3)
        self.fnLabel = Label(self.top,text="file name:").grid(row = 4, column = 2)
        self.b1 = Button(self.top, text = "OK" , command =self.save).grid(row=7, column=2, columnspan=2)
        
    def editTasks(self):
        self.top = Toplevel()
        self.top.title("Edit Task")
        #self.editTaskWindow = Tk()
        #self.editTaskWindow.geometry("300x400")
        Label(self.top, text="Edit Tasks").grid(row=0, column=11, columnspan=2)
        Label(self.top, text="")
        Label(self.top,text="Task name:").grid(row = 0, column =11)
        Label(self.top,text="Priority:").grid(row = 1, column = 11)
        self.RetrieveTaskName=StringVar()
        self.taskNameEntry = Entry(self.top, textvariable = self.RetrieveTaskName).grid(row = 0, column = 12)

        self.eVar = StringVar(self.master)
        self.eVar.set("High")
        self.editDropdown = OptionMenu(self.top, self.eVar, "Low", "High")
        self.editDropdown.grid(row=1, column=12, columnspan = 2)

        self.b2 = Button(self.top, text = "Retrieve Task" , command = self.fetchTask).grid(row=2, column=11, columnspan=2)
        Label(self.top, text="Task Name").grid(row=3, column=11)
        self.taskNameEdit = StringVar()
        Entry(self.top, textvariable=self.taskNameEdit).grid(row=3, column=12)
        Label(self.top, text="Task Priority").grid(row=4, column=11)
        self.taskPriorityEdit = StringVar()
        Label(self.top, textvariable=self.taskPriorityEdit).grid(row=4, column=12)
        Label(self.top, text="Time").grid(row=5, column=11)
        self.taskTimeEdit = StringVar()
        Entry(self.top, textvariable=self.taskTimeEdit).grid(row=5, column=12)
        Label(self.top, text="Completion").grid(row=6, column=11)
        self.complete = StringVar(self.master)
        self.complete.set("True")
        self.completeDrop = OptionMenu(self.top, self.complete, "True", "False")
        self.completeDrop.grid(row=6,column=12)

        self.taskDays = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        self.taskMonths = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.taskYears = [2014,2015,2016,2017,2018,2019,2020]
        self.taskDay = IntVar()
        self.taskDay.set(self.taskDays[0])
        self.taskMonth = IntVar()
        self.taskMonth.set(self.taskMonths[0])
        self.taskYear = IntVar()
        self.taskYear.set(self.taskYears[0])
        self.daysDrop = OptionMenu(self.top, self.taskDay, *self.taskDays)
        self.monthDrop = OptionMenu(self.top,self.taskMonth, *self.taskMonths)
        self.yearDrop = OptionMenu(self.top, self.taskYear, *self.taskYears)
        self.daysDrop.grid(row=7, column=11)
        self.monthDrop.grid(row=7, column=12)
        self.yearDrop.grid(row=7, column=13)

        Button(self.top, text = "Save Changes" , command =self.editTaskSave).grid(row=8, column=11, columnspan=3)

    def fetchTask(self):
        messagebox.askokcancel("Fetching task...", "Please save the task to exit")
        self.top.lift()
        self.priority = str(self.eVar.get())
        self.rtn = str(self.RetrieveTaskName.get())
        if self.priority == "High":
            self.taskToEdit = self.highList[self.search(self.rtn)]
        elif self.priority == "Low":
            self.taskToEdit = self.lowList[self.search(self.rtn)]
        if self.found == True:
            self.taskNameEdit.set(self.taskToEdit[0])
            self.taskPriorityEdit.set(self.taskToEdit[1])
            self.taskTimeEdit.set(self.taskToEdit[2])
            self.taskDay.set(self.taskToEdit[4])
            self.taskMonth.set(self.taskToEdit[5])
            self.taskYear.set(self.taskToEdit[6])
            if self.taskToEdit[3] == True:
                self.complete.set("True")
            else:
                self.complete.set("False")
        self.i = self.search(self.rtn)
        if self.found == True:
            if self.priority == "High":
                self.highList.remove(self.highList[self.i])
                return self.highList
            else:
                self.lowList.remove(self.lowList[self.i])
                return self.lowList

    def editTaskSave(self):
         newTask = []
         newTask.append(self.taskNameEdit.get())
         newTask.append(self.taskPriorityEdit.get())
         newTask.append(self.taskTimeEdit.get())
         isCompleted = self.complete.get()
         self.editDay = self.taskDay.get()
         self.editMonth = self.taskMonth.get()
         self.editYear = self.taskYear.get()
         if isCompleted == "True":
            newTask.append(True)
            newTask.append(self.editDay)
            newTask.append(self.editMonth)
            newTask.append(self.editYear)
         elif isCompleted == "False":
            newTask.append(False)
            newTask.append(self.editDay)
            newTask.append(self.editMonth)
            newTask.append(self.editYear)
         if self.priority == "High":
             self.highList.append(newTask)
             self.top.destroy()
             return self.highList
         elif self.priority =="Low":
             self.lowList.append(newTask)

             self.top.destroy()
             return self.lowList
         else:
            messagebox.showerror("Error!!1!", "Oops something didn't work there, try again")

    def setup(self):
        left = tk.Button(self.master, text='<', command=self.go_prev, background='light gray') #go previous month
        self.wid.append(left)
        left.grid(row=0, column=1)
       
        header = tk.Label(self.master, height=2, text='{}   {}'.format(calendar.month_abbr[self.month], str(self.year)),background='light gray')
        self.wid.append(header)
        header.grid(row=0, column=2, columnspan=3,sticky=(N,W,S,E))
       
        right = tk.Button(self.master, text='>', command=self.go_next,background='light gray') # go next month
        self.wid.append(right)
        right.grid(row=0, column=5)
       
        days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] # days title overview
        for num, name in enumerate(days):
            t = tk.Label(self.master, text=name,background='light gray')
            self.wid.append(t)
            t.grid(row=1, column=num ,sticky=(N,W,S,E),padx=5,)
       
        for w, week in enumerate(self.cal.monthdayscalendar(self.year, self.month), 2):
            for d, day in enumerate(week):
                if day != 0:
                    b = tk.Button(self.master, width=5, text=day, command=lambda d1 = day:self.selection(d1))
                    self.wid.append(b)
                    b.grid(row=w, column=d,sticky=W,padx=5)
 
                   
    def clear(self):
        for w in self.wid[:]:
            w.grid_forget()
            #w.destroy()
            self.wid.remove(w)
   
    def go_prev(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1
        #self.selected = (self.month, self.year)
        self.clear()
        self.setup()

    def go_next(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1
        #self.selected = (self.month, self.year)
        self.clear()
        self.setup()
       
    def selection(self, day):
        self.day = day
        print(self.day, self.month, self.year)


    def YearOverview(self):
        year = calendar.TextCalendar(calendar.SUNDAY).formatyear(2016, 2, 1, 1, 2)
        print(year)

    def getViewDropDown(self):
        view = self.viewOptions.get()
        if view == "Day":
            self.viewAllDay()
        elif view == "Month":
            self.viewAllMonth()
        elif view == "Year":
            self.viewAllYear()
        elif view == "Low":
            self.viewAllLow()
        elif view == "High":
            self.viewAllHigh()
        elif view == "All":
            self.viewAllTasks()

    def getViewcOompletedDropDown(self):
        view = self.viewOptions.get()
        if view == "Day":
            self.viewCompeleDay()
        elif view == "Month":
            self.viewCompeleMonth()
        elif view == "Year":
            self.viewCompeleYear()
        elif view == "Low":
            self.viewCompeleLow()
        elif view == "High":
            self.viewCompeleHigh()
        elif view == "All":
            self.viewCompletedTasks()

    def getViewIncompleteDropDown(self):
        view = self.viewOptions.get()
        if view == "Day":
            self.viewIncompleteDay()
        elif view == "Month":
            self.viewIncompleteMonth()
        elif view == "Year":
            self.viewIncompleteYear()
        elif view == "Low":
            self.viewIncompleteLow()
        elif view == "High":
            self.viewIncompleteHigh()
        elif view == "All":
            self.viewIncompletedTasks()

    def viewAllDay(self):
        self.top = Toplevel(self.master)
        self.top.title("View Tasks - " + str(self.day) + "." +  str(self.month) + "." + str(self.year))
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[4] == self.day:
                if elem[5] == self.month:
                    if elem[6] == self.year:
                        date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                        self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[4] == self.day:
                if item[5] == self.month:
                    if item[6] == self.year:
                        date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                        self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewAllMonth(self):
        self.top = Toplevel(self.master)
        self.top.title("View All Tasks In A Month")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[6] == self.year:
                if elem[5] == self.month:
                    date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                    self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[6] == self.year:
                if item[5] == self.month:
                    date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                    self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewAllYear(self):
        self.top = Toplevel(self.master)
        self.top.title("View All Tasks In A Year")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[6] == self.year:
                date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[6] == self.year:
                date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewAllHigh(self):
        self.top = Toplevel(self.master)
        self.top.title("View All High Priority Tasks")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[6] == self.year:
                date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))

    def viewAllLow(self):
        self.top = Toplevel(self.master)
        self.top.title("View All Low Priority Tasks")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for item in self.lowList:
            if item[6] == self.year:
                date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewCompeleDay(self):
        self.top = Toplevel(self.master)
        self.top.title("View Complete Tasks - " + str(self.day) + "." +  str(self.month) + "." + str(self.year))
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[4] == self.day:
                if elem[5] == self.month:
                    if elem[6] == self.year:
                        if elem[3] == True:
                            date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                            self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[4] == self.day:
                if item[5] == self.month:
                    if item[6] == self.year:
                        if item[3] == True:
                            date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                            self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewCompeleMonth(self):
        self.top = Toplevel(self.master)
        self.top.title("View Complete Tasks In A Month")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[6] == self.year:
                if elem[5] == self.month:
                    if elem[3] == True:
                        date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                        self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[6] == self.year:
                if item[5] == self.month:
                    if item[3] == True:
                        date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                        self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewCompeleYear(self):
        self.top = Toplevel(self.master)
        self.top.title("View Complete Tasks In A year")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[6] == self.month:
                if elem[3] == True:
                    date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                    self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[6] == self.month:
                if item[3] == True:
                    date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                    self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewCompeleLow(self):
        self.top = Toplevel(self.master)
        self.top.title("View Complete Low Priority Tasks")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for item in self.lowList:
            if item[3] == True:
                date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewCompeleHigh(self):
        self.top = Toplevel(self.master)
        self.top.title("View Complete High Priority Tasks")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[3] == True:
                date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))

    def viewIncompleteHigh(self):
        self.top = Toplevel(self.master)
        self.top.title("View Incomplete High Priority Tasks")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[3] == False:
                date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))

    def viewIncompleteLow(self):
        self.top = Toplevel(self.master)
        self.top.title("View Incomplete Low Priority Tasks")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for item in self.lowList:
            if item[3] == False:
                date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewIncompleteYear(self):
        self.top = Toplevel(self.master)
        self.top.title("View Incomplete Tasks In A Yesr")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[6] == self.month:
                if elem[3] == False:
                    date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                    self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[6] == self.month:
                if item[3] == False:
                    date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                    self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewIncompleteMonth(self):
        self.top = Toplevel(self.master)
        self.top.title("View Incomplete Tasks In A Month")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[6] == self.year:
                if elem[5] == self.month:
                    if elem[3] == False:
                        date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                        self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[6] == self.year:
                if item[5] == self.month:
                    if item[3] == False:
                        date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                        self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewIncompleteDay(self):
        self.top = Toplevel(self.master)
        self.top.title("View Incomplete Tasks - " + str(self.day) + "." +  str(self.month) + "." + str(self.year))
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[4] == self.day:
                if elem[5] == self.month:
                    if elem[6] == self.year:
                        if elem[3] == False:
                            date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                            self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[4] == self.day:
                if item[5] == self.month:
                    if item[6] == self.year:
                        if item[3] == False:
                            date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                            self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewIncompletedTasks(self):
        self.top = Toplevel(self.master)
        self.top.title("View All Incomplete Tasks")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[3] == False:
                date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[3] == False:
                date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewCompletedTasks(self):
        self.top = Toplevel(self.master)
        self.top.title("View All Complete Tasks")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        for elem in self.highList:
            if elem[3] == True:
                date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
                self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],date))
        for item in self.lowList:
            if item[3] == True:
                date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
                self.tree.insert("","end",text = item[0], values=(item[1],item[2],date))

    def viewAllTasks(self):
        self.top = Toplevel(self.master)
        self.top.title("View All Incomplete Tasks")
        self.tree = ttk.Treeview(self.top)
        self.tree['columns'] = ("one","two", "three", "four")
        self.tree.heading("#0", text='Task Name', anchor='w')
        self.tree.heading("one", text="Priority:",anchor='w')
        self.tree.heading("two", text="Time Estimate:",anchor='w')
        self.tree.heading("three", text="Status:",anchor='w')
        self.tree.heading("four", text="Date:",anchor='w')
        self.tree.grid(row=4, column=4, rowspan=8)
        complete = ""
        for elem in self.highList:
            if elem[3] == True:
                complete = "Completed"
            else:
                complete = "Incompleted"
            date = str(elem[4]) + "." +  str(elem[5]) + "." + str(elem[6])
            self.tree.insert("","end",text = elem[0], values=(elem[1],elem[2],complete,date))
        for item in self.lowList:
            if item[3] == True:
                complete = "Completed"
            else:
                complete = "Incompleted"
            date = str(item[4]) + "." +  str(item[5]) + "." + str(item[6])
            self.tree.insert("",0,text = item[0], values=(item[1],item[2],complete,date))

def main():
    cal = toDoList()
    #root.mainloop()
  
if __name__ == "__main__":
    main()
