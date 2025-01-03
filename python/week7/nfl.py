nfl = [
     {
          "name": "Chiefs",
          "founded_year": 1920,
          "is_active": False,
          "players": [
               {
               "name": "Patrick Mahomes",
               "age": 26,
               "touchdowns": 20,
               "rushing_yards": 100,
               "passing_yards": 20
               },

               {
               "name": "Travis Kelce",
               "age": 26,
               "touchdowns": 5,
               "rushing_yards": 150,
               "passing_yards": 0

               },
          ]
     }
]

def addTeam():
     global nfl
     team_name = input("Enter the Team's Name: ")
     for value in nfl:
          if value["name"] == team_name:
               print(" The team name already exists.")
               return

     nfl.append({
          "name": team_name,
          "players": [],
          "year_founded": 0,
          })
     print("Team added successfully!")
     return

def addPlayer():
     global nfl
     team_name = input("Enter the Team's Name: ")
     exists = False
     for value in nfl:
          if value["name"] == team_name:
               exists = True
               player_name = input("Enter the Player's Name: ")
               if (player_name == ""):
                    print("The player name can't be empty.")
                    return
               value["players"].append({
                    "name": player_name,
                    "age": 0,
                    "touchdowns": 0,
                    "rushing_yards": 0,
                    "passing_yards": 0
                    })

     if not exists:
          print("The team does not exist")
          return


def updatePlayer():
     return

def viewTeamStats():
     return

def viewPlayerStats():
     return

#print(nfl[0])
#print(nfl[0]["name"])
#print(nfl[0]["players"][1])


while (True):

     print("Welcome to the NFL Menu program")
     print("1.- Add a team")
     print("2.- Add a player")
     print("3.- Update player stats")
     print("4.- View team stats")
     print("5.- View player stats")
     print("6.- Exit Code")
     print("------------------------------")

     choice = int(input("Select your choice: "))

     if choice == 1:
          addTeam()
     elif choice == 2:
          addPlayer()
     elif choice == 3:
          updatePlayer()
     elif choice == 4:
          viewTeamStats
     elif choice == 5:
          viewPlayerStats()
     elif choice == 6:
          print("Program ended")
          break
     else:
          print("Enter a valid option")