#Interpolation and extrapolation

def int_estr_interface(x,y):
    N=len(x)
    assert (N==len(y)), 'Size x is different from size y!'                          #dimension control
    assert (x[N-1]>x[0]), 'The data set is not ordered!'                            #interval control
    while (True):
        op=input('Do you want to make an interpolation or an extrapolation?(i,e) ')
        if (op=='i'):
            a2=x[0]
            b2=x[N-1]
        elif (op=='e'):
            a2=float(input('Insert left point of the new interval: '))
            b2=float(input('Insert right point of the new interval: '))
        else:
            print('Invalid option. Try again.')
            continue
        interp(N,x,y,a2,b2)
        if not(input('Do you want to try again?(S/n) ')=='S'): break

def int_estr(x,y,a,b):
    N=len(x)
    assert (N==len(y)), 'Size x is different from size y!'                     
    assert (x[N-1]>x[0]), 'The data set is not ordered!'                           
    while (True):
        interp(N,x,y,a,b)
        if not(input('Do you want to try again?(S/n) ')=='S'): break
    

def interp(N, x, y, a2, b2):
    print('\nThe implemented methods are lagrange, aitken and updown:'
          '\n-use lagrange if you want a good interpolation method;'
          '\n-use aitken if you want a smarter version of lagrange;'
          '\n-use updown if you want a good extrapolation method.')
    method_list={'lagrange': lagrange, 'aitken': aitken, 'updown': updown}
    m=input('Select a method: ')
    if m in method_list:
        print('\n'+(m+' method').upper())
        print('The starting number of points is {0}.'. format(N))
        D=int(input('Insert the number of points you need: '))
        file=open("datainterp.txt","w")
        x0= [a2 + i*(b2-a2)/(D-1) for i in range(D)]
        y0= [method_list[m](N, x, x0[i], y) for i in range(D)]
        for i in range(D):
            file.write("\n{0} {1} {2}". format(i+1, x0[i], y0[i]))
        file.close()
        print('Your data file is ready.')
    else:
        print('Sorry, this method had not been implemented yet!\n')
    


def lagrange(N, x, x0, y):
    for l in range(N):
       if (x[l]==x0): 
           return y[l]
    y0=0.0
    for l in range(N):
       prod=1.0
       for m in range(N):
          if(m==l): continue 
          prod=prod*(x0-x[m])/(x[l]-x[m])
       y0=y0+prod*y[l]
    return y0

def aitken(N, x, x0, y):
    for l in range(N):
       if (x[l]==x0): 
           return y[l]
    z=[y[i] for i in range(N)]
    for k in range(N-2):
        for i in range(N-k-1):
           z[i]=((x0-x[i+k+1])/(x[i]-x[i+k+1]))*z[i]+((x0-x[i])/(x[i+k+1]-x[i]))*z[i+1]
    return z[0]

#nearest_i = Minloc(Abs(x-xs),1)

def updown(N, x, x0, y):
    """
    Real(rk) :: delta_plus(Size(x),Size(x))  ! Auxiliary matrices delta+
    Real(rk) :: delta_minus(Size(x),Size(x)) ! Auxiliary matrices delta-
    Real(rk) :: aux,dx,delta(Size(x))            ! Auxiliary quantity, difference between xs and closest point, delta to be summed up
    Integer(4) :: N,i,j,near,near_p,near_m           ! N, running integers, closest-point index, running indexes in re-summation

    delta_plus(:,1) = y  ! Loading the auxiliary matrices delta+(:,0) with values of y
    delta_minus(:,1) = y ! Loading the auxiliary matrices delta-(:,0) with values of y
    N = Size(x)          ! Compute the value of N
    Do j = 1, N-1          ! up-down recursion
       Do i = 1, N-j
          aux = (delta_plus(i,j) - delta_minus(i+1,j)) / (x(i) - x(i+j))
          delta_plus(i,j+1) = (x0 - x(i+j)) * aux
          delta_minus(i,j+1) = (x0 - x(i)) * aux
       Enddo
    Enddo
    near=nearest_i(x,x0)
    near_m=near
    near_p=near
    dx=x0-x(near)
    delta(1) = delta_plus(near,1)
    Do i= 2, N
       If ((dx<0.Or.near_p==N).And.near_m>1) Then
          near_m = near_m - 1
          delta(i) = delta_plus(near_m,i)
          dx = -dx
       Else
          delta(i) = delta_minus(near_m,i)
          near_p = near_p + 1
          dx = -dx
       Endif
    Enddo
    y0 = delta(N)
    Do i= N-1, 1, -1
       y0 = y0 + delta(i)
    Enddo
    """
#-----------------------------------------------------------------------
a=3.0
b=9.0
N=5
x=list(map(lambda x: a+x*(b-a)/N, range(N+1)))
y=[x[i]**2 for i in range(N+1)]
int_estr_interface(x,y)
