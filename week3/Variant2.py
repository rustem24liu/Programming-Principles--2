class Activity:
    def __init__(self, exercise):
        self.exercise_ = exercise
    def printInFo(self):
        print("main exercise -", self.exercise_)

#activity
#exercise 
#printInfo
class Sportsmen(Activity):
    def __init__(self,exercise, id, name):
        super().__init__(exercise)
        self.id_ = id
        self.name_ = name
    def printInfo(self):
        print("ID of sport is -", self.id_)
        print("Name of the sportsman -", self.name_)
    def set_Type(self, type):
        self.type = type
    def get_Type(self):
        print("Type of the sport is: ")
        print(self.type)
        print("Main exercise is:")
        print(self.exercise_)
    
        
class TeamSport(Sportsmen):
    def __init__(self,exercise ,id, name, num_players):
        super().__init__(exercise, id, name)
        self.numplayers = num_players
    def printInfoo(self):
        print("Total informations:")
        print("ID-", self.id_)
        print("Name-", self.name_)
        print("Number of players-", self.numplayers)
        print()
        print("Main exercise is:")
        print(self.exercise_)

class Football(TeamSport):
    def __init__(self,exercise,  id, name, num_players, name_team):
        super().__init__(exercise, id, name, num_players)
        self.nameteam = name_team
    def printInfooo(self):
        print("Finally INFORMATION:")
        print("ID-", self.id_)
        print("NAME-", self.name_)
        print("Number of players-", self.numplayers)
        print("TEAM name-", self.nameteam)
        print("Main exercise is:")
        print(self.exercise_)
        
        # print(self.id_, self.name_, self.numplayers, self.nameteam)

   
w = Activity("jump")
w.printInFo()    
y = Sportsmen( "jump",7979, "Arnold")
y.printInfo()
y.set_Type("football")
y.get_Type()
x = TeamSport("jump",7979, "Arnold", 11)
x.printInfoo()
z = Football("jump", 7979, "Arnold", 11, "Qazaqstan")
z.printInfooo()


    