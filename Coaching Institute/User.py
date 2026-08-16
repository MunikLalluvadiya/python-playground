import csv
import datetime
import os

class user:

    def __init__(self,User_ID,User_Name,Email,Password,Role):
        self.User_ID = User_ID
        self.User_Name = User_Name
        self.Email = Email
        self.Password = Password
        self.Role = Role

    

    @classmethod
    def Take_Input(cls):
        User_ID = int(input("Enter User_ID : "))
        User_Name = (input("Enter User_Name : "))
        Email = (input("Enter Email : "))
        Password = (input("Enter Password : "))
        Role = (input("Enter Role : "))

        return User_ID,User_Name,Email,Password,Role
    
    
    def Register(self):
        with open("User.csv","a",newline="")as file:
            writer = csv.writer(file)

            if (os.path.getsize("User.csv") <= 0):
                writer.writerow(["User_ID","User_Name","Email","Password","Role"]) 

            writer.writerow([self.User_ID,self.User_Name,self.Email,self.Password,self.Role])
            print(" Registed Sucsessful.")

    @staticmethod
    def Login():
        Email_Inp = input(" Enter Your Email : ")
        is_true = True

        with open("User.csv","r")as file:
            dictreader = csv.DictReader(file)

            for deta in dictreader:
                if deta["Email"]== Email_Inp :
                    is_true = False

                    Password_inp = input(" Enter Password : ")
                    if deta["Password"]==Password_inp:
                        print(" Login Sucssesfull... ")

                        if deta["Role"].lower()=="admin":
                            return admin(deta["User_ID"],deta["User_Name"],deta["Email"],deta["Password"],deta["Role"])
                        elif deta["Role"].lower()=="teacher":
                            return teacher(deta["User_ID"],deta["User_Name"],deta["Email"],deta["Password"],deta["Role"])
                        else:
                            return student(deta["User_ID"],deta["User_Name"],deta["Email"],deta["Password"],deta["Role"])

                    else:
                        print(" Incorect Password...")
                        return
            if is_true:
                print(" Incorect Email...")
                return

    @staticmethod
    def view_courses():
        with open("Courses.csv","r") as file:
                
            reader = csv.DictReader(file)
            for deta in reader:
                if deta["Status"].lower() == "approved":
                    for key,vel in deta.items():
                        print(key,":",vel)
                    print("----------------")
                else:
                    continue

class admin(user):
    def __init__(self, User_ID, User_Name, Email, Password, Role="admin"):
        super().__init__( User_ID, User_Name, Email, Password, Role)

    def View_All_Users(self):

        with open("User.csv","r") as file:
            reader = csv.DictReader(file)
            for deta in reader :
                for key,vel in deta.items():
                    print(key,":",vel)
                print("--------------")

    def View_Pending_Courses(self):

        found = True
        with open("Courses.csv","r") as file:
            reader = csv.DictReader(file)
            for deta in reader:
                if deta["Status"].lower() == "pending":
                    found = False
                    for key,vel in deta.items():
                        print(key,":",vel)
                    print("----------------")
                 
                else:
                    continue
        if found:
            print("-----------------")
            print(" No Deta Found. ")
            print("-----------------")

    def Approve_And_Reject_Course(self):
        Course_ID = (input(" Enter Course ID : "))
        found = True
        Tem_Deta = []

        with open("Courses.csv","r") as file:
            reader = csv.reader(file)
            for deta in reader:
                if Course_ID == deta[0]:
                    found = False
                    Appruvel = input(" Enter Approve(Y) and Rejected(N) : ")
                    if Appruvel == "Y":
                        deta[-1] = "Approved"
                    else:
                        deta[-1] = "Rejected"
                Tem_Deta.append(deta)

        if not found:
            with open("Courses.csv","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerows(Tem_Deta)
                print(" Data Updeted. ")
        
        if found:
            print(" No Data Found. ")

          

                    




    

class teacher(user):
    def __init__(self, User_ID, User_Name, Email, Password, Role="teacher"):
        super().__init__( User_ID, User_Name, Email, Password, Role)

    def add_Courses(self):
        Course_ID = int(input(" Enter Course ID :"))
        Course_Name = input(" Enter Course Name :")
        Duration = input(" Enter Duration :")
        Fee = int(input(" Enter Fees :")) 
        Status = "pending"

        Add_Course = [Course_ID,Course_Name,Duration,Fee]
        List_Topic = []
        while True:
            Description = input(" Do You Want To Add Topic.:")
            if Description in ("Yes","y","Y","yes"):
                Topic = input(" Enter Topic :")
                List_Topic.append(Topic)
            else:
                print(" Topics Added Sucsessfully...")
                break
        joined = ";".join(List_Topic)
        Add_Course.append(joined)
        Add_Course.append(Status)
        


        with open("Courses.csv","a",newline="")as file:
            writer = csv.writer(file)

            if (os.path.getsize("Courses.csv") <= 0):
                writer.writerow(["Course_ID","Course_Name","Duration","Fee","Topics","Status"]) 

            writer.writerow(Add_Course)
        print(" Course Added Sucsessfull. ")


    def Check_Student_Attendance(self):
        student_Name = (input(" Enter Student Name : "))
        found = True
        with open("Enrollment.csv","r")as file:
            reader = csv.DictReader(file)

            for deta in  reader: 
                if deta["Student_Name"] == student_Name:
                    found = False
                    Check_Att = 0 # present day
                    dete_of_enroll_temp = deta["Enrollment_Date"]
                    dete_of_enroll = datetime.date.fromisoformat(dete_of_enroll_temp)
                    Total_Deys = datetime.date.today() - dete_of_enroll

                    with open("Attendance.csv","r")as file_2:
                        reader_2 = csv.DictReader(file_2)

                        for deta_2 in reader_2:
                            if deta_2["User_Name"] == student_Name:
                                Check_Att += 1
                    print("----------------------")
                    print(f" Student Name : {deta["Student_Name"]} \n Total Deys : {Total_Deys.days} \n Present Days : {Check_Att} \n Date Of Enroll : {dete_of_enroll}")
                    print("----------------------")

            if found:
                
                print(" Student Not Found.")
                            






class student(user):
    def __init__(self, User_ID, User_Name, Email, Password, Role="student"):
        super().__init__( User_ID, User_Name, Email, Password, Role)

    def Attendance(self):
        with open("Attendance.csv","a",newline="")as file:
            writer = csv.writer(file)
            writer.writerow([ self.User_ID, self.User_Name, self.Email, datetime.date.today(),"Present"])
        print(" Thenkyou For Coming...")

    def Enroll_In_Course(self):
        Course_ID = (input(" Enter Course ID : "))
        Found = True
        with open("Courses.csv","r")as file:
            reader = csv.reader(file)
            first = next(file)

            for deta in reader:
                    if Course_ID == deta[0]:
                        Found = False
    
                        with open("Enrollment.csv","a",newline="")as file:
                            writer = csv.writer(file)
                        
                            if (os.path.getsize("Enrollment.csv") <= 0):
                                writer.writerow(["Student_ID","Student_Name","Course_ID","Course_Name","Enrollment_Date"]) 
                        
                            writer.writerow([ self.User_ID,self.User_Name,Course_ID,deta[1],datetime.date.today()])
                    
                        print(" Enroll Sucsessfull.")
                        break
                    
            if Found:
                print(" No Course Found. ")
                    





    



