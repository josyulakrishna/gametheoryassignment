#strongly as well as weakly dominant strategy equi- librium of any n person matrix form game
import gambit
import sys

class equilibria_finder:
	def __init__(self,path):
		g = gambit.read_game(path)
		contingencies = list(g.contingencies)
		self.payoff_matrix = dict()
		for profile in g.contingencies:
			self.payoff_matrix[tuple(profile)] = tuple('{0}{1}'.format(g[profile][0], g[profile][1]))
		print self.payoff_matrix
	def find_strongly_dominated(self):
		pass

	def find_weakly_dominant_strategies(self):
		pass

if __name__=="__main__": 
	t=sys.argv[1]
	e = equilibria_finder(sys.argv[1])
	print sys.argv[1]