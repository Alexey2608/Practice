class Time(BaseException):
    pass
def way(uskor):
    def wrapper(v0,v,t):
        a= uskor(v0,v,t)
        print('a= ',a)
        s=v0*t+a*t*t/2
        print('S= ',s)
    return wrapper
@way
def uskor(v0,v,t):
    a=(v-v0)/t
    return a
try:
    v=int(input())
    v0=int(input())
    t=int(input())
    if t<1:
        raise Time('Time error')
    uskor(v0,v,t)
except ValueError:
    print("Value error")
except T_except:
    print("Time error")