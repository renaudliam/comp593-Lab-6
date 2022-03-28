import requests


def main():


    poke_info = get_poke_info()

    if poke_info:

        print("Weight:", poke_info['weight'])
        print("Ability 1:", poke_info["abilities"][0]['ability']["name"])
        print("Ability 2:", poke_info['abilities'][1]['ability']["name"])
        print("Height:", poke_info['height'])





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