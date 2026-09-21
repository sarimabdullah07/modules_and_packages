#In this module, we are giong to read customer data
import random
def customer_registration():
    id=random.randint(0,100000000)
    customer_name=input("Enter your name: ")
    dob=input("Enter you dob as ddmmyy without any other charachter: ")
    #generation of unique id
    id=customer_name+dob+str(id)
    city=input("Enter your city: ")
    gender=input("Enter gender: ")
    
    return (id, customer_name, dob, city, gender)
