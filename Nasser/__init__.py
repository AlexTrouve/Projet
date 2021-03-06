from Nasser.strategies import defenseur2 , RandomStrategy , gobetter,attaquant2 ,one, gardien, milieu1, defenseur3, defenseur4, attaquant3, attaquant4,attaquant5,defenseur5,milieu2
from soccersimulator import SoccerTeam
from Nasser.tools import SimpleStrategy, SuperState, GoTestStrategy

def get_team (nb_players):
    team = SoccerTeam(name = "Nasser’s Team")
    if (nb_players == 1):
        team.add("One",SimpleStrategy(one,'One'))
    if (nb_players == 2):
        team.add("Attaquant",SimpleStrategy(attaquant2,'Att'))
        team.add("Défenseur",SimpleStrategy(defenseur2,'Def'))
    if (nb_players == 4): 
        team.add("Nasser0",SimpleStrategy(defenseur5,'Def5'))
        team.add("Nasser1",SimpleStrategy(milieu1,'m1'))
        team.add("Nasser2",SimpleStrategy(milieu2,'m2'))
        team.add("Nasser3",SimpleStrategy(attaquant5,'Att5'))
    return team
