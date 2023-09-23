from datetime import datetime
from tkinter import *

from Week3.Asignment.WeatherApp.API.api import get_current_weather, get_icon, get_forecast_weather
from PIL import Image, ImageTk


class WindowWeatherApp:

    def __init__(self):
        self.photo_images = []
        self.window = Tk()
        self.window.title("Weather App")
        self.window.geometry("700x500+10+10")

        self.update_datetime_label()

        self.city_label = Label(self.window, text="Enter city:")
        self.city_label.pack(pady=10)

        self.city_entry = Entry(self.window, font=("Helvetica", 14))
        self.city_entry.pack(pady=5)
        get_weather_button = Button(self.window, text="Get Current Weather", command=self.handle_get_weather_button)
        get_weather_button.pack(pady=10)

        self.weather_info_label = Label(self.window, text="", font=("Helvetica", 12), wraplength=500, justify=LEFT)
        self.weather_info_label.pack(pady=20)

        self.weather_icon_label = Label(self.window)
        self.weather_icon_label.pack()
        self.forecast_frame = Frame(self.window)
        self.forecast_frame.pack(pady=10)

        self.window.mainloop()


    def update_datetime_label(self):
        current_datetime = datetime.now().strftime("%B %d, %Y %H:%M:%S")
        self.datetime_label = Label(self.window, text=current_datetime, font=("Helvetica", 10))
        self.datetime_label.place(x=10, y=10)
        self.window.after(1000, self.update_datetime_label)  # Обновляем каждую секунду

    def display_icon(self, icon_url):
        image = Image.open(icon_url)
        photo = ImageTk.PhotoImage(image)

        self.weather_icon_label.config(image=photo)
        self.weather_icon_label.image = photo

    def handle_get_weather_button(self):
        try:
            city = self.city_entry.get()
            data = get_current_weather(q=city)
            weather_condition = data['condition']
            temperature = data['temperature']
            temp_feels_like = data['temp_feels_like']
            humidity = data['humidity']

            weather_info = f"Weather Condition: {weather_condition}\n" \
                           f"Temperature: {temperature}°C\n" \
                           f"Feels Like: {temp_feels_like}°C\n" \
                           f"Humidity: {humidity}%"

            self.weather_info_label.config(text=weather_info)

            img_data = get_icon(icon_url=f"https:{data['icon']}")
            photo = ImageTk.PhotoImage(img_data)

            self.weather_icon_label.config(image=photo)
            self.weather_icon_label.image = photo
            self.update_forecast(get_forecast_weather(q=city)["forecast"])
        except Exception as e:
            self.weather_info_label.config(text=f"Error: {str(e)}")

    def update_forecast(self, forecast_data):
        for i, day_data in enumerate(forecast_data[:3]):
            frame = Frame(self.forecast_frame)
            frame.grid(row=0, column=i, padx=10)
            date_str = day_data['date']
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            date_label = Label(frame, text=date_obj.strftime("%B %d, %Y "), font=("Helvetica", 12))
            date_label.pack()

            condition_label = Label(frame, text=day_data['condition'], font=("Helvetica", 10))
            condition_label.pack()

            max_temp_label = Label(frame, text=f"Max Temp: {day_data['max_temperature']}°C", font=("Helvetica", 10))
            max_temp_label.pack()

            min_temp_label = Label(frame, text=f"Min Temp: {day_data['min_temperature']}°C", font=("Helvetica", 10))
            min_temp_label.pack()

            img_data = get_icon(icon_url=f"https:{day_data['icon']}")
            photo = ImageTk.PhotoImage(img_data)
            self.photo_images.append(photo)

            icon_label = Label(frame, image=photo)
            icon_label.image = photo
            icon_label.pack()
