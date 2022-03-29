import requests


def main():


    poke_info = get_poke_info()
    if poke_info:
        pastebin_strings = get_pastebin_string(poke_info)
        pass
def get_pastebin_string(poke_info):

    title = poke_info['name'] + "'s " "stats"
    print(title)
    for i in poke_info['abilities']:
        print(i['ability']['name'])
    weight = poke_info['weight']

    print(weight)

















def get_poke_info():
    pokemon = input("Enter a Pokemon")
    print("Getting pokemon information..." " ", end="")
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(pokemon))

    if response.status_code == 200:
        print("Success! You can find the details below!")
        return response.json()

    else:
        print('Connection failed...', response.status_code)
        return

main()