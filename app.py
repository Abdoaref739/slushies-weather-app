from flask import Flask, render_template, request
import requests as req

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather', methods=['POST', 'GET'])
def weather():
    YOUR_API_KEY = '6a8bff312dd44090b95174750251308'
    city_name = request.form.get('city-input-field')
    url = f'http://api.weatherapi.com/v1/current.json?key={YOUR_API_KEY}&q={city_name}&aqi=no'
    if city_name == '' or city_name is None:
         return render_template('weather.html', city_name='Please enter a city name', city_region='NULL', city_country='NULL', city_localtime='NULL', city_temp_c='NULL', city_temp_f='NULL', city_condition='NULL', city_icon='NULL', city_wind_mph='NULL', city_wind_kph='NULL', city_humidity='NULL', city_pressure_mb='NULL', city_pressure_in='NULL')
    else:
        response = req.get(url)
        final_data = response.json()
        return render_template('weather.html', city_name=final_data['location']['name'], city_region=final_data['location']['region'], city_country=final_data['location']['country'], city_localtime=final_data['location']['localtime'], city_temp_c=final_data['current']['temp_c'], city_temp_f=final_data['current']['temp_f'], city_condition=final_data['current']['condition']['text'], city_icon=final_data['current']['condition']['icon'], city_wind_mph=final_data['current']['wind_mph'], city_wind_kph=final_data['current']['wind_kph'], city_humidity=final_data['current']['humidity'], city_pressure_mb=final_data['current']['pressure_mb'], city_pressure_in=final_data['current']['pressure_in'])

@app.route('/about')
def history():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(port=5000, debug=True)