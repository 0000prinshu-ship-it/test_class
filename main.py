from abc import ABC, abstractmethod
import json 

'''with open ("medicine.json", 'r') as file: #this means open and read medicine.json and as file is nickane given to opened file 
    data= json.load(file) #read and update j pani xa inside json file into python object 
print(data) how what python read '''
class Inventory_Operations(ABC):

    ''' @abstractmethod
    def view_medicines(self):
        pass'''
    @abstractmethod
    def add_medicine(self):
        pass
    '''
    @abstractmethod
    def remove_medicine(self):
        pass'''
class Pharmacy_Inventory(Inventory_Operations):
     def __init__(self,name,price,stock, supplier_info,expiry_date):
         self.name=name
         self.price=price
         self.stock=stock
         self.supplier_info= supplier_info
         self.expiry_date=expiry_date

     def add_medicine (self):
         medicine_details={"name":self.name,
                           "price":self.price,
                           "stock_number":self.stock,
                           "supplier_name":self.supplier_info,
                           "expiry_date":self.expiry_date
                           }
         with open ("medicine.json", 'w') as file: #medicine.json is opened and nickname file is given
             json.dump(medicine_details, file) # medicine-details is added 
c= Pharmacy_Inventory('Paracetamol',250, 10, "ABC suppliers", '2026-2-20')

c.add_medicine()