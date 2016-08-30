

from __future__ import print_function
import collections
import time
import pdb
import re
import shlex
import numpy as np
import itertools

class find_equilibrium(object):
    """
    Class to find dominant (strong or weak) stratergy equilibrium in a game
    """
    def __init__(self):
        pass

    def find_max(self, vec):
        """
        Returns the maximum in the vector (returns multiple max if occurred
        """
        return np.argwhere(vec == np.amax(vec)).flatten().tolist()

    def chunk(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:(i+n)]

    def gen_indices(self, ar):
        ind = []
        for i in ar:
            ind.append(range(i))
        indices = [i for i in itertools.product(*ind)]
        return np.asarray(indices)

    def parser(self, inp_path):
        # Parse .nfg input file
        f = open(inp_path, 'r')
        # First line contains info. about game
        metadata = f.readline().rstrip()
        self.game_type, self.version, self.data_type, self.game_name = shlex.split(metadata)
        print("Some information about the game is : \n")
        print("     1. Type of game is : %s"%self.game_type)
        print("     2. Version of game is : %s"%self.version)
        print("     3. Data type used in game (rational or integer) : %s"%self.data_type)
        print("     4. Name of the game is : %s"%(self.game_name))
        # Parsing player's information
        self.player_info = f.readline().rstrip()
        # seperate player info from the string
        ind  = self.player_info.find('}')
        self.players = shlex.split(self.player_info[2:ind-1])
        self.n_stratergies = map(lambda x:int(x), self.player_info[ind+4:-2].split())
        # Parse utility function
        f.readline()
        self.utilities = map(lambda x:int(x), f.readline().split())
        self.utils = list(self.chunk(self.utilities, len(self.players)))
        #pdb.set_trace()
        self.utils = map(lambda x:x[::-1], self.utils)
        self.utils = np.asarray(self.utils, dtype=np.int32)
        self.ds = []
        #self.utility_matrix = np.zeros(self.n_stratergies)

    def find_equilibrium(self):
        """ Find the dominant stratergy equilibrium
            Input:
                stratergy_vec: stratergy vector
                utility: utility matrix

            Ouput:
                Dominant stratergy equilibrium
        """
        # Number of players
        M = len(self.n_stratergies)
        # No of rows in stratergy matrix( NOT REQ., CHECK)
        N = self.utils.shape[0]
        jf = 1
        # Find stratergies
        for i in xrange(1, M+1):
            util = self.utils[:, -i]
            nsteps = np.prod(np.delete(self.n_stratergies, i-1))
            ind = 0
            arg_vec = []
            for j in xrange(nsteps):
                ind_vec = []
                for k in xrange(self.n_stratergies[i-1]):
                    ind_vec.append(ind)
                    ind+= jf
                pdb.set_trace()
                utilities = util[ind_vec]
                arg_vec.append(self.find_max(utilities))
            #pdb.set_trace()
            DS = set.intersection(*map(set, arg_vec))
            if len(DS) >= 1:
                DS = list(DS)[0]
                self.ds.append(DS)
            else:
                print("No dominant stratergy, exit")
                return

            jf *= self.n_stratergies[i-1]
            #pdb.set_trace()

if __name__ == "__main__":
    game = find_equilibrium()
    game.parser('./prisoner_dimemma.nfg')
    game.find_equilibrium()
    print(game.ds)
