# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu
from tools2  import SimpleStrategy,SuperState
from soccersimulator.settings  import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS,BALL_RADIUS
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        return SoccerAction(acceleration=Vector2D.create_random(-1, 1),
                            shoot=Vector2D.create_random(-1, 1))


#|--------------------------------------------------------------------------------------------------------------------------------------------------------|        
#|                                              | Pour l'échauffement|                                                                                    |   
#|--------------------------------------------------------------------------------------------------------------------------------------------------------| 
    
def echauffement(state):
    if state.teamatt[1] : 
        return SoccerAction(Vector2D(GAME_WIDTH*(state.teamatt[0]), (state.ballameliorer.y+state.goal.y)/2 )-state.player, state.goal-state.player)
    else :
        return gobetterechauf(state)

def gobetterechauf(state) : 
    if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
        return SoccerAction(shoot=(state.near-state.player).normalize()*4)
    else :
        return SoccerAction(acceleration=state.ballameliorer-state.player)  





#|--------------------------------------------------------------------------------------------------------------------------------------------------------|        
#|                                              | Pour le 1v1        |                                                                                    |   
#|--------------------------------------------------------------------------------------------------------------------------------------------------------| 
def gobetterone(state):
    if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
        return SoccerAction(shoot=(state.goal-state.player))
    else :
        return SoccerAction(acceleration=state.ballameliorer-state.player)    

def one(state) :       
    if state.teamatt[1] :
        return SoccerAction(Vector2D(GAME_WIDTH*(state.teamatt[0]), (state.ballameliorer.y+state.goal.y)/2 )-state.player, state.goal-state.player)
    else :
        return gobetterone(state)    




#|--------------------------------------------------------------------------------------------------------------------------------------------------------|        
#|                                              | Pour le 2v2        |                                                                                    |   
#|--------------------------------------------------------------------------------------------------------------------------------------------------------| 

def attaquant(state):
    if state.teamatt[1] :
        return SoccerAction(Vector2D(GAME_WIDTH*(state.teamatt[0]), (state.ballameliorer.y+state.goal.y)/2 )-state.player, state.goal-state.player)
    else :
        return gobettervolley(state)
 

def defenseur(state):
    if state.teamdef[1] :
        return SoccerAction(Vector2D(GAME_WIDTH*(state.teamdef[0]), (state.ballameliorer.y+state.goal.y)/2 )-state.player, state.goal-state.player)
    else :
        return gobetterdef(state)
   
def gobetterdef (state):
    if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
        return SoccerAction(shoot=(state.coequipier2-state.player).normalize()*4)
    else :
        return SoccerAction(acceleration=state.ballameliorer-state.player) 

def gobetteratt(state) : 
    if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
       if state.ouest == True :
            return SoccerAction(shoot=(state.goal-state.player))
       else:
            return SoccerAction(shoot=(state.near-state.player))
           
    else :
        return SoccerAction(acceleration=state.ballameliorer-state.player)


  
 
def gobettervolley(state) : 
    if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
        return SoccerAction(shoot=(state.goal-state.player))
    else :
        return SoccerAction(acceleration=state.ballameliorer-state.player)    
       
    

#|--------------------------------------------------------------------------------------------------------------------------------------------------------|        
#|                                              | Création partie    |                                                                                    |   
#|--------------------------------------------------------------------------------------------------------------------------------------------------------|        
    
def get_team (nb_players,nb):
    team = SoccerTeam(name = "Alex’s Team")
    if (nb_players == 1 and nb==0):
        team.add("Echauffement",SimpleStrategy(echauffement,'One'))
    if (nb_players == 1 and nb==2):
        team.add("attaquant",SimpleStrategy(echauffement,'att'))        
    
    if (nb_players == 2 and nb==0):
        team.add("Defenseur",SimpleStrategy(defenseur,'One'))
        team.add("attaquant",SimpleStrategy(attaquant,'One'))
        
    if (nb_players == 2 and nb==2):
        team.add("Defenseur",SimpleStrategy(defenseur,'One'))   
        team.add("attaquant",SimpleStrategy(attaquant,'One'))
           
                

    return team
# Create a match
team1 = get_team(1,2)
team2= get_team(1,0)
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
