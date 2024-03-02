import requests
from bs4 import BeautifulSoup

# Статических сайтов с погодой нет, поэтому я написал рандомные слова по типу example. Пришлосб сымпровизировать

#                              part a
# response = requests.get("https://www.example.com/weather")
#
# if response.status_code == 200:
#     html_content = response.text
#
#     start = html_content.find("Astana:")
#     end = html_content.find("</div>", start)
#     weather = html_content[start:end]
#
#     weather_data = weather.split()[1]
#     print(weather_data)


# Тоже самое со вторым заданием

#                                part b
response = requests.get("https://www.example.com/weather")

if response.status_code == 200:
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    weather_data = soup.find(text='Astana').find_next_sibling('div').text
    print(weather_data)