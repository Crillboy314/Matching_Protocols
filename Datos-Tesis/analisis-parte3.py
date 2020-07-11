#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 01:38:13 2020

@author: kevinrojas
"""

#Import necesary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pandas as pd
import statsmodels.formula.api as smf

import numpy as np
from scipy import stats

#Define current working directory
os.getcwd()
os.chdir("/Users/kevinrojas/Desktop")

#Define the whole data for both mean and random
datasetMean = pd.read_csv("MeanFinal.csv", header = None)
datasetRandom = pd.read_csv("RandomFinal.csv", header = None)

#Define the transposes for the correct analysis
datasetMeanT = datasetMean.T
datasetRandomT = datasetRandom.T

#Classify data based on characteristics for Mean
MeanDecisions = datasetMean.iloc[0:58]
MeanAleatorio = datasetMean.iloc[58:116].astype(float)
MeanCutoff = datasetMean.iloc[116:174].astype(float)
MeanPago = datasetMean.iloc[174:232].astype(float)

#Classify data based on characteristics for Random
RandomDecisions = datasetRandom.iloc[0:60]
RandomAleatorio = datasetRandom.iloc[60:120].astype(float)
RandomCutoff = datasetRandom.iloc[120:180].astype(float)
RandomPago = datasetRandom.iloc[180:240].astype(float)

#Classify data by session
#Mean Matching
MeanDecisions14p = MeanDecisions.iloc[0:14]
MeanDecisions18p = MeanDecisions.iloc[14:32]
MeanDecisions6p = MeanDecisions.iloc[32:38]
MeanDecisions12p = MeanDecisions.iloc[38:50]
MeanDecisions8p = MeanDecisions.iloc[50:58]

MeanAleatorio14p = MeanAleatorio.iloc[0:14]
MeanAleatorio18p = MeanAleatorio.iloc[14:32]
MeanAleatorio6p = MeanAleatorio.iloc[32:38]
MeanAleatorio12p = MeanAleatorio.iloc[38:50]
MeanAleatorio8p = MeanAleatorio.iloc[50:58]

MeanCutoff14p = MeanCutoff.iloc[0:14]
MeanCutoff18p = MeanCutoff.iloc[14:32]
MeanCutoff6p = MeanCutoff.iloc[32:38]
MeanCutoff12p = MeanCutoff.iloc[38:50]
MeanCutoff8p = MeanCutoff.iloc[50:58]

MeanPago14p = MeanPago.iloc[0:14]
MeanPago18p = MeanPago.iloc[14:32]
MeanPago6p = MeanPago.iloc[32:38]
MeanPago12p = MeanPago.iloc[38:50]
MeanPago8p = MeanPago.iloc[50:58]

#Random Matching
RandomDecisions16p = RandomDecisions.iloc[0:16]
RandomDecisions12p = RandomDecisions.iloc[16:28]
RandomDecisions4p = RandomDecisions.iloc[28:32]
RandomDecisions28p = RandomDecisions.iloc[32:60]


RandomAleatorio16p = RandomAleatorio.iloc[0:16]
RandomAleatorio12p = RandomAleatorio.iloc[16:28]
RandomAleatorio4p = RandomAleatorio.iloc[28:32]
RandomAleatorio28p = RandomAleatorio.iloc[32:60]


RandomCutoff16p = RandomCutoff.iloc[0:16]
RandomCutoff12p = RandomCutoff.iloc[16:28]
RandomCutoff4p = RandomCutoff.iloc[28:32]
RandomCutoff28p = RandomCutoff.iloc[32:60]


RandomPago16p = RandomPago.iloc[0:14]
RandomPago12p = RandomPago.iloc[14:32]
RandomPago4p = RandomPago.iloc[32:38]
RandomPago28p = RandomPago.iloc[38:50]



#Funciones importantes, obtener el promedio de un datafrma especifico

row = RandomPago.mean()

x = pd.Series(np.arange(18))
y = row

plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

plt.show()

# Funcion para calcular interpeceptos en una regresion

def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 

########### AQUI EMPIEZAN LOS ANALISIS POR GRUPOS GRANDES ##############
    
#### ANALISIS DE LAS DIFERENCIAS DE VALORES NUMERICOS  ####

# Calcular primeras diferencias 

MeanCutoff1dNan = MeanCutoff.diff(axis = 1)
MeanAleatorio1dNan = MeanAleatorio.diff(axis = 1)
MeanPago1dNan = MeanPago.diff(axis = 1)

MeanCutoff1d = MeanCutoff1dNan.drop(0, axis= 1)
MeanAleatorio1d = MeanAleatorio1dNan.drop(0, axis= 1)
MeanPago1d = MeanPago1dNan.drop(0, axis= 1)

RandomCutoff1dNan = RandomCutoff.diff(axis = 1)
RandomAleatorio1dNan = RandomAleatorio.diff(axis = 1)
RandomPago1dNan = RandomPago.diff(axis = 1)

RandomCutoff1d = RandomCutoff1dNan.drop(0, axis= 1)
RandomAleatorio1d = RandomAleatorio1dNan.drop(0, axis= 1)
RandomPago1d = RandomPago1dNan.drop(0, axis= 1)

# Calcular segundas diferencias 

MeanCutoff2dNan = MeanCutoff1d.diff(axis = 1)
MeanAleatorio2dNan = MeanAleatorio1d.diff(axis = 1)
MeanPago2dNan = MeanPago1d.diff(axis = 1)

MeanCutoff2d = MeanCutoff2dNan.drop(1, axis= 1)
MeanAleatorio2d = MeanAleatorio2dNan.drop(1, axis= 1)
MeanPago2d = MeanPago2dNan.drop(1, axis= 1)

RandomCutoff2dNan = RandomCutoff1d.diff(axis = 1)
RandomAleatorio2dNan = RandomAleatorio1d.diff(axis = 1)
RandomPago2dNan = RandomPago1d.diff(axis = 1)

RandomCutoff2d = RandomCutoff2dNan.drop(1, axis= 1)
RandomAleatorio2d = RandomAleatorio2dNan.drop(1, axis= 1)
RandomPago2d = RandomPago2dNan.drop(1, axis= 1)

rectaMean = range(0,58)
rectaRandom = range(0,60)
rectaRounds = np.array(range(0,18))
rectaRounds1d = range(0,17)
rectaRounds2d = range(0,16)


############## Vamos a ver los graficos promedio de cada variables...


fig1 = plt.figure(figsize=(10,10))
ax1 = fig1.add_subplot(111)
ax1.plot(rectaRounds, RandomPago.mean(),"b-", label = "Random Matching Protocol (Average)")
ax1.plot(rectaRounds, MeanPago.mean(),"b-", color ="red", label = "Mean Matching Protocol (Average)")
ax1.axis(ymin=40,ymax= 80)
ax1.set_xlabel('Rounds')
ax1.set_ylabel("Average Payment Received")
ax1.set_title("Evolution of the average payment in each round")
ax1.legend()
plt.show()

fig1.savefig("Average-Payment-All")  

fig1 = plt.figure(figsize=(10,10))
ax1 = fig1.add_subplot(111)
ax1.plot(rectaRounds, RandomCutoff.mean(),"b-", label = "Random Matching Protocol (Average)")
ax1.plot(rectaRounds, MeanCutoff.mean(),"b-", color ="red", label = "Mean Matching Protocol (Average)")
ax1.axis(ymin=40,ymax= 70)
ax1.set_xlabel('Rounds')
ax1.set_ylabel("Average Cutoff number")
ax1.set_title("Evolution of the average cutoffnumber in each round")
ax1.legend()
plt.show()

fig1.savefig("Average-Cutoff-All")  

fig1 = plt.figure(figsize=(10,10))
ax1 = fig1.add_subplot(111)
ax1.plot(rectaRounds, RandomAleatorio.mean(),"b-", label = "Random Matching Protocol (Average)")
ax1.plot(rectaRounds, MeanAleatorio.mean(),"b-", color ="red", label = "Mean Matching Protocol (Average)")
ax1.axis(ymin=40,ymax= 60)
ax1.set_xlabel('Rounds')
ax1.set_ylabel("Average Random Received")
ax1.set_title("Evolution of the average random in each round")
ax1.legend()
plt.show()

fig1.savefig("Average-Random-All")  


########### Algunas pruebas con rectas de sesiones especificas

######## ALGUNOS ANALISIS ADICIONALES TOMANDO EN CUENTA DATOS PARA LAS DECISIONES

MeanDecisionsBinary = MeanDecisions.replace("A",1)
MeanDecisionsBinary = MeanDecisionsBinary.replace("B", 0)
RandomDecisionsBinary = RandomDecisions.replace("A",1)
RandomDecisionsBinary = RandomDecisionsBinary.replace("B",0)

MeanDecisionsBinary12p = MeanDecisions12p.replace("A",1)
MeanDecisionsBinary12p = MeanDecisionsBinary12p.replace("B", 0)

MeanDecisionsBinary14p = MeanDecisions14p.replace("A",1)
MeanDecisionsBinary14p = MeanDecisionsBinary14p.replace("B", 0)

MeanDecisionsBinary18p = MeanDecisions18p.replace("A",1)
MeanDecisionsBinary18p = MeanDecisionsBinary18p.replace("B", 0)

MeanDecisionsBinary6p = MeanDecisions6p.replace("A",1)
MeanDecisionsBinary6p = MeanDecisionsBinary6p.replace("B", 0)

MeanDecisionsBinary8p = MeanDecisions8p.replace("A",1)
MeanDecisionsBinary8p = MeanDecisionsBinary8p.replace("B", 0)



RandomDecisionsBinary12p = RandomDecisions12p.replace("A",1)
RandomDecisionsBinary12p = RandomDecisionsBinary12p.replace("B",0)

RandomDecisionsBinary16p = RandomDecisions16p.replace("A",1)
RandomDecisionsBinary16p = RandomDecisionsBinary16p.replace("B",0)

RandomDecisionsBinary4p = RandomDecisions4p.replace("A",1)
RandomDecisionsBinary4p = RandomDecisionsBinary4p.replace("B",0)

RandomDecisionsBinary28p = RandomDecisions28p.replace("A",1)
RandomDecisionsBinary28p = RandomDecisionsBinary28p.replace("B",0)



################ Aqui los graficos para las regresiones promedio

MeanPago = MeanPago.mean()
MeanCutoff = MeanCutoff.mean()
MeanDecisions = MeanDecisionsBinary.mean()
MeanAleatorio = MeanAleatorio.mean()
d = { "MeanPago": pd.Series(MeanPago), "MeanCutoff": pd.Series(MeanCutoff), 
     "MeanDecisions": pd.Series(MeanDecisions), "MeanAleatorio": pd.Series(MeanAleatorio)}
df = pd.DataFrame(d)
mod = smf.ols('MeanPago ~ MeanCutoff + MeanDecisions + MeanAleatorio', data=df)
res = mod.fit()
print(res.summary())

beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\end{document}"

f = open('Mean.tex', 'w')
f.write(beginningtex)
f.write(res.summary().as_latex())
f.write(endtex)
f.close()


RandomPago = RandomPago.mean()
RandomCutoff = RandomCutoff.mean()
RandomDecisions = RandomDecisionsBinary.mean()
RandomAleatorio = RandomAleatorio.mean()
d = { "RandomPago": pd.Series(RandomPago), "RandomCutoff": pd.Series(RandomCutoff), 
     "RandomDecisions": pd.Series(RandomDecisions), "RandomAleatorio": pd.Series(RandomAleatorio)}
df = pd.DataFrame(d)
mod = smf.ols('RandomPago ~ RandomCutoff + RandomDecisions + RandomAleatorio', data=df)
res = mod.fit()
print(res.summary())

beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\end{document}"

f = open('Random.tex', 'w')
f.write(beginningtex)
f.write(res.summary().as_latex())
f.write(endtex)
f.close()

################ ACA EMPIEZAN LASVARIACIONES PARA LA TABLA DE RESULTADOS

MeanPago = MeanPago18p.mean()
MeanCutoff = MeanCutoff18p.mean()
MeanDecisions = MeanDecisionsBinary18p.mean()
MeanAleatorio = MeanAleatorio18p.mean()
d = { "MeanPago": pd.Series(MeanPago), "MeanCutoff": pd.Series(MeanCutoff), 
     "MeanDecisions": pd.Series(MeanDecisions), "MeanAleatorio": pd.Series(MeanAleatorio)}
df = pd.DataFrame(d)
mod = smf.ols('MeanPago ~ MeanCutoff + MeanDecisions + MeanAleatorio', data=df)
res = mod.fit()
print(res.summary())

beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\end{document}"

f = open('Mean.tex', 'w')
f.write(beginningtex)
f.write(res.summary().as_latex())
f.write(endtex)
f.close()


RandomPago = RandomPago4p.mean()
RandomCutoff = RandomCutoff4p.mean()
RandomDecisions = RandomDecisionsBinary4p.mean()
RandomAleatorio = RandomAleatorio4p.mean()
d = { "RandomPago": pd.Series(RandomPago), "RandomCutoff": pd.Series(RandomCutoff), 
     "RandomDecisions": pd.Series(RandomDecisions), "RandomAleatorio": pd.Series(RandomAleatorio)}
df = pd.DataFrame(d)
mod = smf.ols('RandomPago ~ RandomCutoff + RandomDecisions + RandomAleatorio', data=df)
res = mod.fit()
print(res.summary())

beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\end{document}"

f = open('Random.tex', 'w')
f.write(beginningtex)
f.write(res.summary().as_latex())
f.write(endtex)
f.close()

############## Ahora hacemos el analisis socio-demogra



datasetSocDem = pd.read_csv("SocioDem.csv")
datasetSocDem['Sex'] = pd.Categorical(datasetSocDem.Sex)
datasetSocDem['Age'] = datasetSocDem.Age.astype(str).str[:2].astype(int)
datasetSocDem['Age'] = pd.Float64Index(datasetSocDem.Age)
datasetSocDem['Race'] = pd.Categorical(datasetSocDem.Race)
datasetSocDem['Student'] = pd.Categorical(datasetSocDem.Student)
datasetSocDem['Income'] = pd.Categorical(datasetSocDem.Income)
datasetSocDem['Intention'] = pd.Categorical(datasetSocDem.Intention)
datasetSocDem['Treatment'] = pd.Categorical(datasetSocDem.Treatment)
mod = smf.ols('Payment ~ Risk + Sex + Age + Race + Student + Income + Intention + Treatment', data=datasetSocDem)
res = mod.fit()
print(res.summary())

beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\end{document}"

f = open('SocDemTret.tex', 'w')
f.write(beginningtex)
f.write(res.summary().as_latex())
f.write(endtex)
f.close()


datasetSocDem = pd.read_csv("SocioDem.csv")
datasetSocDem['Sex'] = pd.Categorical(datasetSocDem.Sex)
datasetSocDem['Age'] = datasetSocDem.Age.astype(str).str[:2].astype(int)
datasetSocDem['Age'] = pd.Float64Index(datasetSocDem.Age)
datasetSocDem['Race'] = pd.Categorical(datasetSocDem.Race)
datasetSocDem['Student'] = pd.Categorical(datasetSocDem.Student)
datasetSocDem['Income'] = pd.Categorical(datasetSocDem.Income)
datasetSocDem['Intention'] = pd.Categorical(datasetSocDem.Intention)
datasetSocDem['Treatment'] = pd.Categorical(datasetSocDem.Treatment)
mod = smf.ols('Payment ~ Risk + Sex + Age + Race + Student + Income + Intention', data=datasetSocDem)
res = mod.fit()
print(res.summary())

beginningtex = """\\documentclass{report}
\\usepackage{booktabs}
\\begin{document}"""
endtex = "\end{document}"

f = open('SocDemNoTr.tex', 'w')
f.write(beginningtex)
f.write(res.summary().as_latex())
f.write(endtex)
f.close()


##################

dataTypeSeries = datasetSocDem.dtypes()
print('Data type of each column of Dataframe :')
print(dataTypeSeries)

datasetSocDem.groupby("Treatment").mean()

datasetSocDem["Age"]




