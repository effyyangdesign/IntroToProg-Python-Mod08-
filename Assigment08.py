# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (08/31/2020,Yizhou Yang,Assignment08):
# RRoot,1.1.2020,Created started script
# YYang,8.31.2020,finished assignment 8
# <Yizhou Yang>,<08/31/2020>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ''
Product_Name  =''
Product_Price =''

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (08/31/2020,Yizhou Yang,Assignment08)
        RRoot,1.1.2020,Created Class
        <YYang>,<08/31/2020>,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self,product_name,product_price):
        #-- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    @property
    def product_name (self):
        return str(self.__product_name).title()
    @product_name.setter
    def product_name(self,value):
        if str(Value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def product_price(self):
        return str(self.__product_price).title()

    @product_price.setter
    def product_price(self, value):
        self.__product_price = value

    # -- Methods --
    def __str__(self):
        return self.product_name + ',' + self.product_price

    def __doc__(self):
        return 'This class holds data about product name and price'

# --End of class--

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (08/31/2020,Yizhou Yang,Assignment08)
        RRoot,1.1.2020,Created Class
        <YYang>,<08/31/2020>,Modified code to complete assignment 8
    """
    pass

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        lstOfProductObjects.clear()  # clear current data
        file = open(file_name, "r")
        for row in file:
            lstOfProductObjects.append(row)
        file.close()

    @staticmethod
    def save_data_to_file(file_name, lstOfProductObjects):
        file = open(file_name, "w")
        for row in lstOfProductObjects:
            file.write(str(row)+"\n")

        file.close()

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Gather data from user:

        methods:
            print_menu_Tasks() -> display menu
            input_menu_choice() ->input inquery
            show_current_data_from_file(file_name)
            get_product_data()

    changelog: (08/31/2020,Yizhou Yang,Assignment08)
        RRoot,1.1.2020,Created Class
        <YYang>,<08/31/2020>,Modified code to complete assignment 8
        """
    pass
    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Add new product info
            2) Show current data from file
            3) Save Data to File        
            4) Exit Program
            ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def show_current_data_from_file(file_name):
        FileProcessor.read_data_from_file(file_name)
        for row in lstOfProductObjects:
            print(row)

    # TODO: Add code to get product data from user
    @staticmethod
    def  get_product_data():
        # Product_Name = input("Please Enter the Product Name")
        # Product_Price = input("Please Enter the Product Price")
        objloader = Product(product_name=input("Please Enter the Product Name"),product_price=input("Please Enter the Product Price"))
        lstOfProductObjects.append(objloader)

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
while(True):
    try:
        IO.show_current_data_from_file(file_name=strFileName)
        IO.print_menu_Tasks()
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':  # Add new Product Info
            IO.get_product_data()
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            lstOfProductObjects.clear()
            continue  # to show the menu


        elif strChoice == '2':  # Show current product info saved in file.
            IO.show_current_data_from_file
            continue  # to show the menu
            #
        elif strChoice == '3':  # Save Data to File
            strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
            if strChoice.lower() == "y":
                FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            else:
                print("Save Cancelled!")
            continue  # to show the menu


        elif strChoice == '4':  # Exit Program
            print("Goodbye!")
            break  # and Exit

    except FileNotFoundError as e:
       print ('No such file is found, check your folder')
       break


