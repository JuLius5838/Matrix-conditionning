import numpy as np
import matplotlib.pyplot as plt 
import math

def Hilbert_Matrix (n):
	H = np.zeros((n,n))
	for i in range (n):
		for j in range (n):
			h = 1/(i+j+1)
			H[i,j] = h

	return(H)

def Cond_hilbert():
	COND = list()
	N = list()
	for n in range (2,21):
		H = Hilbert_Matrix(n)
		cond = np.linalg.cond(H)
		COND.append(cond)
		N.append(n)

	plt.semilogy(N,COND)
	plt.show()

def quotient ():
	n = 10
	H = Hilbert_Matrix(n)
	v = np.random.rand(n)
	b = v / np.linalg.norm(v)
	normb = np.linalg.norm(b)
	v = np.random.rand(n)
	db = (1e-2*v )/ np.linalg.norm(v)
	normdb = (np.linalg.norm(db))
	bprim = db + b
	x = np.linalg.solve(H,b)
	xprim = np.linalg.solve(H,bprim)
	normx = np.linalg.norm(x)
	normxprim = np.linalg.norm(xprim)
	dx = xprim - x
	normdx = np.linalg.norm(dx)

	erx = (normdx/normx)
	erb = (normdb/normb)

	q = erx/erb

	return (q)

def quotien_10_4 ():
	Nexp = 1000

	listeq = np.zeros(Nexp)
	for m in range(Nexp):
		listeq[m] = quotient()

	mini = min(listeq)
	maxi = max(listeq)

	print(mini)
	print(maxi)

#def quotientA  ():

	n = 10
	H = Hilbert_Matrix(n)
	v = np.random.rand(n)
	b = v / np.linalg.norm(v)

	az = np.random.rand(n,n)
	A = az / np.linalg.norm(az)

	az = np.random.rand(n,n)
	dA = (1e-2)*az/np.linalg.norm(az)

	Aprim = dA + A

	x = np.linalg.solve(H,)
	xprim = np.linalg.solve(H,bprim)
	normx = np.linalg.norm(x)
	normdx = np.linalg.norm(dx)
	normdA = np.linalg.norm(dA)
	normA = np.linalg.norm(A)

	erx = normdx / normx
	era = normdA / normA

	q = erx/era

	return(q)#marche pas flemme de continuer

