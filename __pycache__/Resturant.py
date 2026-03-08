#Import tkinter for GUI and ttk for improved widgets
import tkinter as tk
from tkinter import ttk, messagebox

#Define the RestaurantOrderManagementApp class
class RestaurantOrderManagement:
     #Intialize the application
     def __init__(self, root):
          self.root = root #the main video of the app 
          self.root.title("Restaurant Management App")#set the title of the window

          #A dictionary to store the menu items and there prices 
          self.menu_items = {
               "PIZZA": 4,
               "LUNCH": 5,
               "DOHNER KEBAB MEAL": 4,
               "DINNER": 5,
               "CODINGAL MEAL": 10,
               "DRINKS": 1,
               "SWEETS": 2
          }
          self.exchange_rate = 82 #Exchange rate for currency version
          self.setup_background(root) #Set up the background image

          #Create a frame to hold the widgets
          frame = ttk.Frame(root)
          frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

          #Heading label
          ttk.Label(
               frame,
               text="Restaurant Order Management"
               font=("Altone Arial", 20, "bold")
          ).grid(row=0, columnspan=3, padx=10, pady=10)

          self.menu_labels = {}    #To store references to menu item labels
          self.menu_quantities = {}  #to store references to quantity entry widgets

