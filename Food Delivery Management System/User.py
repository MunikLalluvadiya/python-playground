import csv

class User:

    def Register(self):
        self.User_Id = int(input(" Enter Your User Id : "))
        self.Name = input(" Enter Your Name : ")
        self.Phone_Number = int(input(" Enter Your Phone Number : "))
        self.Email = input(" Enter Your Email : ")
        self.Address = input(" Enter Your Address : ")
        self.Password = input(" Enter Your Password : ")

        # write a header row the very first time user.csv is created
        write_header = True
        with open("user.csv", "r", newline="") as file:
            if file.readline().strip() != "":
                write_header = False

        User_Data = [self.User_Id, self.Name, self.Phone_Number, self.Email, self.Address, self.Password]

        with open("user.csv", "a", newline="") as file:
            Writer = csv.writer(file)
            if write_header:
                Writer.writerow(["User_Id", "Name", "Phone_Number", "Email", "Address", "Password"])
            Writer.writerow(User_Data)

        print(" Registered Successfully.")

    def Login(self):
        with open("user.csv", "r", newline="") as file:
            Reader = csv.reader(file)
            next(Reader, None)  # skip header row
            self.Email = input(" Enter Your Email : ")
            is_Email = True
            login_success = False
            for Read in Reader:
                if Read[3] == self.Email:
                    is_Email = False
                    self.Password = input(" Enter Your Password : ")
                    if Read[5] == self.Password:
                        self.User_Id = Read[0]
                        self.Name = Read[1]
                        self.Phone_Number = Read[2]
                        self.Address = Read[4]
                        print(" Login Sucsessfull. ")
                        login_success = True
                    else:
                        print(" Incorect Password.")
                    break
            if is_Email:
                print(" You Are Not Registed User. Please Register First.")
            return login_success

    def View_Profile(self):
        with open("user.csv", "r", newline="") as file:
            Dict_Reader = csv.DictReader(file)
            User_Id_check = input(" Enter User Id : ")
            is_true = True
            for deta in Dict_Reader:
                if deta["User_Id"] == User_Id_check:
                    is_true = False
                    for key, vel in deta.items():
                        if key == "Password":
                            continue
                        else:
                            print(key, ":", vel)
                    break
            if is_true:
                print(" There Is NO User With This Id. ")

    def Update_Profile(self):
        Users_Deta = []
        is_valid = False
        with open("user.csv", "r", newline="") as file:
            first_copy = next(file).rstrip("\r\n")
            first = first_copy.split(",")

            Reader = csv.reader(file)
            self.Email = input(" Enter Your Email : ")
            is_Email = True
            for Read in Reader:
                if Read[3] == self.Email:
                    is_Email = False
                    self.Password = input(" Enter Your Password : ")
                    if Read[5] == self.Password:
                        new_updates = input(" What whoud you change : ")

                        if new_updates == first[1]:
                            new_name = input(" Enter New Name : ")
                            Read[1] = new_name
                            Users_Deta.append(Read)
                            is_valid = True

                        elif new_updates == first[2]:
                            new_Phone_Number = input(" Enter New Phone Number : ")
                            Read[2] = new_Phone_Number
                            Users_Deta.append(Read)
                            is_valid = True

                        elif new_updates == first[3]:
                            new_Email = input(" Enter New Email : ")
                            Read[3] = new_Email
                            Users_Deta.append(Read)
                            is_valid = True

                        elif new_updates == first[4]:
                            new_Address = input(" Enter New Address : ")
                            Read[4] = new_Address
                            Users_Deta.append(Read)
                            is_valid = True

                        else:
                            print(" You Dont Change IT. ")

                    else:
                        print(" Incorect Password.")
                else:
                    Users_Deta.append(Read)

            if is_Email:
                print(" You Are Not Registed User. Please Register First.")

        if is_valid:
            with open("user.csv", "w", newline="") as file:
                Writer = csv.writer(file)
                Writer.writerow(first)
                Writer.writerows(Users_Deta)
            print(" Profile Updated Successfully.")

    def Change_Password(self):
        Users_Deta = []
        is_valid = False
        with open("user.csv", "r", newline="") as file:
            Reader = csv.reader(file)
            header = next(Reader, None)
            self.Email = input(" Enter Your Email : ")
            is_Email = True
            for Read in Reader:
                if Read[3] == self.Email:
                    is_Email = False
                    self.Password = input(" Enter Current Password : ")
                    if Read[5] == self.Password:
                        new_password = input(" Enter New Password : ")
                        Read[5] = new_password
                        Users_Deta.append(Read)
                        is_valid = True
                    else:
                        print(" Incorect Password.")
                        Users_Deta.append(Read)
                else:
                    Users_Deta.append(Read)
            if is_Email:
                print(" Email Not Found!.")
        if is_valid:
            with open("user.csv", "w", newline="") as file:
                Writer = csv.writer(file)
                if header:
                    Writer.writerow(header)
                Writer.writerows(Users_Deta)
            print(" Password Changed Successfully.")
