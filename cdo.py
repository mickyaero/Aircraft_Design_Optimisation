import math
rho = 0.3482675 
temp = 216.7 #in kelvin
test = 0
#at 37,000 ft
r = 286.9
gamma = 1.40166
a = (gamma * r * temp) ** 0.5
mach_no = 0.85
vel = mach_no * a

viscosity = 1.4217183 * 10 ** -5
cor_b = 1.01494
cor_l = 1.02851
cor_h = 1.004062

cl = 0.508
ne = 2 #no of engines on the wing
s_ref = 359.53
q = 0.5 * rho * vel ** 2
coeff_friction = 1.33 * 10 **-5 
#wing data starts ...after converting to trapezoidal wing
c_t_w = 1.5986 #chord at the tip of the wing
c_r_w = 11.08609586 #chord at the root of the wing....the point where the wing starts....i.e ...it touches the fuselage
b_wing = 60.14
s_c_w = 412.6811281 #total area of the trapezoidal wing
s_e_w = 331.101762 #exposed area of the wing, i.e, actual wing exposed
t_c_r_w = 0.134 #thickness to chord ratio at the root of the wing
t_c_t_w =0.088 #thickness to chord ratio at the tip of the wing
w_laminar = 0.1
swept_4_w = 34.176*3.14/180
swept_25_w = 32.176*3.14/180
x_c_w = 0.4 #max thickness for wing
inter_wing = 1.00
#wing data ends

#winglet data starts
c_t_wl = 1.08761784
c_r_wl = 1.98330312
s_e_wl = 0.2087431
t_c_r_wl = 0.088
t_c_t_wl = 0.088
wl_laminar = 0
swept_4_wl = 55.97*3.14/180
swept_25_wl = 53.97*3.14/180
x_c_wl = 0.4
inter_wl = 1.05
#winglet data ends

#horizontal stabilizer data starts
c_t_hs = 1.66341552
c_r_hs = 5.69399
s_e_hs = 71.03906128
t_c_r_hs = 0.1
t_c_t_hs = 0.1
hs_laminar = 0.1
swept_4_hs = 37.1 * 3.14/180
swept_25_hs = 36.09*3.14/180
x_c_hs = 0.4
inter_hs = 1.05

#vertical stabilizer data end
c_t_vs = 2.631484
c_r_vs = 7.494
s_e_vs = 46.1580447
t_c_r_vs = 0.1
t_c_t_vs = 0.1
vs_laminar = 0.1
swept_4_vs = 41.63*3.14/180
swept_25_vs = 39.63*3.14/180
x_c_vs = 0.4
inter_vs = 1.05
#vertical stabilizer data ends

#nacelle data starts
len_nac = 6.0645345
dia_nac = 3.643310686
swn=63.1916 #nacelle wetted surface area...error could be here
inter_nac =1.15
#nacelle data ends

#fuselage data starts
len_fuse = 56.56
width_fuse = 5.708312543
depth_fuse = 5.920379
upsweep = 0.24492 #in radians
swf =855.565 #fuselage wetted surafce area...error could be here
inter_fuse = 1.05 
#fuselage data ends
#skin friction coeff calculator for wing, HS, VS
def skin_fric_1(c_t, c_r, s_e, laminar):
    
    lamb = c_t/c_r
    Mac = 2/3 * c_r *(1 + lamb + lamb **2)/(1 + lamb)
    if laminar == 0: #full turbulent
       rey_to_tur = rho *vel * Mac/viscosity
       rey_to_cut = 38.21 * (Mac/coeff_friction) ** 1.053
      
       if rey_to_tur >= rey_to_cut:
          rey_to = rey_to_cut
      
       else:
          rey_to = rey_to_tur
       c_f  = 0.455/((math.log10(rey_to)**2.58) *(1 + 0.144 * mach_no **2) ** 0.65 ) 
       return c_f

    else:
       macl = laminar * Mac
       rey_l = rho * vel * macl/viscosity
            
       c_f_l = 1.328/(rey_l) ** 0.5
       se_l = laminar * s_e
       d_lam = q * se_l *c_f_l #laminar drag
       
       rey_to_tur = rho *vel * Mac/viscosity
       rey_to_cut = 38.21 * (Mac/coeff_friction) ** 1.053
      
       if rey_to_tur >= rey_to_cut:
          rey_to = rey_to_cut
      
       else:
          rey_to = rey_to_tur
      
       c_f_tt  = 0.455/((math.log10(rey_to)**2.58) *(1 + 0.144 * mach_no **2) ** 0.65 ) 
       d_t_tt = q * s_e * c_f_tt #turbulent full area drag
      
       rey_to_tur_l = rho *vel * macl/viscosity
       rey_to_cut_l = 38.21 * (macl/coeff_friction) ** 1.053
      
       if rey_to_tur_l >= rey_to_cut_l:
          rey_to_l = rey_to_cut_l
      
       else:
          rey_to_l = rey_to_tur_l
      
       c_f_tl  = 0.455/((math.log10(rey_to_l)**2.58) *(1 + 0.144 * mach_no **2) ** 0.65 ) 
       d_t_tl = q * se_l * c_f_tl

       d_t_f = d_t_tt - d_t_tl
       drag = d_t_f + d_lam
       c_f = drag / (q*s_e) 
       return c_f



def skin_fric_2(length):
     rey_to_tur = rho *vel *length /viscosity
     rey_to_cut = 38.21 * (length/coeff_friction) ** 1.053
      
     if rey_to_tur >= rey_to_cut:
        rey_to = rey_to_cut
      
     else:
        rey_to = rey_to_tur
    
     c_f  = 0.455/((math.log10(rey_to)**2.58) *(1 + 0.144 * mach_no **2) ** 0.65 ) 
     return c_f

#calculating c_f for wing, hs, vs, fuselage and nacelle
c_f_wing = skin_fric_1(c_t_w, c_r_w, s_e_w, w_laminar)
c_f_wl = skin_fric_1(c_t_wl, c_r_wl, s_e_wl, wl_laminar)
c_f_hs = skin_fric_1(c_t_hs, c_r_hs, s_e_hs, hs_laminar)
c_f_vs = skin_fric_1(c_t_vs, c_r_vs, s_e_vs, vs_laminar)
c_f_fu = skin_fric_2(len_fuse)
c_f_na = skin_fric_2(len_nac)

#calculating the form factors 
def form(xc, tcr, tct, swept4):
    tc = 0.25*(tcr + 3*tct)
    ff = (1+0.6/xc*tc + 100* tc ** 4)*(1.34*mach_no ** 0.18 * math.cos(swept4)**0.28)
    return ff
  #form factors for wing, hs, and winglet
ff_wing = form(x_c_w, t_c_r_w, t_c_t_w, swept_4_w)
ff_wl = form(x_c_wl, t_c_r_wl, t_c_t_wl, swept_4_wl)
ff_hs = form(x_c_hs, t_c_r_hs, t_c_t_hs, swept_4_hs)
ff_vs = form(x_c_vs, t_c_r_vs, t_c_t_vs, swept_4_vs)
  #form factor for fuselage and nacelle
  #fuselage
a_max_f =3.14/4*width_fuse*depth_fuse
f_fuse = len_fuse/(4/3.14 * a_max_f) ** 0.5
ff_fuse = 1+60/f_fuse ** 3 + f_fuse/400
  #nacelle
a_max_n = 3.14/4*dia_nac ** 2
f_nac = len_nac/(4/3.14*a_max_n) ** 0.5
ff_nac = 1+ 0.35/f_nac
#calculating miscellaneous drag
d_q =3.83 * a_max_f * upsweep**2

#calculating the wetted area
def tc(tcr,tct):
    tc = 0.25 * (tcr + 3*tct)
    return tc

sww = s_e_w *(1.977 + 0.52 * tc(t_c_r_w, t_c_t_w))
swwl = s_e_wl*(1.977 + 0.52 * tc(t_c_r_wl, t_c_t_wl))
swhs = s_e_hs * (1.977 + 0.52 *tc(t_c_r_hs, t_c_t_hs))
swvs = s_e_vs * (1.977 + 0.52 * tc(t_c_r_vs, t_c_t_vs))

#calculating the drag of each component
cdw = c_f_wing * ff_wing * inter_wing * sww/s_ref
cdwl = c_f_wl *ff_wl *inter_wl * swwl/s_ref
cdvs = c_f_vs * ff_vs * inter_vs * swvs/s_ref
cdhs = c_f_hs * ff_hs * inter_hs *swhs/s_ref
cdn  = c_f_na * ff_nac *inter_nac *swn/s_ref
cdf = (d_q + ff_fuse * c_f_fu * swf * inter_fuse)/s_ref
cd_0 =cdf + cdn+cdhs+cdvs+cdwl+cdw
#calculating cdi
a_w = 1.2 * b_wing ** 2/s_c_w
f_wing = 0.005 *(1+1.5*(c_t_w/c_r_w - 0.6)**2)
e = ((1+0.12*mach_no ** 6) * (1+(0.142+f_wing*a_w*(10 * tc(t_c_r_w, t_c_t_w))**0.33)/(math.cos(swept_25_w))**2 + 0.1*(3*ne+1)/(1+a_w)**0.8)) **(-1)

cdi = cl**2/3.14/a_w/e
cdnought = cdi + cd_0
print((cdnought-0.02299)*100/0.02299)
