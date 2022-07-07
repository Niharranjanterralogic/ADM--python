
# pip install  requests

import requests

url = 'http://127.0.0.1:9999/api/students/'

student_obj = {
        "sname": "Rani",
        "marks": 75,
        "email": "rani@gmail.com",
        "mobile": 111112288,
        "address": "KPHB"
}

response = requests.get(url)
# response = requests.post(url, data=student_obj)

# id = input("enter any id : ")
# response = requests.get(url+id+'/')
# response = requests.put(url+id+'/', data=student_obj)
# response = requests.delete(url+id+'/')


if response.status_code == 200:
    try:
        dict_data = response.json()
    except:
        print("Status Code is : ", response.status_code)
        print("Sorry, Data is not came in json format")
    else:
        print("Status Code is : ", response.status_code)
        print(dict_data)

elif response.status_code == 201:
    try:
        dict_data = response.json()
    except:
        print("Status Code is : ", response.status_code)
        print("Sorry, Data is not came in json format")
    else:
        print("Status Code is : ", response.status_code)
        print(dict_data)

elif response.status_code == 404:
    print("Status Code is : ", response.status_code)
    print("Requested resource not available")

elif response.status_code == 204:
    print("Status Code is : ", response.status_code)
    print("Requested resource deleted successfully")

elif response.status_code == 400:
    print("Status Code is : ", response.status_code)
    print("Please send proper data")
else:
    print("Status Code is : ", response.status_code)
    print("Some thing wrong")





