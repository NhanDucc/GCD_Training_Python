class Parent:
    name: str
    __age: int
    _address: str 
    
    def __init__(self, name: str):
        self.name = name
        self.__age = 19
    
    def public_method(self):
        print("Parent")
    
    def __private_method(self):
        pass
    
    def _protected_method(self):
        return 1
        
class Children(Parent):
    def childrent_method(self):
        self.name = "II"
        self.public_method()
        self._address = "abcdef"
        
    # def get_address(self):
    #     return self._address
    
    # def set_address(self, value):
    #     self._address = value
    #     return self._address
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        self._address = value
        return self._address
    
    def public_method(self):
        super().public_method()
        print("Chilrent")
        
children = Children(name = "II")
children.childrent_method()
print(children.name)
children.public_method()