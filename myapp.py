import requests
BASE_URL='http://127.0.0.1:8000/'
End_POINT='api/'
'''def get_res(id):

    res=requests.get(BASE_URL+End_POINT+id)


    print(res.json())
    print(res.status_code)

id=input('Enter ID : ')
get_res(id)'''
#def get_res():

#    res=requests.get(BASE_URL+End_POINT)
#    print(res.json())
#get_res()
import json

def post_res():
    add_emp = {
        'Ename': 'Rasmita',
        'Ejob': 'Tester',
        'ESal': 34000,
        'Eaddr': 'Hyb',
    }

    headers = {
        'Content-Type': 'application/json'  # Important!
    }

    res = requests.post(BASE_URL + End_POINT, data=json.add_emp, headers=headers)
    print(res.status_code)
    print(res.json())
