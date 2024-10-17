import matplotlib.pyplot as pl
a=[140,160,140,180,110]
b=["North","South","East","West","Central"]
pl.plot(b,a,marker='+',markeredgecolor='b',markersize=10,linewidth=3,linestyle='solid')
pl.savefig("C:\Users\Sweet home\Downloads\line chart.png")