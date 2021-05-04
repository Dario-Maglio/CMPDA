Module LibraryInterp

  Use library
  
Contains                                                    !Procedure della libreria (può stare anche in un sottoprogramma)
  !subroutine: funzione il cui return è un void
  !funzione: restituisce qualcosa che è veriabile con nome della funzione
  !subroutine si chiama, f si assegna
  !con f si può restituire anche lo stato della funzione: 0 successo, altro numero errore
!*********************************************************************************************************************************************
  Subroutine interp(x,y,x0,y0,method)
    Implicit None
    Real(rk), Intent(In) :: x(:), y(:), x0                  !def come variabili in input con Intent(in)
    Character(Len=*), Intent(In) :: method                  !warning se vengono modificate
    Real(rk), Intent(Out) :: y0                             !def come variabili in output
                                                            !warning se non viene assegnata y0 a fine esecuzione
                                                            !definendo con in/out o non definendo, non avviene nessun controllo sulle var
 
    Select Case(Trim(method))                               !Invece di un if annidato (è meglio così)!Trim taglia spazi vuoti in stringhe
    Case('lagrange')                                        
       Call interp_lagrange(x,y,x0,y0)
    Case('aitken')
       Call interp_aitken(x,y,x0,y0)
    Case('updown')
       Call interp_updown(x,y,x0,y0)
    Case Default
       Print *,'Sorry, this method had not been implemented yet!'
    End Select
  End Subroutine interp
  
!*********************************************************************************************************************************************
  Subroutine interp_lagrange(x,y,x0,y0)
    Implicit None
    Real(rk), Intent(In) :: x(:), y(:), x0
    Real(rk), Intent(Out) :: y0
    !Fine interfaccia del sottoprogramma. Def interfaccia: tutto ciò che deve sapere chi usa la sub
    
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
          If(m==l) Cycle                          !Salta il passo del ciclo 
          prod=prod*(x0-x(m))/(x(l)-x(m))
       End Do
       y0=y0+prod*y(l)
    End Do
  End Subroutine interp_lagrange

!*********************************************************************************************************************************************
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

!*********************************************************************************************************************************************
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
  
!*********************************************************************************************************************************************
End Module LibraryInterp
