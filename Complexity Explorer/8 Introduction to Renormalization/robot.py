# joint machines for Rock Paper Scissors
# a worked example for the SFI Renormalization MOOC
# http://renorm.complexityexplorer.org
# Simon DeDeo / simon@santafe.edu / http://santafe.edu/~simon
## let's try two robots -- one plays best-response, a deterministic strategy where it plays what would have beaten the opponent the previous round
## the other plays "noisy best response" -- do the same, but sometimes "mix it up" 

## instead of doing a matrix first, let's write it as a dictionary in python:
best_response={"RR": [0,1,0], "RP": [0,0,1], "RS": [1,0,0], "PR": [0,1,0], "PP": [0,0,1], "PS": [1,0,0], "SR": [0,1,0], "SP": [0,0,1], "SS": [1,0,0]}
epsilon=0.1
noisy_best_response={}
for i in best_response.keys():
	ans=[j+epsilon for j in best_response[i]]
	noisy_best_response[i]=[j/sum(ans) for j in ans]

## now let's write down the Markov Chain; again, for simplicity, we'll use the dictionary form so we can remember the moves...
matrix={}
moves=["R", "P", "S"]
for i in moves:
	for j in moves: 
		## when the previous moves was (i+j), what is the probability that (robot 1 emits k) and (robot 2 emits l)? 
		matrix[i+j]={}
		for k in range(3):
			for l in range(3):
				kname=moves[k]
				lname=moves[l]
				matrix[i+j][kname+lname]=best_response[i+j][k]*noisy_best_response[j+i][l]
## matrix["RS"]["RP"] prob that R1 plays R and R2 plays P in response to RS

## let's use the largest eigenvector to find the correct limiting matrix form
import numpy
## now we have the 9x9 transition matrix (as a dictionary); let's write this in matrix form
ans=[]
movepair=[moves[i]+moves[j] for i in range(3) for j in range(3)]
for i in movepair:
	ans += [[matrix[i][j] for j in movepair]]

a = numpy.matrix(ans)
eigenvalues, eigenvectors = numpy.linalg.eig(a)

eigenvalues[0] ## this is the first eigenvalue (equal to unity)
eigenvectors[0:8,0] ## and this is the first eigenvector -- as you can see, it's uniform; another way to say it is that the robots approximate the Nash equilibrium
## the corresponding transition matrix is just a matrix with 1/9 in every entry.
