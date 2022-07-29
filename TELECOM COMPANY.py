

#                 PROGRAM FOR TELECOM COMPANY


#                      IMPORTED MODULES


import random
import pickle
import math
import time


#                      DEFINED FUNCTIONS


def write_data():
    emp_id=int(input('Enter Employee ID: '))
    emp_name=input('Enter Employee Name: ')
    emp_salary=int(input('Enter Employee Salary: '))
    data=[emp_id,emp_name,emp_salary]
    file=open('data.dat','ab')
    pickle.dump(data,file)
    print('record entered')
    file.close()
    
def new_sim():
    print('\nHi User,\n')
    sim_type=int(input('Want a Prepaid Sim Enter 1.\nFor a Postpaid Sim Enter 2 : '))
    
    if sim_type==1:
        pre_cust={}
        cust_name=input('\nEnter Name: ')
        cust_age=int(input('Enter Age : '))
        cust_aadhar=int(input('Enter Aadhar ID: '))
        cust_address=input('Enter Address: ')
        cust_mail=input('Enter E-mail ID: ')
        cust_number = []
        cust_number.append(random.randint(6, 7))
        for i in range(1, 10):
            cust_number.append(random.randint(0, 9))
        cust_id = []
        cust_id.append(random.randint(0,9))
        for i in range(1, 3):
            cust_id.append(random.randint(0, 9))
        print("\nGathering Information...")
        print("wait for 5 seconds")
        time.sleep(5)
        print("\nYour Customer ID is: ")
        for i in cust_id:
            print(i,end='')
        print("\nYour New Phone Number is: ")
        for i in cust_number:
            print(i,end='')
        
        
        
        #PLAN TYPE
        
        
        pre_cust['User ID']=cust_id
        pre_cust['Name']=cust_name
        pre_cust['Phone Number']=cust_number
        pre_cust['Number Type']='PRE-PAID'
        pre_cust['Age']=cust_age
        pre_cust['Aadhar ID']=cust_aadhar
        pre_cust['Address']=cust_address
        pre_cust['Mail ID']=cust_mail
        print('\n',pre_cust)
        print('\n\nRedirecting to Main Menu...')
        time.sleep(5)
        
        
    
    elif sim_type==2:
        post_cust={}
        cust_name=input('\nEnter Name: ')
        cust_age=int(input('Enter Age : '))
        cust_aadhar=int(input('Enter Aadhar ID: '))
        cust_address=input('Enter Address: ')
        cust_mail=input('Enter E-mail ID: ')
        cust_number = []
        cust_number.append(random.randint(6, 7))
        for i in range(1, 10):
            cust_number.append(random.randint(0, 9))
        cust_id = []
        cust_id.append(random.randint(0,9))
        for i in range(1, 4):
            cust_id.append(random.randint(0, 9))
        print("\nGathering Information...")
        print("wait for 5 seconds")
        time.sleep(5)
        print("\nYour Customer ID is: ")
        for i in cust_id:
            print(i,end='')
        print("\nYour New Phone Number is: ")
        for i in cust_number:
            print(i,end='')
        
        
        
        #PLAN TYPE
        
        
        post_cust['User ID']=cust_id
        post_cust['Name']=cust_name
        post_cust['Phone Number']=cust_number
        post_cust['Number Type']='POST-PAID'
        post_cust['Age']=cust_age
        post_cust['Aadhar ID']=cust_aadhar
        post_cust['Address']=cust_address
        post_cust['Mail ID']=cust_mail
        print('\n',post_cust)
        print('\n\nRedirecting to Main Menu...')
        time.sleep(5)
        
    else:
        print("\nInvalid Entry...\n")
        


def faq():
    while True:
        print('\n1. How can I get a new Jio prepaid/postpaid SIM card?')
        print('2. What documents do I need to buy a new Prepaid/Postpaid connection?')
        print('3. How long will it take to activate my new connection?')
        print('4. Do I have to pay any activation/delivery charges for buying a SIM card?')
        print('5. What are the additional benefits of a connection?')
        print('6. Quit\n')
        
        faq_choice=int(input('Enter Query No. '))
        
        if faq_choice == 1:
            print('')
        elif faq_choice == 2:
            print('You need original Proof of Identity (POI) and Proof of Address (POA) document such as Aadhaar, Voter ID, Passport, or Driving License.')
            print('In case you are porting your number from another operator, you would additionally need Unique Porting Code (UPC) for switching your connection.')
        elif faq_choice ==3:
            print ('The Searched Data is ')
        elif faq_choice ==4:
            print('')
        elif faq_choice ==5:
            print('')
        elif faq_choice == 6:
            print('Redirecting to Main Menu...')
            time.sleep(5)
            break
        else :
            print('\n\nInvalid Entry\nRe-Enter from given Choices\n\n')
        
            

def cust_sup():
    while True:
        print('\nNeed guidance?\nWe’d love to help you.\n')
        print('1. Need Helpline No.')
        print('2. Type your Query')
        print('3. Close your Account')
        print('4. Leave\n')
        
        cust_choice=int(input('Enter No. '))
            
        if cust_choice==1:
            print('\nOur experts are available for your assistance 24X7')
            print('ONLY REGISTERED NUMBERS CAN CALL!')
            print('Helpline No.     - 1800-108-1800')
            print('For Queries      - 299')
            print('For Comaplaints  - 399')
            print('For Int. support - 499')
            print('\nHELPLINE FOR NON-REGISTERED NUMBERS - 1800-009-1800')
        elif cust_choice==2:
            n=input('Enter Name :')
            e=input('Enter Email : ')
            no=input('Enter Phone Number : ')
            q=input('Enter Query[in Not More than 50 words] - ')
            print('\nQuery Submitted Successfully')
            print("Our Representatives our working 24X7, they'll contact you shortly")
        elif cust_choice==3:
           
           pass
           
           
            #delete program......
            
            
            
            
        
        elif cust_choice==4:
            print('Redirecting to Main Menu...')
            time.sleep(5)
            break
        else :
            print('\n\nInvalid Entry\nRe-Enter from given Choices\n\n')
    
    
    
        
            






#                       MAIN PROGRAM 


#                        MAIN MENU 


while True:
    print('\n\n            WELCOME TO TELECOM\n\n')
    print('1. Get a New Sim Card')
    print('2. Check Balance')
    print('3. Discover Plans')
    print('4. Recharge/Pay Bill')
    print('5. Change Personal Details')
    print('6. FAQ')
    print('7. Customer Support')
    print('8. Quit\n\n')
    
    menu_choice = int(input("Enter the suitable number : "))
    
    if menu_choice==1:
        new_sim()
    elif menu_choice== 2:
        print('The data is as Follows:')
        chk_bal()
    elif menu_choice== 3:
        print('The data is as Follows:')
        disc_plan()
    elif menu_choice==4:
        print (" The Searched Data is ")
        rec_pay()
    elif menu_choice==5:
        change_det()
    elif menu_choice==6:
        faq()
    elif menu_choice==7:
        cust_sup()
    elif menu_choice==8:
        break
    else :
        print('\n\nInvalid Entry\nRe-Enter from given Choices\n\n')