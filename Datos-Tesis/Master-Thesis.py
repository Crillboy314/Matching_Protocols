#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:59:05 2020

@author: kevinrojas
"""
#Import necesary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import statsmodels.formula.api as smf


from scipy import stats

#Define current working directory
os.getcwd()
os.chdir("/Users/kevinrojas/Desktop/Datos-Tesis")

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
RandomDecisions14p = RandomDecisions.iloc[0:16]
RandomDecisions18p = RandomDecisions.iloc[16:28]
RandomDecisions6p = RandomDecisions.iloc[28:32]
RandomDecisions12p = RandomDecisions.iloc[32:60]


RandomAleatorio14p = RandomAleatorio.iloc[0:16]
RandomAleatorio18p = RandomAleatorio.iloc[16:28]
RandomAleatorio6p = RandomAleatorio.iloc[28:32]
RandomAleatorio12p = RandomAleatorio.iloc[32:60]


RandomCutoff14p = RandomCutoff.iloc[0:16]
RandomCutoff18p = RandomCutoff.iloc[16:28]
RandomCutoff6p = RandomCutoff.iloc[28:32]
RandomCutoff12p = RandomCutoff.iloc[32:60]


RandomPago14p = RandomPago.iloc[0:14]
RandomPago18p = RandomPago.iloc[14:32]
RandomPago6p = RandomPago.iloc[32:38]
RandomPago12p = RandomPago.iloc[38:50]



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

#### Aqui empieza comparacion con primeras diferencias

# Intento comparando cutoff con aleatorio

Slopes = []

for i in range(1,58):
    slope = estimate_coef(MeanCutoff1d.iloc[i], MeanAleatorio1d.iloc[i])
    Slopes.append(slope[0])
    
Slopes2 = []

for i in range(1,60):
    slope = estimate_coef(RandomCutoff1d.iloc[i], RandomAleatorio1d.iloc[i])
    Slopes2.append(slope[0])


t2, p2 = stats.ttest_ind(np.array(Slopes),np.array(Slopes2), nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))



### El resultado es que no hay diferencia entre los dos grupos de coeficientes
### cuando se comparan grupos random y mean


# Intento comparando cutoff con PAGO

Slopes = []

for i in range(1,58):
    slope = estimate_coef(MeanCutoff1d.iloc[i], MeanPago1d.iloc[i])
    Slopes.append(slope[0])
    
Slopes2 = []

for i in range(1,60):
    slope = estimate_coef(RandomCutoff1d.iloc[i], RandomPago1d.iloc[i])
    Slopes2.append(slope[0])


t2, p2 = stats.ttest_ind(np.array(Slopes),np.array(Slopes2), nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))



### El resultado es que no hay diferencia entre los dos grupos de coeficientes
### cuando se comparan grupos random y mean



# Intento comparando aleatorio con pagos

Slopes = []

for i in range(1,58):
    slope = estimate_coef(MeanAleatorio1d.iloc[i], MeanPago1d.iloc[i])
    Slopes.append(slope[0])
    
Slopes2 = []

for i in range(1,60):
    slope = estimate_coef(RandomAleatorio1d.iloc[i], RandomPago1d.iloc[i])
    Slopes2.append(slope[0])


t2, p2 = stats.ttest_ind(np.array(Slopes),np.array(Slopes2), nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))

##### ESTE ES EL RESULTADO MAS ALENTADOR


### El resultado es que no hay diferencia entre los dos grupos de coeficientes
### cuando se comparan grupos random y mean


#### Aqui empieza comparacion con segundas diferencias


# Intento comparando cutoff con aleatorio

Slopes = []

for i in range(1,58):
    slope = estimate_coef(MeanCutoff2d.iloc[i], MeanAleatorio2d.iloc[i])
    Slopes.append(slope[0])
    
Slopes2 = []

for i in range(1,60):
    slope = estimate_coef(RandomCutoff2d.iloc[i], RandomAleatorio2d.iloc[i])
    Slopes2.append(slope[0])


t2, p2 = stats.ttest_ind(np.array(Slopes),np.array(Slopes2), nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))



### El resultado es que no hay diferencia entre los dos grupos de coeficientes
### cuando se comparan grupos random y mean


# Intento comparando cutoff con PAGO

Slopes = []

for i in range(1,58):
    slope = estimate_coef(MeanCutoff2d.iloc[i], MeanPago2d.iloc[i])
    Slopes.append(slope[0])
    
Slopes2 = []

for i in range(1,60):
    slope = estimate_coef(RandomCutoff2d.iloc[i], RandomPago2d.iloc[i])
    Slopes2.append(slope[0])


t2, p2 = stats.ttest_ind(np.array(Slopes),np.array(Slopes2), nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))



### El resultado es que no hay diferencia entre los dos grupos de coeficientes
### cuando se comparan grupos random y mean



# Intento comparando aleatorio con pagos

Slopes = []

for i in range(1,57):
    slope = estimate_coef(MeanAleatorio2d.iloc[i], MeanPago2d.iloc[i])
    Slopes.append(slope[0])
    
Slopes2 = []

for i in range(1,59):
    slope = estimate_coef(RandomAleatorio2d.iloc[i], RandomPago2d.iloc[i])
    Slopes2.append(slope[0])


t2, p2 = stats.ttest_ind(np.array(Slopes),np.array(Slopes2), nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))

####### TRATAMOS DE IDENTIFICAR AHORA DIFERENCIAS EN LA CANTIDAD DE CAMBIO SOBRE 


MeanCutoffAllValues1d = np.array(MeanCutoff1d).flatten()
RandomCutoffAllValues1d = np.array(RandomCutoff1d).flatten()

t2, p2 = stats.ttest_ind(MeanCutoffAllValues1d,RandomCutoffAllValues1d, nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))

MeanCutoffAllValues = np.array(MeanCutoff).flatten()
RandomCutoffAllValues = np.array(RandomCutoff).flatten()

t2, p2 = stats.ttest_ind(MeanCutoffAllValues,RandomCutoffAllValues, nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))



#### Esta diferencia si se nota a lo bestia :)

print(MeanCutoffAllValues.mean())
print(RandomCutoffAllValues.mean())

MeanAleatorioAllValues = np.array(MeanAleatorio).flatten()
RandomAleatorioAllValues = np.array(RandomAleatorio).flatten()

t2, p2 = stats.ttest_ind(MeanAleatorioAllValues,RandomAleatorioAllValues, nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))

#### Los aleatorios no son iguales :)

MeanPagoAllValues = np.array(MeanPago).flatten()
RandomPagoAllValues = np.array(RandomPago).flatten()

t2, p2 = stats.ttest_ind(MeanPagoAllValues,RandomPagoAllValues, nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))

print(MeanPagoAllValues.mean())
print(RandomPagoAllValues.mean())


twosample_results = stats.ttest_ind(MeanPagoAllValues,RandomPagoAllValues, nan_policy = "omit")


#### La diferencia entre los pagos es impresionantemente grande...


######### Comparemos como se comportan los valores solos (contra 1,2,3,4,...)

rectaMean = range(0,58)
rectaRandom = range(0,60)
rectaRounds = range(0,18)
rectaRounds1d = range(0,17)
rectaRounds2d = range(0,16)

###### Primero lo hacemos con differencias del cutoff

Slopes = []

for i in range(0,58):
    slope = estimate_coef(MeanCutoff2d.iloc[i], rectaRounds2d)
    Slopes.append(slope[0])
    
Slopes2 = []

for i in range(0,60):
    slope = estimate_coef(RandomCutoff2d.iloc[i], rectaRounds2d)
    Slopes2.append(slope[0])


t2, p2 = stats.ttest_ind(np.array(Slopes),np.array(Slopes2), nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))

## No se encuentra significancia en ninguna de las 2

###### Ahora sin diferencias

Slopes = []

for i in range(0,58):
    slope = estimate_coef(MeanCutoff.iloc[i], rectaRounds)
    Slopes.append(slope[0])
    
Slopes2 = []

for i in range(0,60):
    slope = estimate_coef(RandomCutoff.iloc[i], rectaRounds)
    Slopes2.append(slope[0])


t2, p2 = stats.ttest_ind(np.array(Slopes),np.array(Slopes2), nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))


######## ALGUNOS ANALISIS ADICIONALES TOMANDO EN CUENTA DATOS PARA LAS DECISIONES

MeanDecisionsBinary = MeanDecisions.replace("A",1)
MeanDecisionsBinary = MeanDecisionsBinary.replace("B", 0)
RandomDecisionsBinary = RandomDecisions.replace("A",1)
RandomDecisionsBinary = RandomDecisionsBinary.replace("B",0)

# Primero vemos que en general...

MeanDecisionsAllValues = np.array(MeanDecisionsBinary).flatten()
RandomDecisionsAllValues = np.array(RandomDecisionsBinary).flatten()

t2, p2 = stats.ttest_ind(MeanDecisionsAllValues,RandomDecisionsAllValues, nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))

print(MeanDecisionsAllValues.mean())
print(RandomDecisionsAllValues.mean())

# Se encuentra diferencia a nivel general respecto de la cantidad de decisiones tomadas

#Ahora vemos con las pendientes de los valores para cada participantes

Slopes = []

for i in range(0,58):
    slope = estimate_coef(MeanDecisionsBinary.iloc[i], rectaRounds)
    Slopes.append(slope[0])
    
Slopes2 = []

for i in range(0,60):
    slope = estimate_coef(RandomDecisionsBinary.iloc[i], rectaRounds)
    Slopes2.append(slope[0])


t2, p2 = stats.ttest_ind(np.array(Slopes),np.array(Slopes2), nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))

# Calcular primeras diferencias para decisiones


MeanDecisiones1dNan = MeanDecisionsBinary.diff(axis = 1)

MeanDecisions1d = MeanDecisiones1dNan.drop(0, axis= 1)

RandomDecisiones1dNan = RandomDecisionsBinary.diff(axis = 1)

RandomDecisions1d = RandomDecisiones1dNan.drop(0, axis= 1)

# Calcular segundas diferencias para decisiones

MeanDecisiones2dNan = MeanDecisions1d.diff(axis = 1)

MeanDecisions2d = MeanDecisiones2dNan.drop(1, axis= 1)

RandomDecisiones2dNan = RandomDecisions1d.diff(axis = 1)

RandomDecisions2d = RandomDecisiones2dNan.drop(1, axis= 1)

#Ahora vemos con las pendientes de los valores para cada participantes y
# las primeras diferencias de cada uno

Slopes = []

for i in range(0,58):
    slope = estimate_coef(MeanDecisions2d.iloc[i], rectaRounds2d)
    Slopes.append(slope[0])
    
Slopes2 = []

for i in range(0,60):
    slope = estimate_coef(RandomDecisions2d.iloc[i], rectaRounds2d)
    Slopes2.append(slope[0])


t2, p2 = stats.ttest_ind(np.array(Slopes),np.array(Slopes2), nan_policy = "omit")
print("t = " + str(t2))
print("p = " + str(p2))

# No hay diferencias entre la forma en la que cambian las decisiones


############### AQUI EMPIEZA LA PARTE DE GRAFICOS #######################


MeanPagoAllValuesSorted = MeanPagoAllValues.copy()
MeanPagoAllValuesSorted.sort()

RandomPagoAllValuesSorted = RandomPagoAllValues.copy()
RandomPagoAllValuesSorted.sort()

MeanCutoffAllValuesSorted = MeanCutoffAllValues.copy()
MeanCutoffAllValuesSorted.sort()

RandomCutoffAllValuesSorted = RandomCutoffAllValues.copy()
RandomCutoffAllValuesSorted.sort()

MeanAleatorioAllValuesSorted = MeanAleatorioAllValues.copy()
MeanAleatorioAllValuesSorted.sort()

RandomAleatorioAllValuesSorted = RandomAleatorioAllValues.copy()
RandomAleatorioAllValuesSorted.sort()



def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y, c = ["red"])
    ax.plot(range(100), range(100))

    # now determine nice limits by hand:
    binwidth = 1
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(0, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005


rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom + height + spacing, width, 0.2]
rect_histy = [left + width + spacing, bottom, 0.2, height]

# start with a square Figure
fig = plt.figure(figsize=(8, 8))

ax = fig.add_axes(rect_scatter, title = "Pagos")
ax_histx = fig.add_axes(rect_histx, sharex=ax, title = "RP Cutoff")
ax_histy = fig.add_axes(rect_histy, sharey=ax, title = "MM Cutoffs")

# use the previously defined function

scatter_hist(RandomCutoffAllValuesSorted[:1044], MeanCutoffAllValuesSorted[:1044], ax, ax_histx, ax_histy)

plt.show()

fig.savefig("Scatter-Cutoff")   

plt.close(fig)

# start with a square Figure
fig2 = plt.figure(figsize=(8, 8))

ax = fig2.add_axes(rect_scatter, title = "Pagos")
ax_histx = fig2.add_axes(rect_histx, sharex=ax, title = "RP Payments")
ax_histy = fig2.add_axes(rect_histy, sharey=ax, title = "MM Payments")

# use the previously defined function

scatter_hist(RandomPagoAllValuesSorted[:1044], MeanPagoAllValuesSorted[:1044], ax, ax_histx, ax_histy)

plt.show()

fig2.savefig("Scatter-Payments")   

plt.close(fig2)

# start with a square Figure
fig3 = plt.figure(figsize=(8, 8))

ax = fig3.add_axes(rect_scatter, title = "Pagos")
ax_histx = fig3.add_axes(rect_histx, sharex=ax, title = "RP Randoms")
ax_histy = fig3.add_axes(rect_histy, sharey=ax, title = "MM Randoms")

# use the previously defined function

scatter_hist(RandomAleatorioAllValuesSorted[:1044], MeanAleatorioAllValuesSorted[:1044], ax, ax_histx, ax_histy)

plt.show()

fig3.savefig("Scatter-Randoms")   

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















