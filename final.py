import resources
 
API_key = "544624d1b442fb4e4776388a59bb477e"
base_url = "http://api.openweathermap.org/data/2.5/forecast?"
 
print("Welcome to WEATHER R US")
userinput = input(" please enter a Zip code or city and state")
if( userinput.isdigit()):
    zip_code = userinput
else:
    city = userinput
Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code
 
forecasts = requests.get(Final_url).json()
 
print("\nCurrent Weather Data Of " + zip_code +":\n")
pprint(forecasts)
#not sure if this works my computer isn't downloading the request files
#not sure what to do next
