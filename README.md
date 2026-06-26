# 🌦️ Python Weather App with Voice

A simple Python application that fetches the current weather of any city using the WeatherAPI and speaks the weather information using text-to-speech.

## 🚀 Features

- Get current temperature
- Get current wind speed
- Get current humidity
- Voice output using Text-to-Speech
- Easy to use

## 🛠️ Technologies Used

- Python
- requests
- json
- pyttsx3
- WeatherAPI

## 📦 Requirements

Install the required libraries:

```bash
pip install requests pyttsx3
```

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/yourusername/weather-app.git
```

2. Open the project folder.

3. Install the required packages.

```bash
pip install requests pyttsx3
```

4. Replace the API key in the code with your own WeatherAPI key.

5. Run the program.

```bash
python weather.py
```

6. Enter the city name when prompted.

Example:

```
Enter a name of city: Delhi
```

## 📋 Sample Output

```
Enter a name of city: Delhi

Temperature: 35°C
Wind Speed: 12.6 kph
Humidity: 58%
```

The application will also announce the weather using your computer's speakers.

## 📂 Project Structure

```
weather-app/
│
├── weather.py
├── README.md
└── requirements.txt
```

## 🌐 API Used

This project uses the WeatherAPI to fetch live weather data.

https://www.weatherapi.com/

## ⚠️ Note

- Internet connection is required.
- Do not share your API key publicly.
- If an invalid city name is entered, the API will return an error.

## 💡 Future Improvements

- Add weather icons
- Show weather condition (Sunny, Rainy, etc.)
- GUI using Tkinter
- 5-day weather forecast
- Better error handling
- Save recent searches

## 👨‍💻 Author

**Bhavya Gupta**

B.Tech Artificial Intelligence & Machine Learning

Learning Python by building real-world projects.

⭐ If you like this project, consider giving it a star on GitHub!
