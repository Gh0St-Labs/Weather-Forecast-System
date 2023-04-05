import requests

API_KEY = "d471bf748136949f513f623b3664ed2e"
def snatch_data(place, days=None, type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    the_data = response.json()
    filtered_data = the_data['list']
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]

    if type == 'Temperature':
        filtered_data = [temps['main']['temp'] for temps in filtered_data]

    if type == 'Atmospheric':
        filtered_data = [atmos['weather'][0]['main'] for atmos in filtered_data]

    return filtered_data



if __name__ == "__main__":
    print(snatch_data("London", days=3, type='Temperature'))
