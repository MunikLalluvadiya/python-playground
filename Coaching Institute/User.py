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
                for key,vel in deta.items():
                    print(key,":",vel)
                print("----------------")

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
                 

    

class teacher(user):
    def __init__(self, User_ID, User_Name, Email, Password, Role="teacher"):
        super().__init__( User_ID, User_Name, Email, Password, Role)

    def add_Courses(self):
        Course_ID = int(input(" Enter Course ID :"))
        Course_Name = input(" Enter Course Name :")
        Duration = input(" Enter Duration :")
        Fee = int(input(" Enter Fees :")) 

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


        with open("Course.csv","a",newline="")as file:
            writer = csv.writer(file)

            if (os.path.getsize("Course.csv") <= 0):
                writer.writerow(["Course_ID","Course_Name","Duration","Fee","Topics"]) 

            writer.writerow(Add_Course)
        print(" Course Added Sucsessfull. ")


class student(user):
    def __init__(self, User_ID, User_Name, Email, Password, Role="student"):
        super().__init__( User_ID, User_Name, Email, Password, Role)

    def Attendance(self):
        with open("Attendance.csv","a",newline="")as file:
            writer = csv.writer(file)
            writer.writerow([ self.User_ID, self.User_Name, self.Email, datetime.date.today(),"Present"])
        print(" Thenkyou For Coming...")





    



