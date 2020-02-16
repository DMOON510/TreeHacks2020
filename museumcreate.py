
from museum import *
import pandas as pd


gallery1= gallery(0,100)
gallery2 = gallery(1,50)
gallery3 = gallery(2, 25)
gallery4 = gallery(3, 80)
gallery5 = gallery(4, 50)
galleries = [gallery1, gallery2, gallery3, gallery4, gallery5]

cols = ['preference','score','recommendation']
lst = []

visitors = {}
for i in range(100):
	visitors[i] = visitor()
	like(visitors[i])
	recommend(galleries, visitors[i])
	pref = ",".join(visitors[i].preference)
	score = ",".join(visitors[i].score)
	rec = visitors[i].recommendation
	lst.append([pref,score,rec])

df = pd.DataFrame(lst, columns=cols)






