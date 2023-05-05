#LIM CHEN YI
#TP066187

import os
import datetime

#Access Page
def access():
    while True:
        print("**************************************************")
        print("**************************************************")
        print("**                                              **")
        print("**             Welcome to STARBANK!             **")
        print("**                                              **")
        print("**************************************************")
        print("**************************************************\n")
        print("(1) Login ")
        print("(2) Register ")
        option = input("Please enter your option (1 / 2): ")
        if ( option == "1" ):
            return "log"
        elif ( option == "2" ):
            return "reg"
        else:
            print("Invalid option, restart\n")

#Login Page
def login_page():
    print("Please enter Account Number and Password")
    #Enter account number and password
    acc_num = input("Account Number: ")
    password = input("Password: ")
    #Open user file 
    with open("file_accnum.txt", "r") as fh_accnum:
        foundrec = "notfound"
        for recline in fh_accnum:
            reclist = recline.strip().split(":")
            if reclist[0] == acc_num and reclist[1] == password:
                foundrec = reclist
                break
        if foundrec == "notfound":
            print("Account Number or Password incorrect")
            print("login unsuccessfully...!!!")
        else:
            print("Login Successful...")
    return foundrec

#Super Account Page
def super_acc():
    while True:
        print("\nHello, Super User")
        print("*******************************")
        print("Super User Account System")
        print("(1) Create staff account")
        print("(2) Create customer account")
        print("(3) Change super's account password")
        print("(4) View all staff details")
        print("\n(0) Logout")
        print("*******************************")
        option = input("Please enter your option: ")
        #Create staff account
        if ( option == "1" ):
            create_staff()
        #create customer account
        elif ( option == "2" ):
            list_supper = ["Super"]
            open_cus(list_supper)
        #Change super's account password
        elif ( option == "3" ):
            with open("file_accnum.txt", "r") as fh_pass:
                old_pass = fh_pass.readline().strip().split(":")
            change_pass(old_pass[1], old_pass[0],old_pass)
        #View customer detail
        elif ( option == "4" ):
            print("\t"+"STAFF DETAIL".center(111))
            print("\t"+"="*111)
            print("\t"+"|"+"Account Number".center(16)+"|"+"Name".center(24)+"|"+"IC".center(20)+"|", end = "")
            print("Phone Number".center(20)+"|"+"Email".center(25)+"|")
            print("\t"+"="*111)
            with open("file_staff.txt", "r") as fh1:
                for line in fh1:
                    list_fh = line.split(":")
                    print("\t"+"|"+list_fh[0].center(16)+"|"+list_fh[2].center(24)+"|"+list_fh[3].center(20)+"|", end = "")
                    print(list_fh[4].center(20)+"|"+list_fh[5].center(25)+"|")
            print("\t"+"="*111)
            retn = input("Enter any key to return")
        #Logout
        elif ( option == "0" ):
            print("Logout succesfully")
            print(datetime.datetime.now())
            print("\n")
            break
        else:
            print("Invalid option, restart\n")
        
#Staff Account Page
def staff_acc(staff_details):
    while True:
        #list_staff = [acc_num, pass, name, IC, phone_num, email]
        list_staff = staff_details.split(":")
        print("\nHello,", list_staff[2])
        print("*******************************")
        print("Staff User Account System")
        print("(1) Create customer account")
        print("(2) Edit customer's detail")
        print("(3) Print customer's statement")
        print("(4) View Personal Detail")
        print("(5) View All Customer Detail")
        print("(6) Change password")
        print("\n(0) Logout")
        print("*******************************")
        option = input("Please enter your option: ")
        #Create customer account
        if ( option == "1" ):
            open_cus(list_staff[0])                     
        #Edit customer account
        elif ( option == "2" ):
            cus_acc = input("Enter customer account: ")
            edit_flag = False
            #Does the customer account exist or not
            with open("file_cus.txt", "r") as file1:
                for recline in file1:
                    reclist = recline.strip().split(":")
                    if reclist[0] == cus_acc:
                        edit_flag = True
                        break
            if edit_flag == False:
                print("Wrong customer account, return to home page \n")
            elif edit_flag == True:
                edit_cus(cus_acc)
        #Print customer's statement
        elif ( option == "3" ):
            while True:
                acc_num = input("Enter customer's account number: ")
                with open("file_cus.txt", "r") as fh1:
                    for line in fh1:
                        list_state = line.strip().split(":")
                        if acc_num == list_state[0]:
                            break
                if ( acc_num != list_state[0] ):
                    print("Account number does not exist")
                    break
                cus_statement(acc_num, list_state[2])
                break
        #View Personal Detail
        elif ( option == "4" ):
            print("\t"+"-"*49)
            print("\t"+"|"+"1".center(5)+"|"+"Account Number".center(20)+"|"+list_staff[0].center(20)+"|")
            print("\t"+"-"*49)
            print("\t"+"|"+"2".center(5)+"|"+"Name".center(20)+"|"+list_staff[2].center(20)+"|")
            print("\t"+"-"*49)
            print("\t"+"|"+"3".center(5)+"|"+"IC".center(20)+"|"+list_staff[3].center(20)+"|")
            print("\t"+"-"*49)
            print("\t"+"|"+"4".center(5)+"|"+"Phone Number".center(20)+"|"+list_staff[4].center(20)+"|")
            print("\t"+"-"*49)
            print("\t"+"|"+"5".center(5)+"|"+"Email".center(20)+"|"+list_staff[5].center(20)+"|")
            print("\t"+"-"*49)
            opt = input("Enter any key to return: ")
        #View All customer detail
        elif ( option == "5" ):
            print("\t"+"CUSTOMER DETAIL".center(139))
            print("\t"+"="*135)
            print("\t"+"|"+"Account Number".center(16)+"|"+"Name".center(20)+"|"+"IC".center(20)+"|"+"Phone Number".center(20)+"|", end = "")
            print("Email".center(25)+"|"+"Account Type".center(16)+"|"+"Balance".center(10)+"|")
            print("\t"+"="*135)
            with open("file_cus.txt", "r") as fh1:
                for line in fh1:
                    list_fh = line.split(":")
                    print("\t"+"|"+list_fh[0].center(16)+"|"+list_fh[2].center(20)+"|"+list_fh[3].center(20)+"|"+list_fh[4].center(20)+"|", end = "")
                    print(list_fh[5].center(25)+"|"+list_fh[6].center(16)+"|"+list_fh[7].center(10)+"|")
            print("\t"+"="*135)
            retn = input("Enter any key to return")
        #change password
        elif ( option == "6" ):
            list_pass = change_pass(list_staff[1], list_staff[0], list_staff)
            list_pass.pop(-1)
            string = ":".join(list_pass)+":\n"
            #Change password in file_staff.txt
            with open("file_staff.txt", "r") as file1:
                read = file1.readlines()
                for i in range(0, len(read)):
                    if read[i] == staff_details:
                        line_psw = i
                        read[line_psw] = string
                        break
            with open("file_staff.txt", "w") as file2:
                j = 0
                while j < len(read):
                    file2.write(read[j])
                    j += 1       
            #Update password in staff page
            with open("file_staff.txt", "r") as update_staff:
                for line in update_staff:
                    if line.startswith(list_staff[0]):
                        staff_details = line
        #Logout
        elif ( option == "0" ):
            print("Logout succesfully")
            print(datetime.datetime.now())
            print("\n")
            break            
        else:
            print("Invalid option, restart\n")

#Customer Page
def cus_acc(cus_details):
    while True:
        list_cus = cus_details.split(":")
        list_cus.pop(-1) #[acc_num, password, name, IC, phone, email, acc_type, balance]
        print("\nHello,", list_cus[2])
        print("*******************************")
        print("Customer User Account System")
        print("(1) Deposit")
        print("(2) Withdrawal")
        print("(3) Change password")
        print("(4) Print statement")
        print("(5) Personal detail")
        print("\n(0) Logout")
        print("*******************************")
        option = input("Please enter your option: ")
        #Deposit
        if ( option == "1" ):
            print("Current Balance:", list_cus[7]) 
            new_balance = cus_deposit(list_cus[6], float(list_cus[7]), list_cus[2], list_cus[1], list_cus[0])
            change_balance(list_cus, new_balance)
            list_cus[7] = new_balance
            #Update balance in customer page
            with open("file_cus.txt", "r") as update_cus:
                for line in update_cus:
                    if line.startswith(list_cus[0]):
                        cus_details = line
                        break
        #Withdrawal
        elif ( option == "2" ):
            print("Current Balance:", list_cus[7]) 
            new_balance = cus_withdrawal(list_cus[6], float(list_cus[7]), list_cus[2], list_cus[1], list_cus[0])
            change_balance(list_cus, new_balance)
            list_cus[7] = new_balance
            #Update balance in customer page
            with open("file_cus.txt", "r") as update_cus:
                for line in update_cus:
                    if line.startswith(list_cus[0]):
                        cus_details = line
                        break            
        #Change password
        elif ( option == "3"):
            list_pass = change_pass(list_cus[1], list_cus[0], list_cus)
            string = ":".join(list_pass)+":\n"
            #Change password in file_cus.txt
            with open("file_cus.txt", "r") as file1:
                read = file1.readlines()
                for i in range(0, len(read)):
                    if read[i] == cus_details:
                        line_psw = i
                        read[line_psw] = string
                        break
            with open("file_cus.txt", "w") as file2:
                j = 0
                while j < len(read):
                    file2.write(read[j])
                    j += 1       
            #Update password in customer page
            with open("file_cus.txt", "r") as update_cus:
                for line in update_cus:
                    if line.startswith(list_cus[0]):
                        cus_details = line
        #Print statement
        elif (option == "4"):
            cus_statement(list_cus[0], list_cus[2])       
        #View personal information    
        elif ( option == "5" ):
            print("\t"+"-"*49)
            print("\t"+"|"+"1".center(5)+"|"+"Account Number".center(20)+"|"+list_cus[0].center(20)+"|")
            print("\t"+"-"*49)
            print("\t"+"|"+"2".center(5)+"|"+"Name".center(20)+"|"+list_cus[2].center(20)+"|")
            print("\t"+"-"*49)
            print("\t"+"|"+"3".center(5)+"|"+"IC".center(20)+"|"+list_cus[3].center(20)+"|")
            print("\t"+"-"*49)
            print("\t"+"|"+"4".center(5)+"|"+"Phone Number".center(20)+"|"+list_cus[4].center(20)+"|")
            print("\t"+"-"*49)
            print("\t"+"|"+"5".center(5)+"|"+"Email".center(20)+"|"+list_cus[5].center(20)+"|")
            print("\t"+"-"*49)
            print("\t"+"|"+"6".center(5)+"|"+"Account Type".center(20)+"|"+list_cus[6].center(20)+"|")
            print("\t"+"-"*49)
            print("\t"+"|"+"7".center(5)+"|"+"Balance".center(20)+"|"+list_cus[7].center(20)+"|")
            print("\t"+"-"*49)
            print("\nPlease contact staff if the information incorrect.")
            print("You are not allow to change account number, name,IC and account type.")
            opt = input("Enter any key to return: ")
        #Logout            
        elif ( option == "0" ):
            print("Logout succesfully")
            print(datetime.datetime.now())
            print("\n")
            break
        else:
            print("Invalid option, restart\n")

#Create staff/customer account basic form
def create_acc():
    name = input("Name: ")
    IC = input("IC number (without - ): ")
    while (IC.isdigit() == False) or (len(IC) != 12):
        print("Please enter valid IC number\n")
        IC = input("IC number (without - ): ")
    phone = input("Phone number (without - ): ")    
    while (phone.isdigit() == False):
        print("Please enter valid phone number\n")
        phone = input("Phone number (without - ): ")
    email = input("Email: ")
    while ("@" not in email) or ".com" not in email:
        print("Please enter valid email\n")
        email = input("Email: ")
    return([name, str(IC), str(phone), email])

#Open Staff Account
def create_staff():   
    #Put staff details into list_staff [name, IC, phone, email]
    list_staff = create_acc()
    print("Successfully create staff account")
    #Autogenerate staff account & default password
    staff_acc = genid("staff")
    default_pass = "staff"
    for i in range(-4, 0):
        default_pass += list_staff[1][i] #staff + IC last 4 number
    print("This is Account Number:", staff_acc)
    print("This is Default Password:", default_pass)
    #save data into file_staff.txt
    with open("file_staff.txt", "a") as staff_file1:
        staff_file1.write(str(staff_acc)+":"+default_pass+":")
        for j in range(0, 4):
            staff_file1.write(list_staff[j]+":")
        staff_file1.write("\n")
    #save account number & password into file_accnum.txt
    with open("file_accnum.txt", "a") as file_accnum:
        file_accnum.write(str(staff_acc)+":"+default_pass+"\n")
    return

#Registration form for customer
def register_form(openers):
    print("\nFill in the registration form")
    #Fill the form and put customer details into list_cus
    list_cus = create_acc() #[name, IC, phone, email]
    #Saving or current account
    print("Which type of account do you want to open?")
    while True:
        acc_type = input("Savings account or Current account (s / c): ").lower()
        if acc_type == "s":
            acc_types = "Savings"
            break
        elif acc_type == "c":
            acc_types = "Current"
            break
        else:
            print("Invalid option, try again\n")
    if openers == "cus":
        #Autogenerate application reference ID
        refer_num = ""
        for i in range(-5, 0):
            refer_num += str(list_cus[1][i])
        refer_num += "-" + list_cus[0][0] + list_cus[0][1] + list_cus[0][-1]+acc_type
        refer_num = refer_num.upper()
        print("\nThis is your application reference:", refer_num, "\n")
        print("Congrats! Your account opening application has been submmitted.")
        print("Walk in to any Starbank brand with your MyKad and ", end = "")
        print("application reference", refer_num, "\n")
    else:
        #Registration form filled by staff
        refer_num = openers
    #Put refer_num and acc_types into list_cus
    list_cus.insert(0, refer_num)
    list_cus.append(acc_types)  #[refer_num, name, IC, phone, email, acc_types]
    #write all customer detail into temp_cus.txt
    with open("temp_cus.txt", "a") as file1:
        for i in list_cus:
            file1.write(i+":")
        file1.write("\n")
    return

#Open Customer Account step 1
def open_cus(list_staff):
    while True:
        #Check does temp_cus.txt exist or not, if not create this text file
        tempcus_exist = os.path.exists("temp_cus.txt")
        if tempcus_exist == False:
            tempcus_file = open("temp_cus.txt", "w")
            tempcus_file.close()
        reg = input("Did customer register online or not?(y/n): ").lower()
        if reg == "y":
            refer_flag = False
            refer_num = input("Enter application reference: ")
            with open("temp_cus.txt", "r") as cus_file:
                for line in cus_file:
                    line_list = line.strip().split(":")
                    if line_list[0] == refer_num:
                        cus_detail = line.split(":")
                        cus_detail.pop(-1)
                        refer_flag = True
                        break
            if refer_flag == True:
                create_cus(cus_detail)
                dlt_temp(line)
                return
            else:
                print("Invalid application reference, try again")
        elif reg == "n":
            opener = "staff" + list_staff[0]
            register_form(opener)
            with open("temp_cus.txt", "r") as cus_file:
                open_flag = False
                for line in cus_file:
                    if line.startswith(opener) == True:
                        cus_detail = line.split(":")
                        cus_detail.pop(-1)
                        open_flag = True
                        break
            if open_flag == True:
                create_cus(cus_detail)
                dlt_temp(line)
                return
                    
#Open Customer Account step 2
def create_cus(list_cus):
    while True:
        print("\nCheck for customer detail")
        print("Name:", list_cus[1])
        print("IC:", list_cus[2])
        print("Phone number:", list_cus[3])
        print("Email:", list_cus[4])
        print("Account type:", list_cus[5])
        correct = input("Does the detail correct?(y/n): ").lower()
        if correct == "y":      
            #Add customer's name into cus_statement.txt
            with open("cus_statement.txt", "a") as file1:
                file1.write("\n"+list_cus[1])
            #Deposit money
            acc_balance = 0
            acc_balances = cus_deposit(list_cus[5], float(acc_balance), list_cus[1], 0, 0)
            list_cus.append(acc_balances)
            #Autogenerate customer account number and default password
            cus_acc = genid("cus")
            default_pass = "Cus&"
            for i in range(-4, 0):
                default_pass += list_cus[2][i]
            print("\nSuccesfully open customer account")
            print("This is Account Number:", cus_acc)
            print("This is Default Password:", default_pass)
            #Put the customer data into file_cus.txt
            with open("file_cus.txt", "a") as file2:
                file2.write(str(cus_acc)+":"+default_pass+":")
                for i in range(1, 7):
                    file2.write(list_cus[i]+":")
                file2.write("\n")
            #Save account number & password into file_accnum.txt
            with open("file_accnum.txt", "a") as file_accnum:
                file_accnum.write(str(cus_acc)+":"+default_pass+"\n")
            #Change customer's name to account num in cus_statement.txt
            count = 0
            with open("cus_statement.txt", "r") as fh1:
                for line in fh1:
                    if line.startswith(list_cus[1]):
                        cus_transac = line.strip().split(":")
                        cus_transac[0] = str(cus_acc)
                        new_line = ":".join(cus_transac)
                        break
                    count += 1
            with open("cus_statement.txt", "r") as fh2:
                read = fh2.readlines()
                read[count] = new_line
            with open("cus_statement.txt", "w") as fh3:
                for i in range(len(read)):
                    fh3.write(read[i])
            return
        #Edit information    
        elif correct == "n":
            while True:
                print("\n***************************")
                print("(1) Name:", list_cus[1])
                print("(2) IC:", list_cus[2])
                print("(3) Phone number:", list_cus[3])
                print("(4) Email:", list_cus[4])
                print("(5) Account type:", list_cus[5])
                print("\n(0) Finish edit")
                print("***************************")
                print("You are not allow to change name and account type")
                print("This is the only chance to change IC.")
                option = input("Which one do you want to edit?: ")
                if option == "1" or option == "5":
                    print("You are not allow to change this")
                elif option == "2":
                    print("Current IC :", list_cus[2])
                    new_IC = input("Enter IC number(without - ): ")
                    while (new_IC.isdigit() == False ) or (len(new_IC) < 12):
                        print("Please enter valid IC number\n")
                        new_IC = input("IC number (without - ): ")
                    list_cus[2] = new_IC
                    print("Succesfully change IC number")
                    print("New IC number: ", list_cus[2], "\n")
                elif option == "3":
                    print("Current phone number :", list_cus[3])
                    new_phone = input("Enter phone number(without - ): ")
                    while (new_phone.isdigit() == False):
                        print("Please enter valid phone number\n")
                        new_phone = input("Phone number (without - ): ")
                    list_cus[3] = new_phone
                    print("Succesfully change phone number")
                    print("New phone number number: ", list_cus[3], "\n")
                elif option == "4":
                    print("Current email :", list_cus[4])
                    new_email = input("Enter email: ")
                    while ("@" not in new_email) or (".com" not in new_email):
                        print("Please enter valid email\n")
                        new_email = input("Email: ")
                    list_cus[4] = new_email
                    print("Succesfully change email")
                    print("New email: ", list_cus[4], "\n")
                elif option == "0": 
                    return create_cus(list_cus)
                else:
                    print("Invalid option, try again")
        else:
            print("Invalid option, try again\n")

#Autogenerate account number for staff/customer
def genid(type_acc):
    with open("id.txt", "r") as idfh:
        rec = idfh.readline()
        rec_list = rec.strip().split(":")
    if type_acc == "staff":
        oldid = rec_list[0]
    elif type_acc == "cus":
        oldid = rec_list[1]
    nextid = int(oldid) + 1
    if type_acc == "staff":
        rec_list[0] = str(nextid)
    elif type_acc == "cus":
        rec_list[1] = str(nextid)
    rec = ":".join(rec_list)
    with open("id.txt", "w") as fh:
        fh.write(rec)
    return str(nextid)

#Delete data from temp_cus.txt
def dlt_temp(data):
    with open("temp_cus.txt","r") as file1:
        temp_list = file1.readlines()
    with open("temp_cus.txt", "w") as file2:
        for i in temp_list:
            if i != data:
                file2.write(i)
    return

#Deposit
def cus_deposit(acc_type, acc_balance, name, password, acc_num):
    while True:
        try:
            deposit = float(input("Enter deposit amount: "))
            if deposit <= 0:
                print("Error, deposit can not equal or small than 0")
                print("try again\n")
            elif deposit != round(deposit, 2):
                print("Error")
                print("Amount do not more than 2 decimal places")
                print("try again\n")
            elif acc_balance != 0:
                verify_pass = input("Enter password: ")
                if verify_pass != password:
                    print("Wrong password, try again\n")
                else:
                    acc_balance += deposit
                    acc_balance = round(acc_balance, 2)
                    break
            #First time deposit
            else:
                if acc_type == "Savings" and deposit >= 100:
                    acc_balance += deposit
                    acc_balance = round(acc_balance, 2)
                    break
                elif acc_type == "Current" and deposit >= 500:
                    acc_balance += deposit
                    acc_balance = round(acc_balance, 2)
                    break
                else:
                    print("Does not meet minimum deposit.")
                    print("try again\n")

        except:
            print("Error, try again.\n")
            
    #Successfully deposit and display new account balance    
    print("Succesfully deposit")
    date = datetime.date.today()
    print(datetime.datetime.now())
    print("Account Balance:", acc_balance)

    #Put data into cus_statement.txt
    with open("cus_statement.txt", "r") as file1:
        count = 0
        for line in file1:
            if line.startswith(name) or line.startswith(str(acc_num)):
                line = line.rstrip(":\n")
                if acc_balance == round(acc_balance, 1):
                    acc_balance = str(acc_balance)+"0"
                if deposit == round(deposit, 1):
                    deposit = str(deposit)+"0"
                add_transaction = (line+":"+str(date)+":"+"Deposit"+":"+"+"+str(deposit)+":"+str(acc_balance)+":\n")
                break
            count += 1
    with open("cus_statement.txt", "r") as file2:
        read = file2.readlines()
        read[count] = add_transaction
    with open("cus_statement.txt", "w") as file3:
        i = 0
        while i < len(read):
            file3.write(read[i])
            i += 1
    return str(acc_balance)

#Withdrawals
def cus_withdrawal(acc_type, acc_balance, name, password, acc_num):
    while True:
        try:
            withdrawal = float(input("Enter withdrawal amount: "))
            if withdrawal <= 0:
                print("Error, withdrawal can not equal or small than 0")
                print("try again\n")
            elif withdrawal  != round(withdrawal, 2):
                print("Error")
                print("Amount do not more than 2 decimal places")
                print("try again\n")
            else:
                verify_pass = input("Enter password: ")
                if verify_pass != password:
                    print("Wrong password, try again\n")
                else:
                    new_balance = acc_balance - withdrawal
                    #Check minimum balance
                    if acc_type == "Savings" and new_balance >= 100:
                        acc_balance -= withdrawal
                        acc_balance = round(acc_balance, 2)
                        break
                    elif acc_type == "Current" and new_balance >= 500:
                        acc_balance -= withdrawal
                        acc_balance = round(acc_balance, 2)
                        break
                    else:
                        print("Over withdrawal amount")
                        if acc_type == "Savings":
                            print("Remainder balance must at least RM100.")
                        else:
                            print("Remainder balance must at least RM500.")
                        while True:
                            option = input("Do you want to try again?(y/n): ").lower()
                            if option == "y":
                                break
                            elif option == "n":
                                return str(acc_balance)
                            else:
                                print("Invalid option\n") 
        except:
            print("Error, try again.\n")
    #Successfully withdrawal and display new account balance    
    print("Succesfully withdrawal")
    date = datetime.date.today()
    print(datetime.datetime.now())
    print("Account Balance:", acc_balance)
    #Put data into cus_statement.txt
    with open("cus_statement.txt", "r") as file1:
        count = 0
        for line in file1:
            if line.startswith(name) or line.startswith(acc_num):
                line = line.rstrip(":\n")
                if acc_balance == round(acc_balance, 1):
                    acc_balance = str(acc_balance)+"0"
                if withdrawal == round(withdrawal, 1):
                    withdrawal = str(withdrawal)+"0"
                add_transaction = (line+":"+str(date)+":"+"Withdrawal"+":"+"-"+str(withdrawal)+":"+str(acc_balance)+":\n")
                break
            count += 1
    with open("cus_statement.txt", "r") as file2:
        read = file2.readlines()
        read[count] = add_transaction
    with open("cus_statement.txt", "w") as file3:
        i = 0
        while i < len(read):
            file3.write(read[i])
            i += 1
    return str(acc_balance)

#Change the balance in file_cus.txt
def change_balance(list_cus, new_balance):
    with open("file_cus.txt", "r") as file1:
        count = 0
        for line in file1:
            if line.startswith(list_cus[0]) == True:
                new = line.rstrip(list_cus[7] + ":" +"\n")
                new += (":" + new_balance + ":" + "\n")
                break
            count += 1
    with open("file_cus.txt", "r") as file2:
        read = file2.readlines()
        read[count] = new
    with open("file_cus.txt", "w") as file3:
        i = 0
        while i < len(read):
            file3.write(read[i])
            i += 1
    return

#Change password
def change_pass(old_pass, acc_num,list_pass):
    while True:
        current_pass = input("Enter current password: ")
        if current_pass != old_pass:
            print("Error current password, try again\n")
        else:
            new_pass = input("Enter new password(at least 7 characters): ")
            if len(new_pass) >= 7:
                confirm_pass = input("Confirm password: ")
                if new_pass == confirm_pass:
                    list_pass[1] = new_pass
                    print("Successfully change password")
                    break
                else:
                    print("Password don't match, try again\n")
            else:
                print("Password too short. try again\n") 
    #Change password in file_accnum.txt
    with open("file_accnum.txt", "r") as file_acc1:
        count = 0
        for lines in file_acc1:
            if lines.startswith(acc_num):
                break
            count += 1
    with open("file_accnum.txt", "r") as file_acc2:
        read_accnum = file_acc2.readlines()
    read_accnum[count] = (list_pass[0] + ":" + new_pass + "\n")
    with open("file_accnum.txt", "w") as file_acc3:
        k = 0
        while k < len(read_accnum):
            file_acc3.write(read_accnum[k])
            k += 1
    return list_pass

#Edit the customers' details
def edit_cus(cus_acc):
    #Find the customer detail
    with open("file_cus.txt", "r") as file1:
        count = 0
        for line in file1:
            if line.startswith(cus_acc) == True:
                cus_detail = line
                break
            count += 1
    list_detail = cus_detail.split(":")
    list_detail.pop(-1)
    #Edit customer's detail
    while True:
        print("\nThis is customer's detail")
        print("***********************************")
        print("(1)Account Number:", list_detail[0])
        print("(2)Password:", list_detail[1])
        print("(3)Name:", list_detail[2])
        print("(4)IC:", list_detail[3])
        print("(5)Phone Number:", list_detail[4])
        print("(6)Email:", list_detail[5])
        print("(7)Account type:", list_detail[6])
        print("\n(0)Finish edit")
        print("***********************************")
        print("You are not allow to change account number, name, IC and account type")
        option = input("Which one do you want to edit: ")
        if option == "2":
            old_pass = list_detail[1]
            print("Current Password:", list_detail[1])
            new_pass = input("Enter password: ")
            list_detail[1] = new_pass
            print("Succesfully change password")
            print("New password: ", list_detail[1], "\n")       
            #Change password in file_accnum.txt
            with open("file_accnum.txt", "r") as file_pass:
                counts = 0
                for line in file_pass:
                    if line.startswith(list_detail[0]) == True:
                        new_detail = (list_detail[0]+":"+new_pass+"\n")
                        break
                    counts += 1
            with open("file_accnum.txt", "r") as file_pass2:
                read = file_pass2.readlines()
                read[counts] = new_detail
            with open("file_accnum.txt", "w") as file_pass3:
                i = 0
                while i < len(read):
                    file_pass3.write(read[i])
                    i += 1
        elif option == "5":
            print("Current Phone Number:", list_detail[4])
            new_phone = input("Phone number (without - ): ")
            while (new_phone.isdigit() == False):
                print("Please enter valid phone number\n")
                new_phone = input("Phone number (without - ): ")
            list_detail[4] = new_phone
            print("Succesfully change phone number")
            print("New phone number: ", list_detail[4], "\n")
        elif option == "6":
            print("Current Email:", list_detail[5])
            new_email = input("Enter Email: ")
            while ("@" not in new_email) or (".com" not in new_email):
                print("Please enter valid email\n")
                new_email = input("Email: ")
            list_detail[5] = new_email
            print("Succesfully change email")
            print("New email: ", list_detail[5], "\n")
        elif option == "1" or option == "3" or option == "4" or option == "7":
            print("You are not allow to change account number, name, IC and account type\n")
        elif option == "0":
            break
        else:
            print("Invalid option, try again\n")
    #Convert new detail from list to string
    string = ""
    for i in list_detail:
        string += (i+":")
    string += "\n" 
    #Put new detail into file_cus.txt
    with open("file_cus.txt", "r") as file2:
        read = file2.readlines()
        read[count] = string
    with open("file_cus.txt", "w") as file3:
        i = 0
        while i < len(read):
            file3.write(read[i])
            i += 1
    return
             
#Customer’s Statement of Account Report
def cus_statement(acc_num, name):
    #Start date
    while True:
        try:
            start = input("Enter start date(YY-MM-DD): ")
            start_exist = True
            start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
            if start_date > datetime.datetime.today():
                print("Start date can not bigger than today date.")
                start_exist = False
            if start_exist== True:
                break
        except:
            print("Invalid date, try again\n")
    #End date
    while True:
        try:
            end = input("Enter end date(YY-MM-DD): ")
            end_exist = True
            end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
            if end_date > datetime.datetime.today():
                print("End date can not bigger than today date.")
                end_exist = False
            if end_exist == True:
                if end_date < start_date:
                    print("End date can not smaller than start date.")
                else:
                    break
        except:
            print("Invalid date, try again\n")
    #Find the transaction
    with open("cus_statement.txt", "r") as file1:
        for line in file1:
            if line.startswith(acc_num) == True:
                data = line
                break
    data = data.split(":")
    data.pop(0)
    data.pop(-1)
    #Start date
    start_pop = False
    end_pop = False
    for i in range(0, len(data)):
        if i == 0 or i % 4 == 0:
            date_time = datetime.datetime.strptime(data[i], "%Y-%m-%d")
            #delete the data before start_date
            if start_date <= date_time:
                count = i-1
                start_pop = True
                break        
    if start_pop == True:        
        for j in range(count, -1, -1):
            data.pop(j)
    #End date
    for i in range(0, len(data)):
        if i == 0 or i % 4 == 0:
            enddate_time = datetime.datetime.strptime(data[i], "%Y-%m-%d")
            #delete the data after end_date
            if enddate_time > end_date:
                end_count = i-1
                end_pop = True
                break
    if end_pop == True:
        for j in range(len(data)-1, end_count, -1):
            data.pop(j)    
    #Find begin balance
    while True:
        if len(data) == 0:
            begin_balance = "0.00"
            break
        if data[1] == "Deposit":
            begin_balance = float(data[3]) - float(data[2])
            begin_balance = round(begin_balance, 2)
            if begin_balance == round(begin_balance, 1):
                begin_balance = str(begin_balance)+"0"
                break
        else:
            begin_balance = -float(data[2]) + float(data[3])
            begin_balance = round(begin_balance, 2)
            if begin_balance == round(begin_balance, 1):
                begin_balance = str(begin_balance)+"0"
                break
    #Displat the statement
    print("\n")
    print("\tName: {}".format(name))
    print("\tAccount Number: {}                                Statement Date: {}".format(acc_num, datetime.date.today() ))
    print("\t"+"ACCOUNT TRANSACTIONS".center(81))
    print("\t"+"Date".center(12)+"|"+"Description".center(21)+"|"+"Withdrawals".center(15)+"|"+"Deposits".center(14)+"|"+"Balance".center(15))
    print("\t"+"".center(12)+"|"+"".center(21)+"|"+"( RM )".center(15)+"|"+"( RM )".center(14)+"|"+"( RM )".center(14))
    print("\t"+"-"*12+"|"+"-"*21+"|"+"-"*15+"|"+"-"*14+"|"+"-"*15)
    print("\t"+"".center(12)+"|"+"Beginning Balance".center(21)+"|"+"".center(15)+"|"+"".center(14)+"|"+"{}".center(15).format(begin_balance))
    #content
    total_dep = 0
    total_with = 0
    space = "               |"
    space2 = "              |"
    space_dep = "       "
    space_dep2 = "       "
    space_with = "       "
    space_with2 = "       "
    for i in range(0, len(data)):
        if i == 0 or i % 4 == 0:
            if(data[i+1]) == "Deposit":
                for j in range(5, len(data[i+2])):
                    space_dep = space_dep[0:-1]
                print("\t {}{}{}{}{}".format(data[i]+" |",data[i+1].center(21)+"|", space,space_dep+data[i+2]+"  |","  "+data[i+3].center(15)))
                total_dep += float(data[i+2])
                space_dep = space_dep2
            elif(data[i+1]) == "Withdrawal":
                for j in range(5, len(data[i+2])):
                    space_with = space_with[0:-1]
                print("\t {}{}{}{}{}".format(data[i]+" |",data[i+1].center(21)+"|",space_with+data[i+2]+"   |", space2,"  "+data[i+3].center(15)))
                total_with -= float(data[i+2])
                space_with = space_with2
    #total
    total_with = round(total_with, 2)
    total_dep = round(total_dep, 2)
    if len(data) == 0:
        data.append("0.00")
        total_dep = 0.00
        total_with = 0.00
    if total_with == 0:
        total_with = "0.00"
    elif total_with == round(total_with, 1):
        total_with = str(total_with)+ "0"
    if total_dep == round(total_dep, 1):
        total_dep = str(total_dep)+ "0"
    total_with2 = "-"+str(total_with)
    total_dep2 = "+"+str(total_dep)
    print("\t"+"-"*81)
    print("\tTotal:"+" "*28+total_with2.center(15)+" "+total_dep2.center(15) )     
    print("\tEnding Balance    :", data[-1])
    print("\tTotal Deposit     :", str(total_dep))
    print("\tTotal Withdrawal  :", str(total_with))
    print("\t"+"*** End of Statement ***".center(81))
    while True:
        option = input("\nEnter r to return(r): ").lower()
        if option == "r":
            return
            
#main_logic (starting point)
while True:
    log_reg = access()
    if ( log_reg == "log" ):
        loginstate = login_page()
        if loginstate != "notfound":
            #differentiate type of account
            if (loginstate[0][0] == "1"):
                super_acc() #super account
            elif(loginstate[0][0] == "2"):
                with open("file_staff.txt") as fh_staff:
                    for line in fh_staff:
                        if line.startswith(loginstate[0]) == True:
                            staff_detail = line
                staff_acc(staff_detail) #staff account
            else:
                with open("file_cus.txt") as fh_cus:
                    for line in fh_cus:
                        if line.startswith(loginstate[0]) == True:
                            cus_detail = line
                cus_acc(cus_detail)  #customer account
    #fill up registration form         
    elif ( log_reg == "reg" ):
        opener = "cus"
        register_form(opener)       
    #Quit or not    
    qut = input("Enter q or Q to quit...Another key to Continue...\n").lower()
    if qut == "q":
        print("Quit")
        break














