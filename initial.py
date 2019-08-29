import requests

api_key = "b835ff1f349d4dbb8b5e138e9a99b25b"

print("Welcome to the Kitchen Club!", end = "\n \n")

ingredient = input("What ingredient would you like to use today? ")
print("\n    Great choice! \n")
recipes = int(input("How many recipes do you want? "))
print("")

parameters = {'query' : ingredient, 'number' : recipes, 'apiKey' : api_key}

# Make a get request to get the latest position of the international space station from the opennotify api.
r = requests.get('https://api.spoonacular.com/recipes/search', params = parameters)

data = r.json()
print(data)

for i in range(recipes):
    print(data['results'][i]['title'])

for i in range(recipes):
    print(data['results'][i]['id'])

















#
