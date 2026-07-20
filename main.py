from abc import ABC, abstractmethod

class Inventory_Operations(ABC):

    @abstractmethod
    def view_medicines(self):
        pass

    @abstractmethod
    def add_medicine(self):
        pass

    @abstractmethod
    def remove_medicine(self):
        pass
#class Pharmacy_Inventory(Inventory_Operations):
