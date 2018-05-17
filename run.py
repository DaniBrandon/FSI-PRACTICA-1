# Search methods
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import search
import matplotlib.pyplot as plt
import numpy as np


ab = search.GPSProblem('A', 'B', search.romania)
oe = search.GPSProblem('O', 'E', search.romania)
zb = search.GPSProblem('Z', 'B', search.romania)
ag = search.GPSProblem('A', 'G', search.romania)
ou = search.GPSProblem('O', 'U', search.romania)
an = search.GPSProblem('A', 'N', search.romania)
zv = search.GPSProblem('Z', 'V', search.romania)
mi = search.GPSProblem('M', 'I', search.romania)
mat = np.empty((4,2,))
def fun(f,s):
     print s
     (search.breadth_first_graph_search(f, mat, 0).path())
     (search.depth_first_graph_search(f, mat, 1).path())
     (search.branch_bound_graph_search(f, mat, 2))
     (search.branch_bound_subestimate_graph_search(f, mat, 3))

fun(ab,'ab')
fun(oe,'oe')
fun(zb,'zb')
fun(ag,'ag')
fun(ou,'ou')
fun(an,'an')
fun(zv,'zv')
fun(mi,'mi')




fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Table from Ed Smith answer
collabel=("Nodos visitados", "Nodos expandidos")
rowlabel=("Búsqueda en Anchura", "Búsqueda en Profundidad", "Ramificación y acotación", "Ramificación y acotación con subestimación")
ax.table(cellText=mat,rowLabels=rowlabel,colLabels=collabel,loc='center')

#axs[1].plot(clust_data[:,0],clust_data[:,1])
#plt.show()

#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
