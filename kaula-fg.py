from sympy import *
import math as math
import numpy as np
def ffun(l, m, p, inc):
    c, s, t = symbols('c s t', integer=True)
    k = math.trunc((l - m) / 2)
    y = Sum(((factorial(2 * l - 2 * t)) / (
            factorial(t) * factorial(l - t) * factorial(l - m - 2 * t) * 2 ** (2 * l - 2 * t)) * (
                 (sin(inc) ** (l - m - 2 * t)))) * Sum(binomial(m, s) * ((cos(inc)) ** s) * Sum(
        binomial(l - m - 2 * t + s, c) * binomial(m - s, p - t - c) * (-1) ** (c - k), (c, 0, 5)), (s, 0, m)),
            (t, 0, min(p, k))).doit()
    return y

def gfun(l, p, q, e):
    if p > l / 2:
        pp = l - p
        qp = -q
    else:
        pp = p
        qp = q

    beta = e / (1 + sqrt(1 - e ** 2))

    qqq = 0
    for k in range(0, 10 + 1):
        if qp < 0:
            hp = k
            hq = k - qp
        else:
            hp = k + qp
            hq = k
        plpq = 0
        qlpq = 0
        for rp in range(0, hp + 1):
            plpq = plpq + binomial(2 * pp - 2 * l, hp - rp) * (((-1) ** rp) / factorial(rp)) * (
                    (l - 2 * pp + qp) * e / (2 * beta)) ** rp
        for rq in range(0, hq + 1):
            qlpq = qlpq + binomial(-2 * pp, hq - rq) / factorial(rq) * (
                    (l - 2 * pp + qp) * e / (2 * beta)) ** rq
        qqq = qqq + plpq * qlpq * beta ** (2 * k)

    z = (-1) ** abs(q) * (1 + beta ** 2) ** l * beta ** abs(q) * qqq

    return z



def getpt(l,m,p,q,inc,e):
	l = l
	m = m
	p = p
	q = q
	inc = inc
	e = e

	f = ffun(l, m, p, inc)
	g = gfun(l, p, q, e)
	#print("l =", l)
	#print("m =", m)
	#print("p =", p)
	#print("q =", q)
	#print("F =", f)
	#print("G =", g)

	pt=f*g

	return pt


l = 2
m = 0
p = 1
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt1=f*g

l = 2
m = 0
p = 1
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt2=f*g



l = 2
m = 0
p = 0
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt3=f*g



l = 2
m = 0
p = 0
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt4=f*g



l = 2
m = 0
p = 2
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt5=f*g



l = 2
m = 0
p = 2
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt6=f*g


tot_20=pt1+pt2+pt3+pt4+pt5+pt6



######


l = 2
m = 2
p = 0
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)

pt1=f*g

#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)



l = 2
m = 2
p = 0
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt2=f*g



l = 2
m = 2
p = 1
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt3=f*g



l = 2
m = 2
p = 1
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt4=f*g



l = 2
m = 2
p = 2
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt5=f*g



l = 2
m = 2
p = 2
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt6=f*g


if m == 0:
	fac=math.factorial(l-m)/math.factorial(l+m)
else:
	fac=2*math.factorial(l-m)/math.factorial(l+m)

tot_22=(pt1+pt2+pt3+pt4+pt5+pt6)*fac



######


l = 2
m = 1
p = 0
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)

pt1=f*g

#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)



l = 2
m = 1
p = 0
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt2=f*g



l = 2
m = 1
p = 1
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt3=f*g



l = 2
m = 1
p = 1
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt4=f*g



l = 2
m = 1
p = 2
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt5=f*g



l = 2
m = 1
p = 2
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt6=f*g


if m == 0:
	fac=math.factorial(l-m)/math.factorial(l+m)
else:
	fac=2*math.factorial(l-m)/math.factorial(l+m)

tot_21=(pt1+pt2+pt3+pt4+pt5+pt6)*fac
######


pt1=getpt(3,3,0,1,6.7*3.14159/180,0.0549)
pt2=getpt(3,3,0,-1,6.7*3.14159/180,0.0549)
pt3=getpt(3,3,1,-1,6.7*3.14159/180,0.0549)
pt4=getpt(3,3,1,1,6.7*3.14159/180,0.0549)
pt5=getpt(3,3,2,-1,6.7*3.14159/180,0.0549)
pt6=getpt(3,3,2,1,6.7*3.14159/180,0.0549)
pt7=getpt(3,3,1,0,6.7*3.14159/180,0.0549)
pt8=getpt(3,3,2,0,6.7*3.14159/180,0.0549)
pt9=getpt(3,3,3,0,6.7*3.14159/180,0.0549)


m = 3
l = 3



if m == 0:
	fac=math.factorial(l-m)/math.factorial(l+m)
else:
	fac=2*math.factorial(l-m)/math.factorial(l+m)

tot_33=(pt1+pt2+pt3+pt4+pt5+pt6+pt7+pt8+pt9)*fac



######


l = 3
m = 1
p = 1
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)

pt1=f*g

#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)



l = 3
m = 1
p = 1
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt2=f*g



l = 3
m = 1
p = 0
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt3=f*g



l = 3
m = 1
p = 0
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt4=f*g



l = 3
m = 1
p = 2
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt5=f*g



l = 3
m = 1
p = 2
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt6=f*g

pt7=getpt(3,1,1,0,6.7*3.14159/180,0.0549)
pt8=getpt(3,1,2,0,6.7*3.14159/180,0.0549)
pt9=getpt(3,1,3,0,6.7*3.14159/180,0.0549)


if m == 0:
	fac=math.factorial(l-m)/math.factorial(l+m)
else:
	fac=2*math.factorial(l-m)/math.factorial(l+m)

tot_31=(pt1+pt2+pt3+pt4+pt5+pt6+pt7+pt8+pt9)*fac


######


l = 3
m = 2
p = 0
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)

pt1=f*g

#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)



l = 3
m = 2
p = 0
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt2=f*g


l = 3
m = 2
p = 1
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)

pt3=f*g

#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)



l = 3
m = 2
p = 1
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt4=f*g




l = 3
m = 2
p = 2
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)

pt5=f*g

#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)



l = 3
m = 2
p = 2
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt6=f*g

pt7=getpt(3,2,1,0,6.7*3.14159/180,0.0549)
pt8=getpt(3,2,2,0,6.7*3.14159/180,0.0549)
pt9=getpt(3,2,3,0,6.7*3.14159/180,0.0549)

if m == 0:
	fac=math.factorial(l-m)/math.factorial(l+m)
else:
	fac=2*math.factorial(l-m)/math.factorial(l+m)

tot_32=(pt1+pt2+pt3+pt4+pt5+pt6+pt7+pt8+pt9)*fac

######


l = 3
m = 0
p = 2
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)

pt1=f*g

#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)



l = 3
m = 0
p = 2
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt2=f*g


l = 3
m = 0
p = 1
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)

pt3=f*g

#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)



l = 3
m = 0
p = 1
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt4=f*g




l = 3
m = 0
p = 0
q = 1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)

pt5=f*g

#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)



l = 3
m = 0
p = 0
q = -1
inc = 6.7*3.14159/180
e = 0.0549

f = ffun(l, m, p, inc)
g = gfun(l, p, q, e)
#print("l =", l)
#print("m =", m)
#print("p =", p)
#print("q =", q)
#print("F =", f)
#print("G =", g)

pt6=f*g



pt7=getpt(3,0,1,0,6.7*3.14159/180,0.0549)
pt8=getpt(3,0,2,0,6.7*3.14159/180,0.0549)
pt9=getpt(3,0,3,0,6.7*3.14159/180,0.0549)


if m == 0:
	fac=math.factorial(l-m)/math.factorial(l+m)
else:
	fac=2*math.factorial(l-m)/math.factorial(l+m)


#print(pt9+pt10)

tot_30=(pt1+pt2+pt3+pt4+pt5+pt6+pt7+pt8+pt9)*fac

Moon_Radius= 1737.4 # km
Earth_distance= 384399 # km

fac_2=(Moon_Radius/Earth_distance)**(3) 
fac_3=(Moon_Radius/Earth_distance)**(4) 



vec=np.zeros(7)


#print(fac_2/fac_3)


k20_meas=2.44247443068e-02
k21_meas=2.42025500776e-02
k22_meas=2.41823548003e-02
k30_meas=1.64447651523e-02
k31_meas=1.56026251733e-02
k32_meas=1.83038653457e-02
k33_meas=1.38802515203e-02
h2_meas=0.0387 #Thor et al., 2021


def getnorm(l,m):
	if m == 0:
		fac=math.factorial(l-m)/math.factorial(l+m)
	else:
		fac=2*math.factorial(l-m)/math.factorial(l+m)
	return fac



tot_20=-((5-3.3)/2)/(k20_meas)
tot_21=-((1.5+2)/2)/(k21_meas)
tot_22=((8.5-5.7)/2)/(k22_meas)
tot_30=((8*1e-3)/2)/(k30_meas)
tot_31=-((6*1e-3)/2)/(k31_meas)
tot_32=-((10*1e-3)/2)/(k32_meas)
tot_33=((8*1e-3)/2)/(k33_meas)




print("Total for 2,0 = ", (tot_20/tot_22)**-1 )
print("Total for 2,1 = ", (tot_21/tot_22)**-1 )
print("Total for 2,2 = ", (tot_22/tot_22)**-1 )
print("Total for 3,0 = ", (tot_30/tot_22)**-1 )
print("Total for 3,1 = ", (tot_31/tot_22)**-1 )
print("Total for 3,2 = ", (tot_32/tot_22)**-1 )
print("Total for 3,3 = ", (tot_33/tot_22)**-1 )



vec[0]=tot_20
vec[1]=tot_21*(-1)
vec[2]=tot_22
vec[3]=tot_30
vec[4]=tot_31*(-1)
vec[5]=tot_32
vec[6]=tot_33*(-1)



np.savetxt('Potentials.txt',vec)

#print("Total for 3,0 relative to 2,0= ", tot_31/tot_20 )

