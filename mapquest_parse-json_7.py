import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "CLEOBL0GrYWUqQ1hKIOdbp4mE6XMAY35" #Replace with MapQuest key

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + color.BOLD + (orig) + color.END + " to " + color.BOLD + (dest) + color.END)
        print(color.BOLD + "Trip Duration: " + color.END + "" + color.GREEN + (json_data["route"]["formattedTime"]) + color.END)
        print(color.BOLD + "Kilometers:: " + color.END + "" +  color.GREEN + str("{:.2f}".format((json_data["route"]["distance"])*1.61)) + color.END)
        print(color.BOLD + "Fuel Used (Ltr): " + color.END + "" +  color.GREEN + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)) + color.END)
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")