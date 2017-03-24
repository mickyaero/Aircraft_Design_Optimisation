from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#-----stalling speed constraint-----
wit=2
span_efficiency = 0.9
aspect_ratio = 3.09
cl_airfoil_max = 1.9
wing_area=27.87
k=3.14*span_efficiency*aspect_ratio
k=1/k
cl_wing = cl_airfoil_max/(1+2/(aspect_ratio*span_efficiency))
rho_sl = 1.225
v_stall = 300*5/18

axes = plt.gca()
axes.set_ylim([0,2])
axes.set_xlim([5,10000])
#***Constraint***

w_s1_c = 0.5*rho_sl*v_stall**2*cl_wing
w_s1 = [0 for i in range(500)]
for i in range(500):
    w_s1[i]=w_s1_c

nt_w1 = np.linspace(0,2,500)
plt.plot(w_s1,nt_w1, linewidth=wit,label='Stall Speed')
#-----Subsonic Sustained turn rate constraint-----
cd_0=0.0175
mach_1500 = 0.9
cl_str = 1
rho_1500 = 1.056
#cd = cd_0 + cl**2/(3.14*span_efficiency*aspect_ratio)
temp_1500 = 278.25
vel_1500 = (1.4*287*temp_1500)**0.5*mach_1500
lf_1500 = 9
w_s2 = np.linspace(5, 10000, 2500)
q21 =0.5*rho_1500*vel_1500**2
#******

t_w1 = q21*cd_0/w_s2 + w_s2*(lf_1500**2/(q21)*k)

plt.plot(w_s2, t_w1,linewidth=wit, label = 'Sub STR')



#******
"""conditional line
t_w2_c = 2*lf_1500*(cd_0/(3.14*aspect_ratio*span_efficiency)**0.5)
w_s_d1 = np.linspace(5,10000,2500)
t_w2 = [0 for i in range(2500)]
for i in range(2500):
    t_w2[i] = t_w2_c

plt.plot(w_s_d1,t_w2,label='Sub STR Cdn')
"""
#-----Supersonic str constraint------
temp_9000 = 229.65
mach_9000 = 1.2
rho_9000=0.46635
vel_9000=(1.4*287*temp_9000)**0.5*mach_9000
lf_9000=4
w_s3 = np.linspace(5, 10000, 2500)
q23=0.5*rho_9000*vel_9000**2
#**********
t_w3 = q23*cd_0/w_s3 + w_s3*lf_9000**2/(q23)*k
#plt.t_w3([0, 2])
plt.plot(w_s3, t_w3,linewidth=wit, label='Super STR')

#********
"""conditional line
t_w4c = 2*lf_9000*(cd_0/(3.14*aspect_ratio*span_efficiency)**0.5)
t_w4 = [0 for i in range(2500)]
for i in range(2500):
    t_w4[i] = t_w4c

wsde = np.linspace(5,10000,2500)
plt.plot(t_w4, wsde, label='Super STR Cdn')
"""
#Instantaneous turn rate constraint
omega = 18*3.14/180
gravity=9.8
mach_itr = 0.9
rho_itr = 0.6597
temp_itr =249.15
vel_itr=mach_itr*(1.4*temp_itr*287)**0.5
lf = ((omega*vel_itr/gravity)**2+1)**0.5
cl_itr_max = 1
w_man = 9862.5
w_to = 16875
#********
w_s4c = 0.5*rho_itr*vel_itr**2*cl_itr_max/lf*(w_to/w_man)
w_s4=[0 for i in range(1000)]
for i in range(1000):
    w_s4[i]=w_s4c

twnw = np.linspace(0,2,1000)
plt.plot(w_s4,twnw,linewidth=wit, label='ITR')
#maximum mach number constraint
rho_mmn = 0.0880349
mmn=2
temp_mmn=216.650
vel_mmn= (1.4*temp_mmn*287)**0.5*mmn
b_mmn = w_man/w_to
alpha_mmn = rho_mmn/rho_sl*(1+0.7*mmn)
lf_mmn=1
w_s5 = np.linspace(5, 10000, 250)
q5=0.5*rho_mmn*vel_mmn**2

#*******
t_w5 =b_mmn/alpha_mmn*(q5/b_mmn*((cd_0/w_s5)+(k*((lf_mmn*b_mmn/q5)**2)*w_s5))) 


plt.plot(w_s5,t_w5,linewidth=wit, label='Max Mach Number')
#specific excees power constraint
rho_sep = 1.056
mach_sep=0.9
temp_sep = 278.25
vel_sep=(1.4*287*temp_sep)**0.5*mach_sep
cl_sep = w_to/(0.5*rho_sep*vel_sep**2*wing_area)
sep = 150
cd = cd_0+cl_sep**2 *k
#***********

t_w6c=sep/vel_sep+0.5*rho_sep*vel_sep**2*cd/w_to
t_w6= [0  for i in range(2500)]
for i in range(2500):
    t_w6[i]=t_w6c

wdx = np.linspace(5,10000,2500)
plt.plot(wdx,t_w6,linewidth=wit, label='SEP')
#rate of climb constraint
roc=160
vel_roc = 500*5/18*1.852
b_roc=1
alpha_roc=1
rho_roc= rho_sl
q44=0.5*rho_roc*vel_roc**2
#*******
w_s6 = np.linspace(5, 10000, 2500)

t_w7=b_roc/alpha_roc*(q44/b_roc*(cd_0/w_s6+(b_roc/q44)**2*w_s6*k)+roc/vel_roc)
#plt.t_w7([0, 2])

plt.plot(w_s6, t_w7,linewidth=wit, label='ROC')
#take off field length constraint
to_roll=900
cl_to=1.27
rho_to =1.11164
w_s7 = np.linspace(5, 10000, 2500)

#*************
t_w8 = 1.44/(to_roll*cl_to*rho_to*gravity)*w_s7

plt.plot(w_s7,t_w8,linewidth=wit,label='TOFL')
#landing distance constraint
meu_roll = 1
cl_land = 1.43
rho_land=1.11164
land_roll=900
b_land=1
w_s8_c = land_roll*rho_land*cl_land*gravity*meu_roll/(1.69*b_land)
w_s8 = [0 for i in range(500)]
for i in range(500):
    w_s8[i]= w_s8_c
twd = np.linspace(0,2,500) 
plt.plot(w_s8, twd, linewidth=wit,label = 'Landing Distance')
plt.xlabel("W/S")
plt.ylabel("T/W")
plt.grid(1)
plt.legend(loc='best')
plt.show()

