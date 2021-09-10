
# Here we will create a weather app using json and tkinter

# JSON (JavaScript Object Notation), specified by RFC 7159 and
# is a lightweight data interchange format inspired by JavaScript object literal syntax


# Since the API key is confidential we store the key in system environment variable

import json   
import tkinter as tk
import os
import requests


# url = api.openweathermap.org/data/2.5/weather?q={}&appid={}

# print(weather_api)

LIGHT_GRAY = '#F5F5F5'
LABEL_COLOR = '#25265E'
SMALL_FONT_STYLE =("Arial", 16)
LARGE_FONT_STYLE =("Arial", 24, "bold")
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
WHITE = '#FFFFFF'
OFF_WHITE = '#F8FAFF'
LIGHT_BLUE ='#CCEDFF'



class Weather:
    def __init__(self): # this is the constructor method
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Weather infos")
    
    
        # The weather infos
        self.url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        self.weather_api = os.environ['weatherAPI_key'] # retrive the API key from the system environment
        
       
        self.weather_data = {"city":"", "country":"", "temp_celsius":"", "temp_fahrenheit":""
                             , "icon": "", "weather": ""}
      
        
        
        self.photo = tk.PhotoImage(file='weather_icons/01d.png')
        
        self.getWeather(self.weather_data["city"])
        
        # Create two frames
        self.display_frame = self.create_display_frame() # To display the weather informations
        self.menu_frame = self.create_menu_frame()  # the select menu e.g, drop down menu to select location
        
        # Create the display labels
        self.display_labels = self.create_display_labels()
        
        # display labels variables
        self.location_label
        self.image_label
        self.temp_label
        self.weather_label
        
        
        
        # Update display labels
        # self.update_display_labels()
        
        # Create search entry box and button
        self.current_city = tk.StringVar()  # stirng variable class
        self.entry_search()
        self.button_search()
        
        
        #self.entry_box, self.current_city = self.entry_search()
    
    
    def search(self):
        CITY = self.current_city.get()
        # json_data = requests.get(self.url.format(CITY,  self.weather_api)).json()
        self.getWeather(CITY)
        self.update_display_labels()
        
    
    
    def getWeather(self, city):
        if (len(city)> 0):
            json_data = requests.get(self.url.format(city,  self.weather_api)).json()
  
            if json_data:
                city = json_data['name']
                country = json_data['sys']['country']
                temp_kelvin = json_data['main']['temp']
                temp_celsius = (temp_kelvin - 273.15)
                temp_fahrenheit = (temp_kelvin - 273.15)*(9/5) + 32
                icon = json_data['weather'][0]['icon']
                weather = json_data['weather'][0]['main']
                
                
                data = {"city":city, "country":country, "temp_celsius":temp_celsius,
                                     "temp_fahrenheit":temp_fahrenheit, "icon": icon, "weather": weather}

                
                self.weather_data = data
                
            else:
                print("none")
#         
        
        
        
        
        
    
    
    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 321, bg=LIGHT_GRAY)
        frame.pack(expand = True, fill= "both")
        return frame

    def create_menu_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill= "both")
        return frame
    
    
    
    
    def entry_search(self):
        entry_box = tk.Entry(self.menu_frame, textvariable = self.current_city)
        entry_box.pack()
        return entry_box
    
    
    def button_search(self):
        button = tk.Button(self.menu_frame, text='Search weather', width= 12, command=self.search)
        button.pack()
        return button
    
    
    def create_display_labels(self):
        location_label = tk.Label(self.display_frame, text='', font=SMALL_FONT_STYLE)
        location_label.pack()
        
        image_label = tk.Label(self.display_frame, image = self.photo)
        image_label.pack()
        
        temp_label = tk.Label(self.display_frame, text='Temperature', font=SMALL_FONT_STYLE)
        temp_label.pack()
        
        weather_label = tk.Label(self.display_frame, text='Weather', font= SMALL_FONT_STYLE)
        weather_label.pack()
        
        self.location_label = location_label
        self.image_label = image_label
        self.temp_label = temp_label
        self.weather_label = weather_label
        return location_label, image_label, temp_label, weather_label
    
    
    
    def update_display_labels(self):
        self.location_label['text'] = '{}, {}'.format(self.weather_data["country"], self.weather_data["city"])
        
       
        photo = tk.PhotoImage(file='weather_icons/{}.png'.format(self.weather_data["icon"]))
        self.photo = photo
        self.image_label['image'] = photo
        
        self.temp_label['text'] = '{:.2f}C'.format(self.weather_data["temp_celsius"])
        self.weather_label['text'] = '{}'.format(self.weather_data["weather"])
        
        
        
    
    
    
    def run(self):
        self.window.mainloop()
    
if __name__ == "__main__":
    calc = Weather()
    calc.run()