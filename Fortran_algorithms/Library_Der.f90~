Module LibraryDer

  Use LibraryInterp
  
Contains                                                   
!*********************************************************************************************************************************************
  Function Der(x,y,l,o,m,e,dy) result (stat)             !result dichiara la var da utilizzare al posto del nome della funzione
    !stat=0 successo                                     !valori che assume lo stat, associati al tipo di errore commesso
    !stat=1 Size(x)/=Size(y)
    !stat=2 l<0 or l>N
    !stat=3 o<1 or o>2 ordine di derivazione                                 
    !stat=4 m<1 or m>3 m+2 sono i punti della formula usata per il calcolo

    Implicit none
    real(rk), Intent (In):: x(0:), y(0:)
    integer(rk), Intent (In):: l,o,m,e                   !l: indice del punto in cui voglio la derivata; o: ordine derivata
    real(rk), Intent (Out):: dy                          !m: numero di punti della formula usata; e:numero di punti da usare per interp 
    integer(4):: stat

    integer(4)::k,N
    real(rk):: xm,xp,ym,yp,bn(1:3,1:3)=0                 !bn: matrice dei coefficienti della comb lin, p: plus, m: minus 

    bn(1,1)=1._rk
    bn(1,2)=4._rk/3._rk
    bn(2,2)=-1._rk/3._rk
    bn(1,3)=1.5_rk
    bn(2,3)=-0.6_rk
    bn(3,3)=0.1_rk
    
    N=size(x)-1
    if (Size(x)/=Size(y)) then                           !Controllo preliminare
       stat=1
       return
    end if
     if (l<0.or.l>N) then
       stat=2
       return
    end if
     if (o<1.or.o>2) then
       stat=3
       return
    end if
     if (m<1.or.m>3) then
       stat=4
       return
    end if

    dy=0                                                 !Algoritmo di derivazione
    Do k=1,m
       if(l<k) then                                      !Estrapola punti a sinistra
          xm=x(0) + (l-k)*(x(1)-x(0))
          call interp_aitken(x(0:Min(e-1,N)),y(0:Min(e-1,N)),xm,ym)
          xp=x(l+k)
          yp=y(l+k)
       else if (l>N-k)then                               !Estrapola punti a destra
          xm=x(l-k)
          ym=y(l-k)
          xp=x(N)+ (l-(N-k))*(x(N)-x(N-1))
          call interp_aitken(x(0:Max(0,N+1-e)),y(0:Max(0,N+1-e)),xp,yp)
       else
          xm=x(l-k)
          xp=x(l+k)
          ym=y(l-k)
          yp=y(l+k)
       end if
       
       Select case(o)                                    !Formula a seconda dell'ordine 'o' della derivata
       Case(1)
          dy=dy+bn(k,m)*(yp-ym)/(xp-xm)
       Case(2)
          dy=dy+bn(k,m)*(yp-2._rk*y(l)+ym)/(0.25_rk*(xp-xm)**2)
       End select
    End do
    stat=0
  End Function Der
  
!*********************************************************************************************************************************************
  Recursive Function Der_fun(fun,x0,o,h_ini,eps,max_steps,steps_,Dfun) Result(stat)
  ! stat=0 success
  ! stat=1 max_steps overcome
  ! stat=2 diff. order not implemented

    Implicit None
    Procedure(fun_R_R) :: fun
    Real(rk), Intent(in) :: x0,h_ini,eps                                !h_ini=semidistanza tra i punti del calcolo
    Integer(4), Intent(in) :: o,max_steps
    Integer(4), Intent(out) :: steps_
    Real(rk), Intent(out) :: Dfun
    Integer(4) :: stat

    Integer(4), Save :: steps=1
    Real(rk) :: Dyh,Dyh2
    Real(rk), Save :: Dyh_old

    If (steps==1) Then                                                  !Inizializzazione 
       Select Case(o)
       Case(1)
          Dyh=(fun(x0+h_ini)-fun(x0-h_ini))/(2._rk*h_ini)
       Case(2)
          Dyh=(fun(x0+h_ini)-2._rk*fun(x0)+fun(x0-h_ini))/(h_ini**2)
       Case Default
          stat=2
          steps_=0
          steps=1
          Return
       End Select
    Else 
       Dyh=Dyh_old                                                      !Slittamento del valore di Dyh2 precedente
    End If
    
    Select Case(o)
    Case(1)
       Dyh2=(fun(x0+h_ini/2)-fun(x0-h_ini/2))/h_ini
    Case(2)
       Dyh2=(fun(x0+h_ini/2)-2._rk*fun(x0)+fun(x0-h_ini/2))/((h_ini**2)/4._rk)
    End Select
    Dyh_old=Dyh2                                                        !Mette nella variabile salvata il risultato

    If (Abs(Dyh-Dyh2)<=eps*Abs(Dyh2)) Then                              !Controllo per l'interruzione del programma
       Dfun=4._rk/3._rk*Dyh2-Dyh/3._rk
       stat=0
       steps_=steps
       steps=1
       Return
    End If
    
    steps=steps+1
    If (steps>max_steps) Then
       stat=1
       steps_=max_steps
       steps=1
       Return
    End If
    
    stat=Der_fun(fun,x0,o,h_ini/2,eps,max_steps,steps_,Dfun)           !Chiamata ricorsiva con la distanza dimezzata 
    
  End Function Der_fun

!*********************************************************************************************************************************************
  Function integrate(x,y,integr,Method) result(stat) 

    Implicit None
    Real(rk), Intent(In) :: x(0:), y(0:)
    Character(Len=*), Intent(In) :: Method
    Real(rk) :: integr
    Integer(4):: stat

    Integer(4) ::N,p
    Real(rk) :: w(0:Size(x)-1), Delta
    Delta=x(1)-x(0)
    N=Size(x)-1

    Select case(trim(Method))                                !Assegnazione dei coefficienti a seconda del metodo d'integrazione
    Case('simpson')
       Do p=1,N-1
          if ((p/2)*2==p) then
             w(p)=2._rk/3._rk
          else
             w(p)=4._rk/3._rk
          end if
       end do
       w(0)=1._rk/3._rk
       w(N)=1._rk/3._rk
    Case('trapezi')
       w=1._rk
       w(0)=0.5_rk                                           
    Case default
       print *, 'Sorry, this method has not been implemented yet.'
    End Select
    integr=0._rk
    Do p=0,N
       integr=integr+y(p)*w(p)
    end do
    !Oppure integrate=dot_product(w,y)       prodotto scalare
    !Oppure integrate=sum(w*y)               somma delle coordinate w(i)*y(i) di w*y
    
    integr=integr*Delta
    stat=0

  End function integrate

!*********************************************************************************************************************************************
   Recursive Function int_fun(fun,a,b,fa,fb,eps,min_steps,max_steps,steps_,Ifun) Result(stat)
    
    Implicit None
    Procedure(fun_R_R) :: fun
    Real(rk), Intent(In) :: a,b,fa,fb,eps
    Integer(4), Intent(In) :: min_steps,max_steps
    Integer(4), Intent(Out) :: steps_
    Real(rk), Intent(Out) :: Ifun
    Integer(4) :: stat

    Integer(4), Save :: steps=1
    Real(rk), Save :: a0,b0
    Real(rk) :: h,c,fc,S_I,S_II,Ifun_I,Ifun_II

    If (steps==1) Then                                    !Inizializzazione con assegnazione degli estremi 
       a0=a
       b0=b
    Endif
    h=b-a                                                 !Salviamo la distanza
    c=0.5_rk*(a+b)                                        !Il punto medio
    S_I=0.5_rk*h*(fa+fb)                                  !Trapezi 2 punti
    fc=fun(c)                                             !valore f in punto medio
    S_II=0.5_rk*S_I+0.5_rk*h*fc                           !Trapezi 3 punti
    
    If ((Abs(S_II-S_I)<=3._rk*eps*Abs(S_II)).And.(steps>=min_steps)) Then 
       Ifun=S_II                                          !Se c'è la precisione richiesta salva e stat=0
       stat=0
    Else
       steps=steps+2                                      
       If (steps>max_steps) Then                          !Controllo sul numero di step
          Ifun=0._rk
          stat=1
       Else                                               !chiamata iterativa ai due intervalli dx e sx
          stat=Min(1,int_fun(fun,a,c,fa,fc,eps,min_steps,max_steps,steps_,Ifun_I)&
               +int_fun(fun,c,b,fc,fb,eps,min_steps,max_steps,steps_,Ifun_II))
          If (stat==0) Ifun=Ifun_I+Ifun_II
       End If
    Endif
    
    If (a==a0.And.b==b0) Then                             !Il calcolo non è neanche iniziato 
       steps_=steps
       steps=1
    Endif
    
  End Function int_fun

!*********************************************************************************************************************************************
!*********************************************************************************************************************************************
!*********************************************************************************************************************************************
!*********************************************************************************************************************************************
  
End Module LibraryDer
