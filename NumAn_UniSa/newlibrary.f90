Module library
!!-----------------------------------------------------------------
!!-----------------------------------------------------------------
!!	General parameters and abstract interface
!!-----------------------------------------------------------------
!!-----------------------------------------------------------------

  Implicit None 
  Integer(4), Parameter :: rk=8
  Real(rk), Parameter :: pi=Acos(-1._rk)

  Abstract Interface                                        !Dichiarare come è fatta la funzione che verrà chiamata in una subroutine
     Function fun_R_R(x)                                    !Nome e variabili funzione
       Import :: rk                                         !Prende rk da sopra (necessario xk non è nel contains)
       Real(rk), Intent(in) :: x
       Real(rk) :: fun_R_R                                  !Anche nome della f è una variabile
     End Function fun_R_R
     Function fun_vR_RvR(y,x)
       import:: rk
       Real(rk), intent (in):: y(1:),x
       Real (rk)::fun_vR_RvR(1:size(y))
     end function fun_vR_RvR
     Function fun_mR_RvR (y,x)
       import:: rk
       Real(rk), intent (in):: y(1:),x
       Real (rk)::fun_mR_RvR(1:size(y),1:size(y))
     end function fun_mR_RvR
  End Interface

  Type::ode_data
     Real(rk), allocatable:: y0(:),y1(:),y(:),u(:,:)
     Real(rk)::x0,x1,dx
     Procedure(fun_vR_RvR), Nopass, pointer::fun            !Non passa alla funzione il tipo ode data come argomento
     Procedure(fun_vR_RvR), Nopass, pointer::dfun_t
     Procedure(fun_mR_RvR), Nopass, pointer::dfun_y  
  End Type ode_data

  Type::ode_para
     Real(rk)::eps
     integer(4)::steps,max_steps
     character(1)::Case
  end type ode_para

  Type :: matrix
     Real(rk), Allocatable :: A(:,:),At(:,:),iA(:,:),b(:),bt(:),x(:),Bm(:,:),Bmt(:,:)
     Integer(4), Allocatable :: v(:)
     Integer(4) :: p
     Real(rk) :: detA,TrA,lambda
  End Type matrix

  Type :: matrix_para
     Real(rk) :: eps_x,eps_lambda
     Integer(4) :: steps,max_steps
  End Type matrix_para

Contains                                                    !Introduce le procedure della libreria o del sottoprogramma
  							    !subroutine: funzione il cui return è un void
							    !funzione: restituisce qualcosa che è veriabile con nome della funzione
 							    !subroutine si chiama, f si assegna
 							    !con f si può restituire anche lo stato della funzione: 0 successo, altro numero errore
!!-----------------------------------------------------------------
!!-----------------------------------------------------------------
!!	Interpolation, derivation and integration algorithms
!!-----------------------------------------------------------------
!!-----------------------------------------------------------------
!******************************************************************
  Subroutine interp(x,y,x0,y0,method)
  !!input: vettori dati e puntatori a x0, y0 in cui si desidera ottenere l'interpolazione
  !!optional: method_ può essere lagrange, aitken o updown
    Implicit None
    Real(rk), Intent(In) :: x(:), y(:), x0                  !def come variabili in input con Intent(in) warning se modificate
    Character(6), optional :: method
    Real(rk), Intent(Out) :: y0                             !qui analogamente warning se non viene assegnata y0 alla fine
    
    If (present(method)) Then                               !definizione di argomento opzionale
    	Select Case(trim(method))                           !Invece di un if annidato (è meglio così)
   	 Case('lagran')                                     !Trim taglia spazi vuoti in stringhe
   	   Call interp_lagrange(x,y,x0,y0)
   	 Case('aitken')
    	   Call interp_aitken(x,y,x0,y0)
         Case('updown')
   	   Call interp_updown(x,y,x0,y0)
   	 Case Default
    	   Print *,'Sorry, this method had not been implemented yet!'
    	End Select
    Else
    	Call interp_aitken(x,y,x0,y0)
    End If
  End Subroutine interp
  
!******************************************************************
  Subroutine interp_lagrange(x,y,x0,y0)
    Implicit None
    Real(rk), Intent(In) :: x(:), y(:), x0
    Real(rk), Intent(Out) :: y0

    Integer(4) :: l, m, N
    Real(rk) :: prod

    N=Size(x)                                      !Size prende la misura dell'array
    If (Size(x)/=Size(y)) Then
       Print *,'Size x is different from Size y!'
       Stop                                        !Ferma il programma
    End If
    Do l=1,N
       If (x(l)==x0) Then
          y0=y(l)
          Return                                   !Ferma l'esecuzione del sottoprogramma
       End If
    End Do

    y0=0._rk
    Do l=1,N
       prod=1._rk
       Do m=1,N
          If(m==l) Cycle                           !Salta il passo del ciclo 
          prod=prod*(x0-x(m))/(x(l)-x(m))
       End Do
       y0=y0+prod*y(l)
    End Do
  End Subroutine interp_lagrange

!******************************************************************
  Subroutine interp_aitken(x,y,x0,y0)
    Implicit None
    Real(rk), Intent(In) :: x(:), y(:), x0
    Real(rk), Intent(Out) :: y0

    Integer(4) :: k, i, N
    Real(Rk) :: y_(1:Size(x))

    N=Size(x)
    If (Size(x)/=Size(y)) Then
       Print *,'Size x is different from Size y!'
       Stop
    End If
    Do k=1,N
       If (x(k)==x0) Then
          y0=y(k)
          Return 
       End If
    End Do

    y_=y
    Do k=1,N-1
       Do i=1,N-k
          y_(i)=(x0-x(i+k))/((x(i)-x(i+k)))*y_(i)+(x0-x(i))/((x(i+k)-x(i)))*y_(i+1)
       End Do
    End Do
    y0=y_(1)
  End Subroutine interp_aitken

!******************************************************************
  Function nearest_i(x,xs)
    ! Search the closest point x(i) to xs and return i, i = 1...N
    ! Adolfo Avella
    ! ver:1.0 Salerno, 2013.04.07
    
    Implicit None
    Integer(4) :: nearest_i
    Real(rk), Intent(In) :: x(:),xs

    nearest_i = Minloc(Abs(x-xs),1)

  End Function nearest_i

  Subroutine interp_updown(x,y,x0,y0)
    ! Search the closest point x(i) to xs and return i, i = 1...N
    ! Adolfo Avella
    ! ver:1.0 Salerno, 2013.04.07
    Implicit None
    Real(rk), Intent(In) :: x(:), y(:), x0
    Real(rk), Intent(Out) :: y0

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
  End Subroutine interp_updown

!******************************************************************
!!-----------------------------------------------------------------
!******************************************************************
  Function Der(x,y,l,dy,o_,m_,e_) result (stat)          !result dichiara la var da utilizzare al posto del nome della funzione
    !!input: vettori dati, l indice di x0 in cui calcolare la derivata, dy puntatore al risultato in x0
    !!opzionali: o=1,2 ordine della derivata, m=1,2,3 rispettivamente per la derivata a 3,5,7 punti, e punti per estrapolazione ai bordi
    !stat=0 successo
    !stat=1 Size(x)/=Size(y)
    !stat=2 l<0 or l>N
    !stat=3 o<1 or o>2                                
    !stat=4 m<1 or m>3

    Implicit none
    real(rk), Intent (In):: x(0:), y(0:)
    integer(4), Intent (In) :: l
    real(rk), Intent (Out):: dy
    integer(4), optional :: o_,m_,e_
    integer(4) :: o=1, m=2, e = 10                                              
    integer(4):: stat
    
    integer(4)::k,N
    real(rk):: xm,xp,ym,yp,bn(1:3,1:3)=0                 !bn: matrice dei coefficienti della comb lin, p: plus, m: minus
    if(present(o_)) o = o_
    if(present(m_)) m = m_
    if(present(e_)) e = e_

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
  
!******************************************************************
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
  

 
End Module library 
