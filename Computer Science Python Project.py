import mysql.connector as mslc
db = mslc.connect(user = 'root', password = 'root', host = 'localhost')
pointer = db.cursor()

def database():
    
    pointer.execute("create database if not exists cs_project")
    pointer.execute("Use CS_Project")
    pointer.execute("Create Table if not exists Student(Name Varchar(30) Not Null, Admission_Number Integer(5) Primary Key, Date_of_Birth date, Class Integer(2), Section Varchar(1))")
    pointer.execute("Create Table if not exists Employee(Employee_Number Integer(5) Primary Key, Name Varchar(30), Job Varchar(30), Hiredate date)")
    pointer.execute("Create Table if not exists Fee(Admission_Number Integer(5) Primary Key, Fee Integer(5), Month Varchar(30))")
    pointer.execute("Create Table if not exists Exam(Admission_Number Integer(5) Primary Key, Name Varchar(30), Class Integer(2), Section Varchar(1), Percentage Decimal(4,2), Marks Integer(3))")


def display1():
    pointer.execute("Select * From Student")
    List = list(pointer)
    for i in range(len(List)):
        Name = List[i][0]
        Admission_Number = List[i][1]
        DOB = List[i][2]
        Class = List[i][3]
        Section = List[i][4]
        Result = "Name = %s, Admission_Number = %d, DOB = %s, Class = %s, Section = %s"%(Name, Admission_Number, DOB, Class, Section)
        print(i + 1, ")", Result)


def insert1():
    ans = "y"
    while ans == "y" or ans == "Y":
        Name = input("\nEnter Student Name - ")
        Admission_Number = int(input("Enter Admission No - "))
        DOB = input("Enter Date of Birth [Correct form : yyyy-mm-dd] - ")
        Class = int(input("Enter Class for Admission - "))
        Section = input("Enter Section - ")
        pointer.execute("Insert Into Student Values('%s' ,'%d', '%s', '%s', '%s')"%(Name, Admission_Number, DOB, Class, Section))
        db.commit()
        ans = input("Do you want to enter more records [y/n] - ")
  

def update1():
    ans = "y"
    while ans == "y" or ans == "Y":
        Number = int(input("\nSelect student by using its admission number - "))
        Query = input("What do you want to update? [(a) Name or (b) Admission_Number or (c) Date_of_Birth or (d) Class or (e) Section] - ")
        New_Data = input("\nEnter new %s - "%Query)
        pointer.execute("Update Student Set %s = '%s' Where Admission_Number = '%d'" % (Query, New_Data, Number))
        db.commit()
        print("Data of Admission Number", Number, "Updated Successfully !!")
        ans = input("Do you want to update more records? [y/n] - ")


def delete1():
    ans = "y"
    while ans == "y" or ans == "Y":
        Query = input("\nSelect student by using its admission number whose data you want to delete - ")
        pointer.execute("Delete From Student Where Admission_Number = '%s'"% Query)
        db.commit()
        print("Data of Admission Number", Query, "Deleted Successfully !!")
        ans = input("Do you want to delete more records [y/n] - ")


def display2(): 
        pointer.execute("Select * From Employee")
        List = list(pointer)
        for i in range(len(List)):
            Employee_Number = List[i][0]
            Name = List[i][1]
            Job = List[i][2]
            Hiredate = List[i][3]
            Result = "Employee_Number = %d, Name = %s, Job = %s, Hiredate = %s" % (Employee_Number, Name, Job, Hiredate)
            print(i + 1, ")", Result)


def insert2():
    ans = "y"
    while ans == "y" or ans == "Y":
        Employee_Number = int(input("\nEnter Employee No : "))
        Name = input("Enter Employee Name - ")
        Job = input("Enter Designation - ")
        Hiredate = input("Enter date of joining [Correct form : yyyy-mm-dd] - ")
        pointer.execute("Insert Into Employee Values('%d', '%s', '%s', '%s')"%(Employee_Number, Name, Job, Hiredate))
        db.commit()
        ans = input("Do you want to enter more records [y/n] - ")


def update2():
    ans = "y"
    while ans == "y" or ans=="Y":
        Number = int(input("\nSelect employee by using its employee number - "))
        Query = input("What do you want to update? [(a) Employee_Number or (b) Name or (c) Job or (d) Hiredate] - ")
        New_Data = input("\nEnter new %s - "%Query)
        pointer.execute("Update Employee Set %s = '%s' Where Employee_Number = '%d'" % (Query, New_Data, Number))
        db.commit()
        print("Data of Employee Number", Number, "Updated Successfully !!")
        ans = input("Do you want to update more records? [y/n] - ")


def delete2():
    ans = "y"
    while ans == "y"or ans == "Y":
        Query = input("\nSelect employee by using its employee number whose data you want to delete - ")
        pointer.execute("Delete From Employee Where Employee_Number = '%s'"% Query)
        db.commit()
        print("Data of Employee Number", Query, "Deleted Successfully !!")
        ans = input("Do you want to delete more records [y/n] - ")


def display3(): 
    pointer.execute("Select * From Fee")
    List = list(pointer)
    for i in range(len(List)):
        Admission_Number = List[i][0]
        Fee = List[i][1]
        Month = List[i][2]
        Result = "Admission_Number = %d, Fee = %d, Month = %s"%(Admission_Number, Fee, Month)
        print(i + 1, ")", Result)


def insert3():
    ans = "y"
    while ans == "y" or ans == "Y":
        Admission_Number = int(input("\nEnter Admission Number - "))
        Fee = float(input("Enter Fee Amount - "))
        Month = input("Enter Month: ")
        pointer.execute("Insert Into Fee Values('%d','%d','%s')"%(Admission_Number, Fee, Month))
        db.commit()
        ans = input("Do you want to enter more records [y/n] - ")


def update3(): 
    ans = "y"
    while ans == "y" or ans == "Y":
        Number = int(input("\nSelect student by using its admission number - "))
        Query = input("What do you want to update? [(a) Admission_Number or (b) Fee or (c) Month] - ")
        New_Data = input("\nEnter new %s - "%Query)
        pointer.execute("Update Fee Set %s = '%s' Where Admission_Number = '%d'"%(Query, New_Data, Number))
        db.commit()
        print("Data of Admission Number", Number, "Updated Successfully !!")
        ans = input("Do you want to update more records? [y/n] - ")


def delete3():
    ans = "y"
    while ans == "y" or ans == "Y":
        Query = input("\nSelect student by using its admission number whose data you want to delete - ")
        pointer.execute("Delete From Fee Where Admission_Number = '%s'"% Query)
        db.commit()
        print("Data of Admission Number", Query, "Deleted Successfully !!")
        ans = input("Do you want to delete more records [y/n] - ")
        


def display4():
    pointer.execute("Select * From Exam")
    List = list(pointer)
    for i in range(len(List)):
        Admission_Number = List[i][0]
        Name = List[i][1]
        Class = List[i][2]
        Section = List[i][3]
        Percentage = List[i][4]
        Marks = List[i][5]
        Result = "Admission_Number = %d, Name = %s, Class = %s, Section = %s, Percentage = %s, Marks = %s"%( Admission_Number, Name, Class, Section, Percentage, Marks)
        print(i + 1, ")", Result)
    

def insert4():
    ans = "y"
    while ans == "y" or ans == "Y":
        Admission_Number = int(input("\nEnter Admission No - "))
        Name = input("Enter Student Name - ")
        Class = int(input("Enter Class - "))
        Section = input("Enter Section - ")
        Percentage = float(input("Enter Percentage - "))
        Marks = int(input("Enter Total Marks - "))
        pointer.execute("Insert Into Exam Values('%d' ,'%s', '%s', '%s', '%s', '%s')"%(Admission_Number, Name, Class, Section, Percentage, Marks))
        db.commit()
        ans = input("Do you want to enter more records [y/n] - ")


def update4():
    ans = "y"
    while ans == "y" or ans == "Y":
        Number = int(input("\nSelect student by using its admission number - "))
        Query = input("What do you want to update? [(a) Admission_Number or (b) Name or (c) Class or (d) Section or (e) Percentage or (f) Marks] - ")
        New_Data = input("\nEnter new %s - "%Query)
        pointer.execute("Update Exam Set %s = '%s' Where Admission_Number = '%d'" % (Query, New_Data, Number))
        db.commit()
        print("Data of Admission Number", Number, "Updated Successfully !!")
        ans = input("Do you want to update more records? [y/n] - ")
    

def delete4():
    ans = "y"
    while ans == "y" or ans == "Y":
        Query = input("\nSelect student by using its admission number whose data you want to delete - ")
        pointer.execute("Delete From Exam Where Admission_Number = '%s'"% Query)
        db.commit()
        print("Data of Admission Number", Query, "Deleted Successfully !!")
        ans = input("Do you want to delete more records [y/n] - ")
    

def selection():

    database()   
    
    ans = "y"
    while ans == "y" or ans == "Y":
        print('-----------------------------------\nWELCOME TO SCHOOL MANAGEMENT SYSTEM\n-----------------------------------')
        print("1.STUDENT MANAGEMENT")
        print("2.EMPLOYEE MANAGEMENT")
        print("3.FEE MANAGEMENT")
        print("4.EXAM MANAGEMENT")
        ch = int(input("\nEnter ur choice ['1' or '2' or '3' or '4'] - "))
        if ch == 1:
            ans = "n"
            while ans == "n" or ans == "N":
                print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
                print('a.NEW ADMISSION')
                print('b.UPDATE STUDENT DETAILS')
                print("c.DELETE STUDENT'S DATA")
                c = input("\nEnter your choice ['a' or 'b' or 'c'] - ")
                print('\nInitially the details are...\n')
                display1()
                if c == 'a':
                    insert1()
                    print('\nModified details are...\n')
                    display1()
                elif c == 'b':
                    update1()
                    print('\nModified details are...\n')
                    display1()
                elif c == 'c':
                    delete1()
                    print('\nModified details are...\n')
                    display1()
                else:
                    print('Enter correct choice...!!')
                ans = input("Do you want to exit STUDENT MANAGEMENT [y/n] - ")
        elif ch == 2:
            ans = "n"
            while ans == "n" or ans == "N":
                print('\nWELCOME TO EMPLOYEE MANAGEMENT SYSTEM\n')
                print('a.NEW EMPLOYEE')
                print('b.UPDATE STAFF DETAILS')
                print("c.DELETE EMPLOYEE'S DATA")
                c = input("\nEnter your choice ['a' or 'b' or 'c'] - ")
                print('\nInitially the details are...\n')
                display2()
                if c == 'a':
                    insert2()
                    print('\nModified details are...\n')
                    display2()
                elif c == 'b':
                    update2()
                    print('\nModified details are...\n')
                    display2()
                elif c == 'c':
                    delete2()
                    print('\nModified details are...\n')
                    display2()
                else:
                    print('Enter correct choice...!!')
                ans = input("Do you want to exit EMPLOYEE MANAGEMENT [y/n] - ")
        elif ch == 3:
            ans = "n"
            while ans == "n" or ans == "N":
                print('WELCOME TO FEE MANAGEMENT SYSTEM')
                print('a.NEW FEE')
                print('b.UPDATE FEE')
                print('c.EXEMPT FEE')
                c = input("\nEnter your choice ['a' or 'b' or 'c'] - ")
                print('\nInitially the details are...\n')
                display3()
                if c == 'a':
                    insert3()
                    print('\nModified details are...\n')
                    display3()
                elif c == 'b':
                    update3()
                    print('\nModified details are...\n')
                    display3()
                elif c == 'c':
                    delete3()
                    print('\nModified details are...\n')
                    display3()
                else:
                    print('Enter correct choice...!!')
                ans = input("Do you want to exit FEE MANAGEMENT [y/n] - ")
        elif ch == 4:
            ans = "n"
            while ans == "n" or ans == "N":
                print('WELCOME TO EXAM MANAGEMENT SYSTEM')
                print('a.EXAM DETAILS')
                print('b.UPDATE DETAILS ')
                print('c.DELETE DETAILS')
                c = input("\nEnter your choice ['a' or 'b' or 'c'] - ")
                print('\nInitially the details are...\n')
                display4()
                if c == 'a':
                    insert4()
                    print('\nModified details are...\n')
                    display4()
                elif c == 'b':
                    update4()
                    print('\nModified details are...\n')
                    display4()
                elif c == 'c':
                    delete4()
                    print('\nModified details are...\n')
                    display4()
                else:
                    print('Enter correct choice...!!')
                ans = input("Do you want to exit EXAM MANAGEMENT [y/n] - ")
        else:
            print('Enter correct choice..!!')

        ans = input("Do you want to Repeat SCHOOL MANAGEMENT SYSTEM ? [y/n] - ")


selection()
