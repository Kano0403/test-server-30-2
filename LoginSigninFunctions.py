#Imports
import hashlib
import json
import string
from random import *
from datetime import datetime
filepath="test.json"
LogFilepath="UserLogs.json"
 
#Checking the inputed username and password against 
def UsernameCheck(Username,Password):
    # Writing to sample.json
    with open(filepath, "r") as openfile:
        #json_object = json.load(openfile)
        InfoFile = json.load(openfile)

    #Iteration through each userID
    for key in InfoFile["userID"].keys():
        #Testing if inputed user information if correct through hashs
        if hashlib.sha256((InfoFile["userID"][key]["seed"]+Username).encode()).hexdigest()==InfoFile["userID"][key]["Username"] and hashlib.sha256((InfoFile["userID"][key]["seed"]+Password).encode()).hexdigest()==InfoFile["userID"][key]["Password"]:
            #Runs when its verifies
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            with open(LogFilepath, "r") as TimeFile:
                #json_object = json.load(openfile)
                TimeFileOpen = json.load(TimeFile)
            NameofUser=TimeFileOpen["userID"][key]["name"]
            TimeRecord={
                "Username":Username,
                "Name": NameofUser,
                "Time" : current_time
            }

            TimeFileOpen.update(TimeRecord)

            json_objecttime = json.dumps(TimeFileOpen, indent=1)

            with open(LogFilepath, "w") as outfileTime:
                outfileTime.write(json_objecttime)

            return TimeFileOpen["userID"][key]
        else:
            #Runs when its not correct
            return None


def SignIn(Username,Password,Name,Email):
    GoodToGo=True
    min_char = 15
    max_char = 20
    seed = "".join(choice(string.ascii_letters + string.punctuation + string.digits) for x in range(randint(min_char, max_char)))
    Username=seed+Username
    Password=seed+Password
    Username=hashlib.sha256(Username.encode()).hexdigest()
    Password=hashlib.sha256(Password.encode()).hexdigest()
    with open(filepath, "r") as openfile:
        #json_object = json.load(openfile)
        InfoFile = json.load(openfile)
    for key in InfoFile["userID"].keys():
        #Testing if inputed user information if correct through hashs
        if hashlib.sha256(Username.encode()).hexdigest()==InfoFile["userID"][key]["Username"]:
            GoodToGo=False
    #Runs only if username is not taken
    if GoodToGo:
        Appendage = {
            Email:{
            "Username": Username,
            "Password": Password,
            "Access": "TBD",
            "Name": Name,
            "Email": Email,
            "seed": seed
            }
        }

        InfoFile["userID"].update(Appendage)

        json_object = json.dumps(InfoFile, indent=4)

        #Writing to sample.json
        with open(filepath, "w") as outfile:
            outfile.write(json_object)
        return True
    #Runs only if username is taken
    else:
        return False

def UsernameTaken(Username):
    GoodToGoBoogaloo=True

    with open(filepath, "r") as openfile:
        #json_object = json.load(openfile)
        InfoFile = json.load(openfile)

    seed=InfoFile["userID"][key]["seed"]

    Username=seed+Username

    for key in InfoFile["userID"].keys():
        #Testing if inputed user information if correct through hashs
        if hashlib.sha256(Username.encode()).hexdigest()==InfoFile["userID"][key]["Username"]:
            GoodToGoBoogaloo=False
    
    if GoodToGoBoogaloo:
        return True
    else:
        return False