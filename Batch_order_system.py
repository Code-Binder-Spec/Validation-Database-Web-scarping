from uuid import uuid4
from pydantic import BaseModel , model_validator,Field
import random
from datetime import datetime
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "orders.db")
connect = sqlite3.connect(DB_PATH)

class UserDetails(BaseModel):
   
    username:str
    password:str
    confi_username : str
    confi_password : str

    @model_validator(mode ='after')
    def checking_everything_for_login_system(self):
            if self.username != self.confi_username:
                  raise ValueError("User name not matching")
            if self.password != self.confi_password:
                  raise ValueError("Password donot matching")
            return self
    
class Details(BaseModel):
     
      name:str
      city:str
      pincode:int
      @model_validator(mode ='after')
      def checking_name_and_pincode(self):
            if len(self.name) < 3:
                  raise ValueError("Too short name")
            if len(str(self.pincode)) != 4:
                  raise ValueError("Pincode Must be 4 digit")
            return self

class Payment(BaseModel):
        
        product : str
        amount_of_product : int
                


class Ordering(BaseModel):
       
       login : UserDetails
       Address : Details
       amount_of_balance : int
       order_confirmation : bool
       payment_product : Payment
       order_id : str = Field(default_factory=lambda:str (uuid4()))
       time : datetime = Field(default_factory=datetime.now)

       @model_validator(mode = 'after')
       def checking_capacity(self):
              if self.payment_product.amount_of_product > self.amount_of_balance :
                     raise ValueError("You cant buy a product with price more than your balance")
     
              return self
products = {
    
    'phone': 25000,
    'laptop': 54000,
    'waterbottle': 599,
    'spectacles': 458,
    'pen':10,
    'book':399
    
    }



orders_batch = [
    {
        "login": {"username": "adhilx", "password": "123", "confi_username": "adhilx", "confi_password": "123"},
        "Address": {"name": "Adhil", "city": "Sharjah", "pincode": 5671},
        "order_confirmation": True,
        "amount_of_balance":1000
    },
    {
        "login": {"username": "hacker", "password": "123", "confi_username": "hacker", "confi_password": "123"}, 
        "Address": {"name": "Bob", "city": "Dubai", "pincode": 1111},
        "order_confirmation": True,
        "amount_of_balance":2321
    },
    {
        "login": {"username": "student1", "password": "abc", "confi_username": "student1", "confi_password": "abc"},
        "Address": {"name": "Charlie", "city": "Ajman", "pincode": 2222}, 
        "order_confirmation": True,
        "amount_of_balance":9232
    }
]

def placing_order(order : Ordering):
          
           if order.order_confirmation:
          
                  order.amount_of_balance = order.amount_of_balance - order.payment_product.amount_of_product
                  print("\nName : ",order.Address.name)
                  print("City : ",order.Address.city)
                  print("Pincode : ",order.Address.pincode)
                  print("Product : ",order.payment_product.product)
                  print("Order id : ",order.order_id)
                  print("Time : ",order.time)

                  connect.execute("""
                               INSERT INTO orders (order_id,name,city,product,amount,time)
                               VALUES(?,?,?,?,?,?)                                 


                                """,(
                                          order.order_id,
                                          order.Address.name,
                                          order.Address.city,
                                          order.payment_product.product,
                                          order.payment_product.amount_of_product,
                                          order.time
                                                
                                                ))
                  connect.commit()
           else:
                  print("Order cancelled")


for i,data in enumerate(orders_batch,1):

        prod_name,prod_price = random.choice(list(products.items())) 
        
        new_data = {
                **data,
                
                "payment_product":{

                           "product" : prod_name,
                           "amount_of_product":  prod_price                     
 

                }

        }
        
        
        try:
                p1 = Ordering(**new_data)
                placing_order(p1)

        except Exception as e:
                print(f"\nIn user {i} Failed insufficient data. Reason : {e}")

print("The Project completed")
                



       
        


