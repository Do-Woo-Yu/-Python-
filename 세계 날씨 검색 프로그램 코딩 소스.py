import tkinter as tk
from tkinter import *
import requests

Height = 690 # 실행창 높이 조절
Width = 350  # 실행창 길이 조절

def get_weather(city):
    weather_key = 'b12bc74b30d718b2c05ecf27b5c35593'  # openweather API key
    url = 'https://api.openweathermap.org/data/2.5/weather' # openweather url 여기서 날씨 정보를 얻어옴
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'} 
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)


def format_response(weather):
    try:
        name = weather['name'] # 지역 이름 
        dec = weather['weather'][0]['description'] # 지역 날씨 정보
        temper = weather['main']['temp'] # 지역 기온 정보

        # 영어 번역한것
        
        if dec == 'overcast clouds' :
            dec = '흐린 구름'
        elif dec == 'moderate rain' :
            dec = '비 조금'
        elif dec == 'light rain' :
            dec = '맑은 날씨에 비'
        elif dec == 'clear sky' :
            dec = '맑은 하늘'
        elif dec == 'broken clouds' :
            dec = '깨진 구름'

            
        # 날씨에 따른 코디 알려주는 부분(온도가 몇도 이상이거나 이하면 아래와 같은 코디 추천)
        
        if int(temper) >= int(30) :
            cody = '폭염이므로 외출자제를'
            
        elif 20 <= int(temper) < int(30) :
            cody = '긴바지에 반팔'

        elif 15 <= int(temper) < 20 :
            cody = '긴바지에 외투'

        elif int(temper) <= 10 :
            cody = '긴바지에 패딩'

        # 도시이름, 도시 날씨, 도시 온도, 코디 를 입력받는 부분
        final_str = '도시: %s \n\n날씨: %s \n\n온도:%s(°C)\n\n 코디:%s추천합니다!' % (name, dec, temper, cody)

        # 도시이름을 잘못 입력했을때 출력
    except:
        final_str = '다시 입력해주세요.'
        # 도시이름, 도시 날씨, 도시 온도, 코디 출력해주는 부분
    return final_str


# http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}


root = tk.Tk()

root.title("세계 날씨 검색 프로그램") # tk창 실행시 창 이름 설정

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

background_image = tk.PhotoImage(file='weather image.png') # 배경 사진 선택
background_label = tk.Label(root, image=background_image)

background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, text='Search', font=40, command=lambda: get_weather(entry.get()))  # 검색(Search) 버튼 설정
button.place(relx=0.7, relwidth=0.3, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=("휴먼매직체", 13)) # 출력 글씨체와 글씨 크기 설정
label.place(relwidth=1, relheight=1)

# print(tk.font.families())


root.mainloop()
