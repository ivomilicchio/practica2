evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""
titulo= evaluar.split("resumen: ")[0].split()
titulo.pop(0)
condicion= { "Fácil de leer" : 0 , "Aceptable para leer" : 0 , "Difícil de leer" : 0 , "Muy difícil" : 0 }
resumen= evaluar.split("resumen: ")[1].split(".")
for actual in resumen:
		if (len(actual.split())) <= 12:
				condicion["Fácil de leer"]= condicion["Fácil de leer"] + 1
		elif (len(actual.split())) > 12 and (len(actual.split())) <= 17:
				condicion["Aceptable para leer"]= condicion["Aceptable para leer"] + 1
		elif (len(actual.split())) > 17 and (len(actual.split())) <= 25:
				condicion["Difícil de leer"]= condicion["Difícil de leer"] + 1
		else:
			condicion["Muy difícil"]= condicion["Muy difícil"] + 1
if len(titulo) < 11:
		print ("Título está ok")
else:
		print ("Título está mal")
print (condicion.items())	
				
				
