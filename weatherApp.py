from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import geocoder

root= Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def getWeather(city: str):
    try:
     #city=textfield.get()
     print(city)
     geolocator =Nominatim(user_agent="weatherapp")
     location= geolocator.geocode(city)
     obj=TimezoneFinder()
     result= obj.timezone_at(lng=location.longitude, lat=location.latitude)

     home=pytz.timezone(result)
     local_time= datetime.now(home)
     current_time=local_time.strftime("%I: %M %p")
     clock.config(text=current_time)
     name.config(text="Current Weather")

     #the weather
     key="7736f9660dbed83f556e3b179a64145a"
     api="https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid=7736f9660dbed83f556e3b179a64145a"
 
     data=requests.get(api).json()
     print(data)
     condition= data["weather"][0]["main"]
     description= data["weather"][0]["description"]
     temp=int(data["main"]["temp"]-273.15)
     pressure= data["main"]["pressure"]
     humidity= data["main"]["humidity"]
     wind= data["wind"]["speed"]

     t.config(text=(temp, "°"))
     c.config(text=(condition, "|", "Feels", "Like",temp,"c"))
     w.config(text=wind)
     w2.config(text=humidity)
     w3.config(text=description)
     w4.config(text=pressure)
    except Exception as e:
       messagebox.showerror("Weather App", "Invalid Entry!")
def getlocation():
   location=geocoder.ip("me")
   textfield.insert(0, location.city)
   return location.city


       

#search box
Search_image= PhotoImage(file="search.png")
myimage=Label(image= Search_image)
myimage.place(x=20, y=20)

textfield=tk.Entry(root, justify='center', width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon= PhotoImage(file="search_icon.png")
myimage_icon=Button(image= Search_icon, borderwidth=0, cursor="hand2",bg="#404040" , command= lambda: getWeather(textfield.get()))
myimage_icon.place(x=370, y=34)

Location_icon=PhotoImage(file="location.png")
Location= Button(image= Location_icon,border=0, bg="#404040" ,fg="white", cursor="hand2", command= lambda: getWeather(getlocation())) 
Location.place(x=425, y=45)
#Logo
Logo_image=PhotoImage(file="logo.png")
logo= Label(image=Logo_image)
logo.place(x=150, y=100)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage= Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

#time
name=Label(root, font=("arial", 15, "bold"))
name.place(x=30 , y=100)
clock=Label(root, font=("Helvetica",20))
clock.place(x=30, y=130)

#label
label1=Label(root , text="Wind",font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2=Label(root , text="Humidity",font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3=Label(root , text="Description",font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4=Label(root , text="Pressure",font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t=Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c=Label(font=("arial", 15,'bold'))
c.place(x=400, y=250)

w=Label (text="...", font=("arial",20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

w2=Label (text="...", font=("arial",20, "bold"), bg="#1ab5ef")
w2.place(x=250, y=430)

w3=Label (text="...", font=("arial",20, "bold"), bg="#1ab5ef")
w3.place(x=430, y=430)

w4=Label (text="...", font=("arial",20, "bold"), bg="#1ab5ef")
w4.place(x=650, y=430)


root.mainloop()