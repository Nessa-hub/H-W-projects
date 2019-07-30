#Car wash management system
import datetime

class Customer:
    def __init__(self):
        pass

    def drive_in(self):
        #At the entrance, make use of sensors. If gates detect motion/presence of an object(car/humanbeing), they should swing open

        object = Car
        if object == Car:
            #Open gates
            #Print welcome message to customer on screen
            print("Welcome to Phos GH")

    # def Already_Existing_Customer():
    #     password = 1234
    #     if password = 1234
    #       print("Please hand over your keys to the attendant")

class Customer_Database:
    #Register new customers, allow already existing customers to proceed
    Customer_type = int(input("Press 1 if you are new and 2 if you are an already existing customer: "))

    if Customer_type == 1:
        customer_name = input("Please enter your name: ")
        car_model = input("Please enter your car's model: ")
        car_number = input("Please enter your car's number: ")
        contact_number = input("Please enter your contact number: ")

        def Register_Customer(self,customer_name,car_model,car_number,contact_number):
            self.customer_name = customer_name
            self.car_model = car_model
            self.car_number = car_number
            self.contact_number = contact_number
            #self.id_number = id_number

            Customer_List = dict()



        Customer_List = {"Customer's name":{},"Car model":{},"Car number":{}.format(customer_name,car_model,car_number)}

        print("You may now proceed to the next attendant")

    elif Customer_type == 2:
        print("Please proceed to the next attendant")

    else:
        Customer_type = input("Error!\n Please press 1 if you are a new customer and 2 if you are an already existing customer: ")
