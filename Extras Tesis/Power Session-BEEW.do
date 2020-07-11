*********************************************************
* BOGOTA EXPERIMENTAL ECONOMICS WORKSHOP				*
* POWER ANALYSIS FOR (MOSTLY FIELD) EXPERIMENTS			*
*														*
* Stanislao Maldonado									*
* www.stanislaomaldonado.org							*
* E-mail: stanislao@stanislaomaldonado.org				*
* Last change: 01/06/20									*
*********************************************************


set more off

* Change directory

cd "C:\Users\Stanislao\Dropbox\Teaching\1. Current\Econometrics\3. Lecture Notes\1. Lectures\2. Graduate Applied\13. Lecture XIII-Power\BEEW Code"

*---------*
* 1. DATA *
*---------*

use "DataFinal_power.dta", clear 

describe

sum

*----------------------------------------------------------------*
* 2. MINIMUN DETECTABLE EFFECT FOR INDIVIDUAL RANDOMIZED DESIGNS *
*----------------------------------------------------------------*

*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/
* 2.1. MEANS AND VARIANCE OF IMPACT INDICATOR
*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/

* Variance and standard deviation

sum IncomeLabHH1, detail

scalar mean_income = r(mean)			/*Mean*/
display mean_income

scalar var_income = r(Var)				/*Variance*/
display var_income

scalar stddev_income = r(sd)			/*Standard deviation*/
display stddev_income

* Saving info about parameters in locals

local control_m = mean_income
local sigma_m = stddev_income


*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/
* 2.2. COMPUTING THE MINIMUM DETECTABLE EFFECT (USING POWER COMMAND)
*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/

power twomeans `control_m', sd(`sigma_m') alpha(0.05) power (0.9) n(1000)


*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/
* 2.3. COMPUTING THE MINIMUM DETECTABLE EFFECT (USING MANUAL APPROACH)
*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/

* Clearing scalars

scalar drop _all

* A. MEANS AND VARIANCE OF IMPACT INDICATOR

sum IncomeLabHH1, detail

scalar mean_income = r(mean)			/*Mean*/

scalar var_income = r(Var)				/*Variance*/

scalar stddev_income = r(sd)			/*Standard deviation*/


* B. COMPUTING STANDARD ERRORS: (sigma^2/N)^(1/2)

scalar n_sample = 1000 				/*Asumming known sample size and we need to compute MDE*/

scalar st_error = (var_income/n_sample)^(1/2)


* C. PROPORTION OF TREATMENT AND CONTROL UNITS: (1/(P(1-P)))^(1/2) 

local p=0.5								 /*P: proportion of treatment units*/

scalar p_exp=(1/(`p'*(1-`p')))^(1/2)


* D. T-VALUES FOR ALPHA (SIGNIFICANCE LEVEL) AND 1-K (POWER) *

scalar t_alpha=invnormal(0.975)			/*Note: 0.95 if one-sided test*/

scalar t_beta=invnormal(0.90)

scalar t_alphaplusbeta=t_alpha+t_beta

* Parameters

display p_exp

display t_alpha
display t_beta


* E. COMPUTING MDE (N and power given) 

/* FORMULA OF MDE:

MDE={t_(1-k)+t_alpha}*{(1/(P(1-P)))^(1/2)}*{(sigma^2/N)^(1/2)}

*/

scalar mde_abs=t_alphaplusbeta*p_exp*st_error

display mde_abs


*--------------------------------------------*
* 3. POWER FOR INDIVIDUAL RANDOMIZED DESIGNS *
*--------------------------------------------*

* Clearing scalars

scalar drop _all


*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/
* 3.1. MEANS AND VARIANCE OF IMPACT INDICATOR
*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/

* Variance and standard deviation

sum IncomeLabHH1, detail

scalar mean_income = r(mean)			/*Mean*/

scalar var_income = r(Var)				/*Variance*/

scalar stddev_income = r(sd)			/*Standard deviation*/

* Means for treatment and control units (Assumption: standarized effect size of 0.2 desviaciones estandar)

scalar control_income=mean_income
display control_income

scalar treat_income=control_income+0.2*stddev_income
display treat_income

scalar effect_size=treat_income-control_income
display effect_size

local control_m = control_income
local treat_m = treat_income
local sigma_m = stddev_income


*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/
* 3.2. COMPUTING POWER (USING POWER COMMAND)
*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/

power twomeans `control_m' `treat_m', sd(`sigma_m') alpha(0.05) n(1000)


*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/
* 3.3. COMPUTING POWER (USING MANUAL APPROACH)
*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/

* Clearing scalars

scalar drop _all


* A. MEANS AND VARIANCE OF IMPACT INDICATOR

sum IncomeLabHH1, detail

scalar mean_income = r(mean)			/*Mean*/

scalar var_income = r(Var)				/*Variance*/

scalar stddev_income = r(sd)			/*Standard deviation*/


* B. COMPUTING STANDARD ERRORS: (sigma^2/N)^(1/2)

scalar n_sample = 1000 				/*Asumming known sample size and we need to compute MDE*/

scalar st_error = (var_income/n_sample)^(1/2)


* C. PROPORTION OF TREATMENT AND CONTROL UNITS: (1/(P(1-P)))^(1/2) 

local p=0.5								 /*P: proportion of treatment units*/

scalar p_exp=(1/(`p'*(1-`p')))^(1/2)


* D. T-VALUES FOR ALPHA (SIGNIFICANCE LEVEL) 

scalar t_alpha=invnormal(0.975)			/*Note: 0.95 if one-sided test*/


* Parameters

display p_exp

display t_alpha


* E. COMPUTING POWER (N and effect size given) *

/*FORMULA OF POWER:

t_(1-k)=[delta/{(1/(P(1-P)))^(1/2)}*{(sigma^2/N)^(1/2)}]-t_alpha

*/

*Assume effect size (delta=280 mexican pesos or 0.2 std deviation)

scalar delta_n=0.2

scalar delta_a=delta_n*stddev_income
display delta_a

scalar t_power= (delta_a/(p_exp*st_error))- t_alpha

local t_power=t_power

scalar power=normal(`t_power')

display power


*--------------------------------------------------------------*
* 4. SAMPLE SIZE CALCULATION FOR INDIVIDUAL RANDOMIZED DESIGNS *
*--------------------------------------------------------------*


* Clearing scalars

scalar drop _all

*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/
* 4.1. MEANS AND VARIANCE OF IMPACT INDICATOR
*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/

* Variance and standard deviation

sum IncomeLabHH1, detail

scalar mean_income = r(mean)			/*Mean*/

scalar var_income = r(Var)				/*Variance*/

scalar stddev_income = r(sd)			/*Standard deviation*/

* Means for treatment and control units (Assumption: standarized effect size of 0.2 desviaciones estandar)

scalar control_income=mean_income
display control_income

scalar treat_income=control_income+0.2*stddev_income
display treat_income

local control_m = control_income
local treat_m = treat_income
local sigma_m = stddev_income


*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/
* 4.2. COMPUTING SAMPLE SIZE (USING POWER COMMAND)
*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/

power twomeans `control_m' `treat_m', sd(`sigma_m') alpha(0.05) power(0.9)


*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/
* 4.3. COMPUTING SAMPLE SIZE (USING MANUAL APPROACH)
*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/

* Clearing scalars

scalar drop _all

* A. MEANS AND VARIANCE OF IMPACT INDICATOR

sum IncomeLabHH1, detail

scalar mean_income = r(mean)			/*Mean*/

scalar var_income = r(Var)				/*Variance*/

scalar stddev_income = r(sd)			/*Standard deviation*/


* B. EFFECT SIZE

*Assume effect size (delta=280 mexican pesos or 0.2 std deviation)

scalar delta_n=0.2

scalar delta_a=delta_n*stddev_income
display delta_a


* C. PROPORTION OF TREATMENT AND CONTROL UNITS: (1/(P(1-P)))^(1/2) 

local p=0.5								 /*P: proportion of treatment units*/

scalar p_exp=(1/(`p'*(1-`p')))^(1/2)


* D. T-VALUES FOR ALPHA (SIGNIFICANCE LEVEL) AND 1-K (POWER) *

scalar t_alpha=invnormal(0.975)			/*Note: 0.95 if one-sided test*/

scalar t_beta=invnormal(0.90)

scalar t_alphaplusbeta=t_alpha+t_beta


* E. DETERMINATION OF SAMPLE SIZE (for a given effect size and power) *

/*FORMULA OF SAMPLE SIZE (n):

n = [sigma*{t_(1-k)+t_alpha}*{(1/(P(1-P)))^(1/2)}/delta]^2

*/

scalar n_sample=[stddev_income*t_alphaplusbeta*p_exp/delta_a]^2

display n_sample


*-----------------*
* 5. POWER CURVE  *
*-----------------*

* Clearing scalars

scalar drop _all

* A. MEANS AND VARIANCE OF IMPACT INDICATOR

sum IncomeLabHH1, detail

scalar mean_income = r(mean)			/*Mean*/

scalar var_income = r(Var)				/*Variance*/

scalar stddev_income = r(sd)

* Means for treatment and control units (Assumption: standarized effect size of 0.2 desviaciones estandar)

scalar control_income=mean_income
display control_income

scalar treat_income=control_income+0.2*stddev_income
display treat_income

scalar effect_size=treat_income-control_income
display effect_size

local control_m = control_income
local treat_m = treat_income
local sigma_m = stddev_income

* B. POWER CURVE

power twomeans `control_m' `treat_m', sd(`sigma_m') alpha(0.05) power(0.1(0.05)0.95) graph(y(power))


*-------------------------------------*
* 6. FACTORS AFFECTING POWER ANALYSIS *
*-------------------------------------*

scalar control_income=mean_income
display control_income

scalar treat_income02=control_income+0.2*stddev_income
display treat_income02

* Locals with parameters

local control_m = control_income
local treat_m02 = treat_income02
local sigma_m = stddev_income

*Baseline

power twomeans `control_m' `treat_m02', sd(`sigma_m') alpha(0.05) n(1000)


* A. EFFECT SIZE: Smaller effect size (0.1 std)

scalar treat_income01=control_income+0.1*stddev_income
display treat_income01

local control_m = control_income
local treat_m01 = treat_income01
local sigma_m = stddev_income

power twomeans `control_m' `treat_m01', sd(`sigma_m') alpha(0.05) n(1000)


* B. SAMPLE SIZE: Sample size of 500

local control_m = control_income
local treat_m02 = treat_income02
local sigma_m = stddev_income

power twomeans `control_m' `treat_m02', sd(`sigma_m') alpha(0.05) n(500)


* C. POWER LEVEL: Lower power level (0.8)

local control_m = control_income
local treat_m02 = treat_income02
local sigma_m = stddev_income

power twomeans `control_m' `treat_m02', sd(`sigma_m') alpha(0.05) power(0.9)

power twomeans `control_m' `treat_m02', sd(`sigma_m') alpha(0.05) power(0.8)


* D. OUTCOME VARIANCE

local control_m = control_income
local treat_m02 = treat_income02
local sigma_m2 = stddev_income*1.5

power twomeans `control_m' `treat_m02', sd(`sigma_m2') alpha(0.05) n(1000)


* E. ONE-SIDED VS TWO-SIDED TEST

local control_m = control_income
local treat_m02 = treat_income02
local sigma_m = stddev_income

power twomeans `control_m' `treat_m02', sd(`sigma_m') alpha(0.05) n(1000) onesided


* F. PROPORTION OF TREATMENT AND CONTROLS IN THE SAMPLE

local control_m = control_income
local treat_m02 = treat_income02
local sigma_m = stddev_income

power twomeans `control_m' `treat_m02', sd(`sigma_m') alpha(0.05) n1(750) n2(250)


*----------------------------*
* 7. STANDARIZED EFFECT SIZE *
*----------------------------*

power twomeans 0 0.2, sd(1) alpha(0.05) n(1000)


*-----------------------------*
* 8. ADJUSTING FOR COVARIATES *
*-----------------------------*

* Clearing scalars

scalar drop _all

* Clearing scalars

scalar drop _all

* A. MEANS AND VARIANCE OF IMPACT INDICATOR

sum IncomeLabHH1, detail

scalar mean_income = r(mean)			/*Mean*/

scalar var_income = r(Var)				/*Variance*/

scalar stddev_income = r(sd)			/*Standard deviation*/


* B. COMPUTING STANDARD ERRORS (adjusting for covariates): (sigma^2/N)^(1/2)

scalar n_sample = 1000 				/*Asumming known sample size and we need to compute MDE*/

scalar r_sq=0.3

scalar st_error = (var_income/n_sample)^(1/2)

scalar st_error_cov = ((var_income*(1-r_sq))/n_sample)^(1/2)


* C. PROPORTION OF TREATMENT AND CONTROL UNITS: (1/(P(1-P)))^(1/2) 

local p=0.5								 /*P: proportion of treatment units*/

scalar p_exp=(1/(`p'*(1-`p')))^(1/2)


* D. T-VALUES FOR ALPHA (SIGNIFICANCE LEVEL) AND 1-K (POWER) *

scalar t_alpha=invnormal(0.975)			/*Note: 0.95 if one-sided test*/

scalar t_beta=invnormal(0.90)

scalar t_alphaplusbeta=t_alpha+t_beta

* Parameters

display p_exp

display t_alpha
display t_beta


* E. COMPUTING MDE (N and power given) 

/* FORMULA OF MDE:

MDE={t_(1-k)+t_alpha}*{(1/(P(1-P)))^(1/2)}*{(sigma^2(1-R2)/N)^(1/2)}

*/

scalar mde_abs=t_alphaplusbeta*p_exp*st_error

display mde_abs


scalar mde_abs_cov=t_alphaplusbeta*p_exp*st_error_cov

display mde_abs_cov


*---------------------------------------*
* 9. ADJUSTING FOR IMPERFECT COMPLIANCE *
*---------------------------------------*

* Clearing scalars

scalar drop _all

* A. MEANS AND VARIANCE OF IMPACT INDICATOR

sum IncomeLabHH1, detail

scalar mean_income = r(mean)			/*Mean*/

scalar var_income = r(Var)				/*Variance*/

scalar stddev_income = r(sd)			/*Standard deviation*/


* B. COMPUTING STANDARD ERRORS (adjusting for covariates): (sigma^2/N)^(1/2)

scalar n_sample = 1000 				/*Asumming known sample size and we need to compute MDE*/

scalar st_error = (var_income/n_sample)^(1/2)


* C. PROPORTION OF TREATMENT AND CONTROL UNITS: (1/(P(1-P)))^(1/2) 

local p=0.5								 /*P: proportion of treatment units*/

scalar p_exp=(1/(`p'*(1-`p')))^(1/2)


* D. T-VALUES FOR ALPHA (SIGNIFICANCE LEVEL) AND 1-K (POWER) *

scalar t_alpha=invnormal(0.975)			/*Note: 0.95 if one-sided test*/

scalar t_beta=invnormal(0.90)

scalar t_alphaplusbeta=t_alpha+t_beta

* Parameters

display p_exp

display t_alpha
display t_beta


* E. NON-COMPLIANCE FACTOR 

local c=0.9
local s=0.2

scalar comp_factor=1/(`c'-`s')
display comp_factor

* F. COMPUTING MDE WITH IMPERFECT COMPLIANCE (N and power given) 

/* FORMULA OF MDE:

MDE={t_(1-k)+t_alpha}*{(1/(P(1-P)))^(1/2)}*{(sigma^2/N)^(1/2)}

*/

scalar mde_abs=t_alphaplusbeta*p_exp*st_error

display mde_abs


scalar mde_abs_impcomp=t_alphaplusbeta*p_exp*st_error*comp_factor

display mde_abs_impcomp


*------------------------------*
* 10. CLUSTER RANDOMIZED DESIGN *
*------------------------------*

* Clearing scalars

scalar drop _all


* A. ESTIMATING ICC

* Alternative 1: Computing rho from ANOVA
 
loneway IncomeLabHH1 villid
scalar rho = r(rho)
display rho

* Alternative 2: Computing rho using Maximum Likelihood

findit iccvar

quiet xtmixed IncomeLabHH1 ||  villid: , var
iccvar


* B. MEANS AND VARIANCE OF IMPACT INDICATOR

sum IncomeLabHH1, detail

scalar mean_income = r(mean)			/*Mean*/

scalar var_income = r(Var)				/*Variance*/

scalar stddev_income = r(sd)			/*Standard deviation*/


* C. COMPUTING STANDARD ERRORS: (sigma^2/N)^(1/2)

scalar n_sample = 1000 				/*Asumming known sample size and we need to compute MDE*/

scalar st_error = (var_income/n_sample)^(1/2)


* D PROPORTION OF TREATMENT AND CONTROL UNITS: (1/(P(1-P)))^(1/2) 

local p=0.5								 /*P: proportion of treatment units*/

scalar p_exp=(1/(`p'*(1-`p')))^(1/2)


* E. T-VALUES FOR ALPHA (SIGNIFICANCE LEVEL) AND 1-K (POWER) *

scalar t_alpha=invnormal(0.975)			/*Note: 0.95 if one-sided test*/

scalar t_beta=invnormal(0.90)

scalar t_alphaplusbeta=t_alpha+t_beta


* F. DESIGN EFFECT

scalar m_sample=20  /*Cluster size*/

scalar d_effect=(1+(m_sample-1)*rho)^(1/2)

display d_effect


* G. MINIMUM DETECTABLE EFFECTS FOR CLUSTER DESIGNS

* MDE individual randomized design

scalar mde_abs=t_alphaplusbeta*p_exp*st_error

display mde_abs

* MDE cluster randomized design

scalar mde_abs_cluster=t_alphaplusbeta*p_exp*st_error*d_effect

display mde_abs_cluster

* Using POWER command

scalar control_income=mean_income

local control_m = control_income
local sigma_m = stddev_income
local rho=rho

power twomeans `control_m', sd(`sigma_m') alpha(0.05) power (0.9) k1(25) k2(25) cluster m1(20) m2(20) rho(`rho')


* H. CHANGES IN THE ICC

scalar rho_04=0.4

scalar d_effect04=(1+(m_sample-1)*rho_04)^(1/2)

scalar mde_abs_cluster_04=t_alphaplusbeta*p_exp*st_error*d_effect04

display mde_abs_cluster_04


* I. CHANGES IN NUMBER OF OBSERVATIONS PER CLUSTER

scalar m_sample50=50

scalar d_effect50=(1+(m_sample50-1)*rho)^(1/2)

scalar mde_abs_cluster_50=t_alphaplusbeta*p_exp*st_error*d_effect50

display mde_abs_cluster_50
