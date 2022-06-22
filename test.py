import requests

url = 'http://localhost:8000/chat/api/messages/'  # Полный адрес эндпоинта
response = requests.get(url)  # Делаем GET-запрос
# Поскольку данные пришли в формате json, переведем их в python
response_on_python = response.json()
# Запишем полученные данные в файл capitals.txt
# class ="w-100 mb-2 btn btn-lg rounded-4 btn-primary" name="next" value="login" type="submit" > Sign in < / button >
#print(requests.post('http://localhost:8000/login/', data={'username': 'gagaga', 'password': 'gagagagagagagagaga', 'next': 'login'}))
main_url = 'http://localhost:8000/'
with open('messages.txt', 'w') as file:
    for message in response_on_python:
        file.write(
            #f"message : {message['text']} is "
            #f"pub date : {message['pub_date']}, "
            f"author : {message['members']}\n"
        )
        print('1')