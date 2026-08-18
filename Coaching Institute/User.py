import csv
import datetime
import os

class user:

    def __init__(self, User_ID, User_Name, Email, Password, Role):
        self.User_ID = User_ID
        self.User_Name = User_Name
        self.Email = Email
        self.Password = Password
        self.Role = Role

    @classmethod
    def Take_Input(cls):
        User_ID = int(input("Enter User_ID : "))
        User_Name = input("Enter User_Name : ")
        Email = input("Enter Email : ")
        Password = input("Enter Password : ")
        Role = input("Enter Role : ")
        return User_ID, User_Name, Email, Password, Role

    def Register(self):
        with open("User.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if os.path.getsize("User.csv") <= 0:
                writer.writerow(["User_ID", "User_Name", "Email", "Password", "Role"])
            writer.writerow([self.User_ID, self.User_Name, self.Email, self.Password, self.Role])
        print(" Registed Sucsessful.")

    @staticmethod
    def Login():
        Email_Inp = input(" Enter Your Email : ")
        is_true = True

        with open("User.csv", "r") as file:
            dictreader = csv.DictReader(file)
            for deta in dictreader:
                if deta["Email"] == Email_Inp:
                    is_true = False
                    Password_inp = input(" Enter Password : ")
                    if deta["Password"] == Password_inp:
                        print(" Login Sucssesfull... ")
                        if deta["Role"].lower() == "admin":
                            return admin(deta["User_ID"], deta["User_Name"], deta["Email"], deta["Password"], deta["Role"])
                        elif deta["Role"].lower() == "teacher":
                            return teacher(deta["User_ID"], deta["User_Name"], deta["Email"], deta["Password"], deta["Role"])
                        else:
                            return student(deta["User_ID"], deta["User_Name"], deta["Email"], deta["Password"], deta["Role"])
                    else:
                        print(" Incorect Password...")
                        return
            if is_true:
                print(" Incorect Email...")
                return

    @staticmethod
    def view_courses():
        with open("Courses.csv", "r") as file:
            reader = csv.DictReader(file)
            for deta in reader:
                if deta["Status"].lower() == "approved":
                    for key, vel in deta.items():
                        print(key, ":", vel)
                    print("----------------")


class admin(user):
    def __init__(self, User_ID, User_Name, Email, Password, Role="admin"):
        super().__init__(User_ID, User_Name, Email, Password, Role)

    def View_All_Users(self):
        with open("User.csv", "r") as file:
            reader = csv.DictReader(file)
            for deta in reader:
                for key, vel in deta.items():
                    print(key, ":", vel)
                print("--------------")

    def View_Pending_Courses(self):
        found = True
        with open("Courses.csv", "r") as file:
            reader = csv.DictReader(file)
            for deta in reader:
                if deta["Status"].lower() == "pending":
                    found = False
                    for key, vel in deta.items():
                        print(key, ":", vel)
                    print("----------------")
        if found:
            print("-----------------")
            print(" No Deta Found. ")
            print("-----------------")

    def Approve_And_Reject_Course(self):
        Course_ID = input(" Enter Course ID : ")
        found = True
        Tem_Deta = []

        with open("Courses.csv", "r") as file:
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
            with open("Courses.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(Tem_Deta)
            print(" Data Updeted. ")

        if found:
            print(" No Data Found. ")

    def View_All_Payments(self):
        with open("Payment.csv", "r") as file:
            reader = csv.DictReader(file)
            for deta in reader:
                for key, vel in deta.items():
                    print(key, ":", vel)
                print("----------------")


class teacher(user):
    def __init__(self, User_ID, User_Name, Email, Password, Role="teacher"):
        super().__init__(User_ID, User_Name, Email, Password, Role)

    def add_Courses(self):
        Course_ID = int(input(" Enter Course ID :"))
        Course_Name = input(" Enter Course Name :")
        Duration = input(" Enter Duration :")
        Fee = int(input(" Enter Fees :"))
        Status = "Pending"

        Add_Course = [Course_ID, Course_Name, Duration, Fee]
        List_Topic = []
        while True:
            Description = input(" Do You Want To Add Topic.:")
            if Description in ("Yes", "y", "Y", "yes"):
                Topic = input(" Enter Topic :")
                List_Topic.append(Topic)
            else:
                print(" Topics Added Sucsessfully...")
                break
        joined = ";".join(List_Topic)
        Add_Course.append(joined)
        Add_Course.append(Status)

        with open("Courses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if os.path.getsize("Courses.csv") <= 0:
                writer.writerow(["Course_ID", "Course_Name", "Duration", "Fee", "Topics", "Status"])
            writer.writerow(Add_Course)
        print(" Course Added Sucsessfull. ")

    def Check_Student_Attendance(self):
        student_Name = input(" Enter Student Name : ")
        found = True
        with open("Enrollment.csv", "r") as file:
            reader = csv.DictReader(file)
            for deta in reader:
                if deta["Student_Name"] == student_Name:
                    found = False
                    Check_Att = 0
                    dete_of_enroll = datetime.date.fromisoformat(deta["Enrollment_Date"])
                    Total_Deys = datetime.date.today() - dete_of_enroll

                    with open("Attendance.csv", "r") as file_2:
                        reader_2 = csv.DictReader(file_2)
                        for deta_2 in reader_2:
                            if deta_2["User_Name"] == student_Name:
                                Check_Att += 1

                    print(f" Student Name : {student_Name} \n Total Deys : {Total_Deys.days} \n Present Days : {Check_Att}")

            if found:
                print(" Student Not Found.")


class student(user):
    def __init__(self, User_ID, User_Name, Email, Password, Role="student"):
        super().__init__(User_ID, User_Name, Email, Password, Role)

    def Attendance(self):
        with open("Attendance.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.User_ID, self.User_Name, self.Email, datetime.date.today(), "Present"])
        print(" Thenkyou For Coming...")

    def Enroll_In_Course(self):
        Course_ID = input(" Enter Course ID : ")
        Found = True
        with open("Courses.csv", "r") as file:
            reader = csv.reader(file)
            next(file)

            for deta in reader:
                if Course_ID == deta[0]:
                    Found = False

                    with open("Enrollment.csv", "a", newline="") as file2:
                        writer = csv.writer(file2)
                        if os.path.getsize("Enrollment.csv") <= 0:
                            writer.writerow(["Student_ID", "Student_Name", "Course_ID", "Course_Name", "Enrollment_Date"])
                        writer.writerow([self.User_ID, self.User_Name, Course_ID, deta[1], datetime.date.today()])

                    Course_Fee = deta[3]
                    with open("Payment.csv", "a", newline="") as file3:
                        writer = csv.writer(file3)
                        if os.path.getsize("Payment.csv") <= 0:
                            writer.writerow(["Student_ID", "Student_Name", "Course_ID", "Course_Name", "Amount_Due", "Amount_Paid", "Status", "Payment_Date"])
                        writer.writerow([self.User_ID, self.User_Name, Course_ID, deta[1], Course_Fee, 0, "Pending", "-"])

                    print(" Enroll Sucsessfull.")
                    break

            if Found:
                print(" No Course Found. ")

    def Make_Payment(self):
        Course_ID = input(" Enter Course ID : ")
        Amount = int(input(" Enter Amount To Pay : "))
        found = True
        Tem_Deta = []

        with open("Payment.csv", "r") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for deta in reader:
                if deta["Course_ID"] == Course_ID and deta["Student_ID"] == self.User_ID:
                    found = False
                    New_Paid = int(deta["Amount_Paid"]) + Amount
                    deta["Amount_Paid"] = New_Paid
                    if New_Paid >= int(deta["Amount_Due"]):
                        deta["Status"] = "Paid"
                    else:
                        deta["Status"] = "Pending"
                    deta["Payment_Date"] = datetime.date.today()
                Tem_Deta.append(deta)

        if not found:
            with open("Payment.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(Tem_Deta)
            print(" Payment Sucsessfull. ")

        if found:
            print(" No Enrollment Found For This Course. ")

    def View_My_Fee_Status(self):
        found = True
        with open("Payment.csv", "r") as file:
            reader = csv.DictReader(file)
            for deta in reader:
                if deta["Student_ID"] == self.User_ID:
                    found = False
                    for key, vel in deta.items():
                        print(key, ":", vel)
                    print("----------------")
        if found:
            print(" No Payment Records Found. ")