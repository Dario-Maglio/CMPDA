Module LibraryZero

  Use Library
  
Contains
!*********************************************************************************************************************************************
 Function braket(fun,x,dx,a,b) Result (stat)

    Implicit None
    Procedure(fun_R_R) :: fun
    Real(rk), Intent(In) :: x,dx
    Real(rk), Intent(Out) :: a,b
    Integer(4) :: stat

    Real(rk) :: a0,b0

    a0=x-dx
    b0=x+dx
    a=x-100*dx
    b=x+100*dx
    
    Do While (a0>=a.And.b0<=b)                         !Finché non si esce fuori dall'intervallo massimo di ricerca (ampio 200*dx)
       If (fun(a0)*fun(b0)<0) Then                     !f(a)*f(b)>0
          if (fun(b0)*fun(b0-dx)<0) then               !Se le zero è a destra salva gli estremi in a b
             a=b0-dx
             b=b0
          else                                         !Rispettivamente se è a sinistra
             a=a0
             b=a0+dx
          end if
          stat=0
          Return
       End if
       a0=a0-dx
       b0=b0+dx
    End do
    stat=1                                             !Se ci arriva non ha trovato zeri
  End Function braket

!*********************************************************************************************************************************************
 Function fun_zero_bisezione(fun,x,dx,epsx,epsy,max_steps,x0,steps) Result (stat)

  Implicit None
  Procedure(fun_R_R) :: fun
  Real(rk), Intent(In) :: x,dx,epsx,epsy
  Integer(4), Intent(In) ::max_steps
  Integer(4), Intent(Out) :: steps
  Real(rk), Intent(Out):: x0
  Integer(4) :: stat

  Real(rk):: a,b,c

  if (braket(fun,x,dx,a,b)/=0) then                     !Ricerca estremi ed intermedio
     stat=1
     return
  end if
  steps=1
  c=0.5_rk*(a+b)
  
  Do while (abs(fun(c))>epsy)
     if ((b-a)<epsx) then
        stat=2
        return
     end if
     steps=steps+1
     if (steps>max_steps) then
        stat=3
        return
     end if
     if (fun(a)*fun(c)<0) then
        b=c
     else
        a=c
     end if
     c=0.5_rk*(a+b)
     print *, a,c,b
  End do

  stat=0
  x0=c
  
 End Function fun_zero_bisezione

!*********************************************************************************************************************************************
 Function fun_zero_newton(fun,dfun,x1,epsy,max_steps,x0,steps) Result (stat)

  Implicit None
  Procedure(fun_R_R) :: fun,dfun
  Real(rk), Intent(In) :: x1,epsy
  Integer(4), Intent(In) ::max_steps
  Integer(4), Intent(Out) :: steps
  Real(rk), Intent(Out):: x0
  Integer(4) :: stat

  Real(rk):: x2

  x2=x1
  steps=0
  
  Do while (abs(fun(x2))>epsy)
     if (abs(dfun(x2)) < 1.E-12_rk) then
      stat=1
      return
     end if
     x2=x2 - fun(x2)/dfun(x2)
     steps=steps+1
     print *, x2
     if (steps>max_steps) then
        stat=1
        return
     end if
  End Do

  stat=0
  x0=x2
  
End Function fun_zero_newton

!*********************************************************************************************************************************************
 Function fun_zero_secante(fun,x,dx,epsx,epsy,max_steps,x0,steps) Result (stat)

  Implicit None
  Procedure(fun_R_R) :: fun
  Real(rk), Intent(In) :: x,dx,epsx,epsy
  Integer(4), Intent(In) ::max_steps
  Integer(4), Intent(Out) :: steps
  Real(rk), Intent(Out):: x0
  Integer(4) :: stat

  Real(rk):: x1,x2,x3

  if (braket(fun,x,dx,x1,x2)/=0) then                !x1 e x2 diventano gli estremi dell'intervallo
     stat=1
     return
  end if
  steps=0

  Do while (abs(fun(x2))>epsy)
     if (abs(fun(x2)-fun(x1))< 1.E-12_rk) then        !Si azzera denominatore nel calcolo
        stat=2
        return
     end if
     x3=x2-fun(x2)/((fun(x2)-fun(x1))/(x2-x1))
     print *, x1,x2,x3
     x1=x2
     x2=x3
     steps=steps+1
     if (steps>max_steps) then
        stat=2
        return
     end if
  End do

  stat=0
  x0=x2
  
End Function fun_zero_secante

!*********************************************************************************************************************************************
!*********************************************************************************************************************************************
!*********************************************************************************************************************************************
!*********************************************************************************************************************************************
  
End Module LibraryZero
