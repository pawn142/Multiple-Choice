from decimal import *
getcontext().prec = 100
pools = [8,8,8]
acc = 32
h = [[Decimal(m) for m in pools], float('inf')]
r = lambda j,g : sum(j(k) for k in g)
s = lambda x,y,p : r(lambda v : 2/((v/y-x)+((v/y-x)**2+4).sqrt()),p)-x
t = lambda x,y,p : r(lambda v : (v/x-y)/((v/x-y)**2+4).sqrt(),p)-len(p)+2
def u(x,y,q):
    f = lambda o : y(x,o,q[0])
    n = Decimal(0)
    while q[1] < 2**(n+1) or 0 < f(2**(n+1))*f(2**n):
        n = (n < 1)-n
    a = 2**n
    b = 2*a
    while abs(f(a)) > 2**-acc:
        a += (0 <= f(a)*f((a+b)/2))*(b-a)/2
        b += (0 > f(a)*f((a+b)/2))*(a-b)/2
    return a
w = u(0,lambda d,i,e : u(u(i,t,h),s,h)-i,[0,u(0,lambda x,y,l : t(y,x,l),h)])
z = w*u(w,t,h)
ys = [(c-z+((c-z)**2+4*w*w).sqrt())/2 for c in h[0]]
ns = [w*w/y for y in ys]