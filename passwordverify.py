from operator import truediv
import profile
import login1

class Main():
    name = "Hackathon"
    password = "Hackathon"
    a = True
    n = login1.username.get()
    p = login1.password.get()
    while(a):
        if(p != password):
            p = input("Incorrect password, please try again: ")
        else:
            a = False   
    print("the password is correct")
    

         
