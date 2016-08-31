#strongly as well as weakly dominant strategy equi- librium of any n person matrix form game
import gambit
import sys
import numpy as np

class equilibria_finder:
	def __init__(self,path):
		g = gambit.read_game(path)
		contingencies = list(g.contingencies)
		#payoff matrix contains the key as action and payoff as values
		self.payoff_matrix = dict()
		self.actions =[]		
		self.players=len(g.players)
		for profile in g.contingencies:
			# print profile
			self.actions.append(profile)
			self.payoff_matrix[tuple(profile)] = [str(g[profile][i]) for i in range(len(g.players))]

		self.actions = np.array(self.actions)
		self.player_actions = dict()

		for player in range(len(g.players)): 
			self.player_actions[player]=len(np.unique(self.actions[:,player]))

		# print self.player_actions
		# print self.payoff_matrix
		# print self.actions
		# print self.players
		self.total = len(self.actions)


		#dim= tuple([ self.player_actions[i] for i in range(len(g.players))])
		# utility_matrix = np.zeros(dim)
		# for profile in g.contingencies:
		# 	print profile
		# 	utility_matrix[profile] = self.payoff_matrix[tuple(profile)]

	def find_dominant_strategy(self, i): 
		payoffs=[]
		for j in range(self.player_actions[i]):
			#print "for action ", j
			payoffs.append(np.array(map(lambda x: self.payoff_matrix[tuple(x)][i], self.actions[np.where(self.actions[:,i]==j)]),dtype=int))
		payoffs = np.array(payoffs)
		flag=True
		_max = 0
		_len = len(payoffs[0])
		# print payoffs, _len
		for k in range(1,len(payoffs)):
			# print payoffs[_max,:]
			# print payoffs[k,:]
			t = len(np.where(payoffs[_max,:]>=payoffs[k,:])[0])
			# print t
			if  t==0:
				_max = k
			if t<_len:
				if len(np.where(payoffs[k,:]>=payoffs[_max,:])[0])==_len:
					flag=False
					_max = k
					print "No strongly dominated strategy"

				else: 
					print "No dominant strategy"
					return
			if t==_len:
				flag=False
				print "No strongly dominated strategy"
		return _max

	def find_equilibria(self):
		#player1 dominant or weakly dominant
		answer = []
		for i in range(self.players):
			print "evaluating for player {0} ".format(i)
			t = self.find_dominant_strategy(i)
			if  t== None:
				 return
			else:
				answer.append(t)
		print " answer is ",answer			
			#[self.payoff_matrix[tuple(action)] for action in actions]

			



if __name__=="__main__": 
	t=sys.argv[1]
	e = equilibria_finder(sys.argv[1])
	e.find_equilibria()
