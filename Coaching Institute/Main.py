from User import user,admin,teacher,student

def student_inst(logged_user):
    student_Deshbord = """
1 => Attendance
2 => View Courses
0 => Log Out
""" 
    while True:

        print(student_Deshbord)  
        Std_Choice = int(input(" Enter Your Choice : ")) 

        if Std_Choice == 1:
            logged_user.Attendance()
        elif Std_Choice == 2:
            logged_user.view_courses()
        elif Std_Choice == 0:
            break


def teacher_inst(logged_user):
    Teacher_Deshbord = """
1 => add_Courses 
2 => View Courses
0 => Log Out
""" 
    while  True:
        print(Teacher_Deshbord)  
        Teacher_Choice = int(input(" Enter Your Choice : "))  

        if Teacher_Choice == 1:
            logged_user.add_Courses()
        elif Teacher_Choice == 2:
            logged_user.view_courses()
        elif Teacher_Choice == 0:
            break


def admin_inst(logged_user):
    Admin_Deshbord = """
1 => View_All_Users 
2 => View Courses
0 => Log Out
""" 
    while True:
        print(Admin_Deshbord)
        Admin_Choice = int(input(" Enter Your Choice : "))  

        if Admin_Choice == 1:
            logged_user.View_All_Users()   
        elif Admin_Choice == 2:
            logged_user.view_courses()
        elif Admin_Choice == 0:
            break





while True:
    Deta_Deshbord = """
1 => Register
2 => Login
0 => Exit
"""

    print(Deta_Deshbord)
    Choice = int(input(" Enter Your Choice : "))

    if Choice == 1:
        User_ID,User_Name,Email,Password,Role = user.Take_Input()

        if Role.lower() == "student":
            user1 = student(User_ID,User_Name,Email,Password,Role)
        elif Role.lower() == "teacher":
            user1 = teacher(User_ID,User_Name,Email,Password,Role)
        elif Role.lower() == "admin":
            user1 = admin(User_ID,User_Name,Email,Password,Role)
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
    