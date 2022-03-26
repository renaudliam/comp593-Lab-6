import requests
def request():
    response = requests.head("https://pokeapi.co/api/v2/")


    if response.status_code == 200:
        print('Response:', response.status_code, "Connection Successful!" '\n')
    else:
        print('Uh Oh, got', response.status_code)

    print(response.headers)
