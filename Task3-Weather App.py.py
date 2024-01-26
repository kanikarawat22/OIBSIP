from tkinter import *

from tkinter import messagebox as mb

import requests

from PIL import Image

from datetime import datetime

root = Tk()

root.title('Weather Application')

root.configure(bg='royal blue1')

root.geometry("700x450")


def get_weather():
    global city
    city = city_input.get()
    api_key = 'd4e7f3cb936975eba1598838afd42824'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']-273.15
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = (data['wind']['speed'])*3.6
        epoch_time = data['dt']
        date_time = datetime.fromtimestamp(epoch_time)
        desc = data['weather'][0]['description']
        cloudy = data['clouds']['all']

        timelabel.config(text=str(date_time))
        temp_field.insert(0, '{:.2f}'.format(temp) + "celcius")
        pressure_field.insert(0, str(pressure) + "hPa")
        humid_field.insert(0, str(humidity) + "%")
        wind_field.insert(0, '{:.2f}'.format(wind) + "km/h")
        cloud_field.insert(0, str(cloudy) + "%")
        desc_field.insert(0, str(desc))
    else:
        mb.showerror("Error", "City Not Found.Enter a valid city name")
        city_input.delete(0, END)


def reset():
    city_input.delete(0,END)
    temp_field.delete(0,END)
    pressure_field.delete(0,END)
    humid_field.delete(0,END)
    wind_field.delete(0,END)
    cloud_field.delete(0,END)
    desc_field.delete(0,END)
    timelabel.config(text='')
    

def get_forecast():
    url1 = 'https://wttr.in/{}.png'.format(city)
    response1 = requests.get(url1)
    path = 'forecast_weather.png'
    if response1.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response1.content)
            im = Image.open(path)
            im.show()

title = Label(root, text='Weather detection and forecast', fg='yellow', bg='royal blue1', font=("bold", 15))

label1 = Label(root, text='Enter the City name : ', font=('bold', 12), bg='royal blue1')

city_input = Entry(root, width=24, fg='red2', font=12, relief=GROOVE)

timelabel = Label(root, text='', bg='royal blue1', font=('bold', 14), fg='yellow')
              

btn_submit = Button(root, text='Get Weather', width=10, font=12, bg='lime green', command= get_weather)

btn_forecast = Button(root, text='Weather forecast', width=14, font=12, bg='lime green', command= None)

btn_reset = Button(root, text='Reset', font=12, bg='lime green', command= reset)


label2 = Label(root, text="Temperature : ", font=('bold', 12), bg='royal blue1')
              
label3 = Label(root, text="Pressure : ", font=('bold', 12), bg='royal blue1')

label4 = Label(root, text="Humidity : ", font=('bold', 12), bg='royal blue1')

label5 = Label(root, text="Wind : ", font=('bold', 12), bg='royal blue1')

labeló = Label (root, text="Cloudiness : ", font=('bold', 12), bg='royal blue1')

label7 = Label (root, text="Description : ", font=('bold', 12), bg='royal blue1')



temp_field = Entry(root, width=24, font=11)

pressure_field = Entry(root, width=24, font=11)

humid_field = Entry(root, width=24, font=11)

wind_field = Entry(root, width=24, font=11)

cloud_field = Entry(root, width=24, font=11)

desc_field = Entry(root, width=24, font=11)


title.grid(row=0, column=1, padx=10, pady=10)

label1.grid(row=1, column=0, padx=10, pady=10)

timelabel.grid(row=1, column=2)

btn_submit.grid(row=2, column=1, pady=5)

btn_forecast.grid(row=2, column=2, pady=5)

label2.grid(row=3, column=0, padx=5, pady=5, sticky='w')

label3.grid(row=4, column=0, padx=5, pady=5, sticky='w')

label4.grid(row=5, column=0, padx=5, pady=5, sticky='W')

label5.grid(row=6, column=0, padx=5, pady=5, sticky='w')

labeló.grid(row=7, column=0, padx=5, pady=5, sticky='W')

label7.grid(row=8, column=0, padx=5, pady=5, sticky='W')


city_input.grid(row=1, column=1, padx=5, pady=5)

temp_field.grid(row=3, column=1, padx=5, pady=5)

pressure_field.grid(row=4, column=1, padx=5, pady=5)

humid_field.grid(row=5, column=1, padx=5, pady=5)

cloud_field.grid(row=7, column=1, padx=5, pady=5)

desc_field.grid(row=8, column=1, padx=5, pady=5)

btn_reset.grid(row=9, column=1, pady=5)
              

root.mainloop()

