import csv
class item:# this is called the class level activities and off this stuff gets applied at the instance level as well.
    
    payrate = 0.8# although this statement is in the class level we can acess it from the instance level as well.
    all = []
    def __init__(self,name : str,price : float,quantity: int):#run validations on the types of data recieved
        print('You created the class:',name) # this line is running it for all of the instances within the class.
        assert price >=0 # making sure that the values inputted even make sense or not.
        assert quantity >=0 # 
        
        # created the self and then assigned the related parameters to the self.
        self.name = name 
        self.price = price
        self.quantity = quantity

        item.all.append(self)# creating a list which contains all the instances within it to acess their attributes through it 
    
    def cal_tl_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * self.payrate # by putting self here we can acess the values differntly based on if we want that item to get the 
        # differnt rate or not.
    def __repr__(self):
        return f"{self.__class__.__name___}('{self.name}','{self.price}',{self.quantity})"# here using the self.__class__.__name___ we can acess the
        # class name generically without needing to hard code it everytime, ie we can acess teh child classes here as well
        
    @classmethod# this is magically getting info from a csv file and then converting that into a list of dictionaries

    
    #this does something which has a relation to the class but at the same time usually has to do something with the manupulation of the 
    #different data sets like csv to instantiate objects like has been done with csv
    
    def instantiate_from_csv(cls):# this sends the class reference as the first argument and not the self similar to staticmethod line 38
        with open('C:\\Users\\Shourya\\OneDrive\\Desktop\\anaconda\\items.csv','r') as f:# opening the csv file
            reader = csv.DictReader(f) # reading an putting it as a dictionary
            items = list(reader)# converting in a list of dictionaries
        for lul in items:# reading the intems of the list to give us the individual dictionaries, just some insane shit
            item(
                name = lul.get('name'),
                price = float(lul.get('price')),
                quantity = int(lul.get('quantity'))
            )
    @staticmethod # these are also called decorators which help us run a  diff function in the background before running the code within it.
    
    #we use this method when the function that we are trying to pass is not something unique to each instance,
    #but has some relation to the class obviously
    
    def is_integer(num):# in static method the instance is never sent as the first argument same as classmethod in line 27 it's like a regular func
        # will count out the numbers that have a point 0 in them like 10.0 that we dont like
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
class Phone(item):# when we create a child class within a parent class we can use the super function to use all the paramets of the parent class
        # without needing to hard code it specifically
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(# super allows us to use the parent atribute classes without needing to code for it again.
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones
        
       # now to make this more readable we can put each the main class the sub class and all their respective atributes in differnt files and acess
        #then using from item import Item in each of the files again.
        
    @property # the property as a whole allows to change what to do with attributes itself
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name # by setting up this __ we are able to make this act as a private atribute which cannot be editted this is also known
        # read only attribute.

    # we can use this thing called property decorator in order to incorporaet the properties
    # setting up private atributes first we have to set up the @property which will set that value in the class level and then to make it 
    # private we do the thing in line 76
    @name.setter # a property which allows us to change the value of a read only attribute
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

phone1 = Phone("jscPho", 500, 5, 1)

#print(item.all)



print(item.is_integer(7))


# process for setting up read only attributes for more critical attriutes that are usefull


# item1 = item('phone',100,3)
# item1.payrate = 0.7# here by setting a diff payrate first when the code tries to access the instance pay rate it will find it for phone 
# but when it tries to acess the same thing for the laptop it will need to go to the class level and get the othher value.

