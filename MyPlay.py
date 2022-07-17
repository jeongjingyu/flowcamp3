import MyPong # My PyGame Pong Game 
import MyAgent # My DQN Based Agent
import numpy as np 
import random 
import matplotlib.pyplot as plt
import pickle
import pygame
#
# =======================================================================
#   DQN Algorith Paramaters 
ACTIONS = 3 # Number of Actions.  Acton istelf is a scalar:  0:stay, 1:Up, 2:Down
STATECOUNT = 5 # Size of State [ PlayerYPos, BallXPos, BallYPos, BallXDirection, BallYDirection] 
TOTAL_GAMETIME = 20000
# =======================================================================
# Normalise GameState
def CaptureNormalisedState(PlayerYPos, BallXPos, BallYPos, BallXDirection, BallYDirection):
	gstate = np.zeros([STATECOUNT])
	gstate[0] = PlayerYPos/400.0	# Normalised PlayerYPos
	gstate[1] = BallXPos/400.0	# Normalised BallXPos
	gstate[2] = BallYPos/400.0	# Normalised BallYPos
	gstate[3] = BallXDirection/1.0	# Normalised BallXDirection
	gstate[4] = BallYDirection/1.0	# Normalised BallYDirection
	
	return gstate
# =====================================================================
# Main Experiment Method 
def Play(n):
    
	with open("test_exp_replay_"+str(n), "rb") as fp:
		exp_replay = pickle.load(fp)
	
	#Create our PongGame instance
	TheGame = MyPong.PongGame()
    # Initialise Game
	TheGame.InitialDisplay()
 	#  Create our Agent (including DQN based Brain)
	TheAgent = MyAgent.Agent(STATECOUNT, ACTIONS)
	TheAgent.Load(exp_replay, n)
	
	# Initialise NextAction  Assume Action is scalar:  0:stay, 1:Up, 2:Down
	BestAction = 0
	
	# Initialise current Game State ~ Believe insigificant: (PlayerYPos, BallXPos, BallYPos, BallXDirection, BallYDirection)
	GameState = CaptureNormalisedState(200.0, 200.0, 200.0, 1.0, 1.0)
 
	for gtime in range(TOTAL_GAMETIME):
     
		BestAction = TheAgent.ActP(GameState)
		[RightScore, LeftScore, PlayerYPos, BallXPos, BallYPos, BallXDirection, BallYDirection]= TheGame.PlayNextMoveP(BestAction)
		NextState = CaptureNormalisedState(PlayerYPos, BallXPos, BallYPos, BallXDirection, BallYDirection)
		GameState = NextState
  
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
	
		if RightScore == 11:
			return 1
		elif LeftScore == 11:
			return 0