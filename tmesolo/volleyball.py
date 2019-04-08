# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu
from tools  import SimpleStrategy,SuperState
from soccersimulator.settings  import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS,BALL_RADIUS
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        return SoccerAction(acceleration=Vector2D.create_random(-1, 1),
                            shoot=Vector2D.create_random(-1, 1))

def gobettervolley(state) : 
    if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
        return SoccerAction(shoot=(state.near-state.player).normalize()*4)
    else :
        return SoccerAction(acceleration=state.ballameliorer-state.player)

def gobetteratt(state) : 
    if state.player.distance(state.ball)<PLAYER_RADIUS + BALL_RADIUS :
        return SoccerAction(shoot=state.near-state.player)
    else :
        return SoccerAction(acceleration=state.ballameliorer-state.player)



    
def echauffement(state):
    if state.teamdef[1] : 
        return SoccerAction(Vector2D(GAME_WIDTH*(state.teamdef[0]), (state.ballameliorer.y+state.goal.y)/2 )-state.player, state.goal-state.player)
    else :
        return gobettervolley(state)
  
    
    
def attaquant(state):
    if state.teamdef[1] : 
        return SoccerAction(Vector2D(GAME_WIDTH*(state.teamdef[0]), (state.ballameliorer.y+state.goal.y)/2 )-state.player, state.goal-state.player)
    else :
        return gobetteratt(state)
  
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

"""
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", RandomStrategy())  # Random strategy
team2.add("Player 2", RandomStrategy())   # Random strategy
"""

def get_team (nb_players,nb):
    team = SoccerTeam(name = "Alex’s Team")
    if (nb_players == 1 and nb==0):
        team.add("Echauffement",SimpleStrategy(echauffement,'One'))
    if (nb_players == 1 and nb==2):
        team.add("attaquant",SimpleStrategy(echauffement,'att'))        
        

    return team
# Create a match
team1 = get_team(1,0)
team2= get_team(1,2)
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
