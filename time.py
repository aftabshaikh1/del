from datetime import date
inf = date.today()
inf = str(inf)
fname = "/home/aftab/PyTelnet/" +inf+".txt"
a = open(fname, "w")
a.write("this is a file")
