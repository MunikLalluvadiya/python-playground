from User import user,admin,teacher,student

def student_inst(logged_user):
    student_Deshbord = """
-------Student--------
1 => Attendance
2 => View Courses
3 => Enroll In Course
0 => Log Out
----------------------
""" 
    while True:

        print(student_Deshbord)  
        print("--------------------------------------")
        Std_Choice = int(input(" Enter Your Choice : ")) 
        print("--------------------------------------")

        if Std_Choice == 1:
            logged_user.Attendance()
        elif Std_Choice == 2:
            logged_user.view_courses()
        elif Std_Choice == 3:
            logged_user.Enroll_In_Course()
        elif Std_Choice == 0:
            break


def teacher_inst(logged_user):
    Teacher_Deshbord = """
----------Teacher------------
1 => add_Courses 
2 => View Courses
3 => Check Student Attendance
0 => Log Out
-----------------------------
""" 
    while  True:
        print(Teacher_Deshbord)  
        print("------------------------------------------")
        Teacher_Choice = int(input(" Enter Your Choice : "))  
        print("------------------------------------------")

        if Teacher_Choice == 1:
            logged_user.add_Courses()
        elif Teacher_Choice == 2:
            logged_user.view_courses()
        elif Teacher_Choice == 3:
            logged_user.Check_Student_Attendance()
        elif Teacher_Choice == 0:
            break


def admin_inst(logged_user):
    Admin_Deshbord = """
-------Admin--------
1 => View_All_Users 
2 => View Courses
3 => View Pending Courses
4 => Approve And Reject Course
0 => Log Out
--------------------
""" 
    while True:
        print(Admin_Deshbord)
        print("-----------------------------------------")
        Admin_Choice = int(input(" Enter Your Choice : "))  
        print("-----------------------------------------")

        if Admin_Choice == 1:
            logged_user.View_All_Users()   
        elif Admin_Choice == 2:
            logged_user.view_courses()
        elif Admin_Choice == 3:
            logged_user.View_Pending_Courses()
        elif Admin_Choice == 4:
            logged_user.Approve_And_Reject_Course()
        elif Admin_Choice == 0:
            break





while True:
    Deta_Deshbord = """
--------------
1 => Register
2 => Login
0 => Exit
--------------
"""

    print(Deta_Deshbord)
    Choice = int(input(" Enter Your Choice : "))

    if Choice == 1:
        User_ID,User_Name,Email,Password,Role = user.Take_Input()

        if Role.lower()  == "student":
            user1 = student(User_ID,User_Name,Email,Password,Role.lower())
        elif Role.lower()  == "teacher":
            user1 = teacher(User_ID,User_Name,Email,Password,Role.lower())
        elif Role.lower()  == "admin":
            user1 = admin(User_ID,User_Name,Email,Password,Role.lower())
        else:
            print(" Invalid Role.")
            continue

        user1.Register()

        if isinstance(user1, student):
            student_inst(user1)
        elif isinstance(user1, teacher):
            teacher_inst(user1)
        elif isinstance(user1, admin):
            admin_inst(user1)


    elif Choice == 2:
        Student_Login = user.Login()  #obj of login
        if Student_Login is None:
            print(" Login Faild Try Again. ")

        if isinstance(Student_Login, student):
            student_inst(Student_Login)
        elif isinstance(Student_Login, teacher):
            teacher_inst(Student_Login)
        elif isinstance(Student_Login, admin):
            admin_inst(Student_Login)


    elif Choice == 0:
        break
    