import requests


def main():
    poke_info = get_poke_info()
    if poke_info:
        pastebin_strings = get_pastebin_string(poke_info)
        pastebin(pastebin_strings)

def pastebin(pokemon_data):


    requestParams = {
        'api_dev_key': "DwQS1JEYBGxcXYYSx7feoTnngeyKFHeD",
        'api_option': "paste",
        'api_paste_code': pokemon_data,
        'api_paste_name': "Liam's Pokemon Data"
    }


    req = requests.post("https://pastebin.com/api/api_post.php", data=requestParams)
    if req.status_code == 200:
            print("Successful connection to PasteBin")
            print("Here's the link to the paste!!")
    else:
        print(req.status_code, "Failed to establish connection")
    print(req.text)
def get_pastebin_string(poke_info):
    weight = poke_info['weight']
    title = poke_info['name'] + "'s " "stats"
    print(title.title())
    poke = ''
    j = 0
    for i in poke_info['abilities']:

        if j != len(poke_info['abilities'])-1:
            poke += (i['ability']['name']) + "," " "
            j += 1
        else:
            poke += (i['ability']['name'])

    pokemon_data = "Abilities: " + poke + "\nWeight: " + str(weight)
    print(pokemon_data)
    return pokemon_data




def get_poke_info():
    pokemon = input("Enter a Pokemon")
    print("Getting pokemon information..." " ", end="")
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(pokemon))

    if response.status_code == 200:
        print("Success! You can find the details below!")
        return response.json()

    else:
        print('Connection failed...', response.status_code)
        print("Did you enter a valid pokemon name?")
        return get_poke_info()
main()