from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

CITY = "Vladimir,RU"
API_KEY = "492392ecf3ad69f1072d69ef722d721c" 

@app.route('/weather')
def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # 自定义响应格式
        return jsonify({
            "город": data['name'],
            "страна": data['sys']['country'],
            "температура": f"{data['main']['temp']}°C",
            "ощущается": f"{data['main']['feels_like']}°C",
            "погода": data['weather'][0]['description'],
            "влажность": f"{data['main']['humidity']}%",
            "ветер": f"{data['wind']['speed']} м/с",
            "обновлено": data['dt']
        })
    except Exception as e:
        return jsonify({"ошибка": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)