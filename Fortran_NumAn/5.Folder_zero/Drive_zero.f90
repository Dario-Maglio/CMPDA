Program Drive_zero
  
  Use LibraryZero
  
  Implicit None
  Real(rk), Parameter::epsx=1.E-12_rk,epsy=1.E-10_rk
  Real(rk) ::a=1_rk, passo=0.2_rk, x0
  Integer(4) ::max_step=100,steps

  If (fun_zero_bisezione(fun,a,passo,epsx,epsy,max_step,x0,steps)/=0) Then
     Stop 'Errore nella ricerca degli zeri'      
  Endif
  Write(*,'(1A,1F15.12,1A,I3)') 'x0= ',x0,'; steps= ',steps
  Read(*,*)
  
  If (fun_zero_newton(fun,dfun,a,epsy,max_step,x0,steps)/=0) Then
     Stop 'Errore nella ricerca degli zeri'      
  Endif
  Write(*,'(1A,1F15.12,1A,I3)') 'x0= ',x0,'; steps= ',steps
  Read(*,*)
  
  If (fun_zero_secante(fun,a,passo,epsx,epsy,max_step,x0,steps)/=0) Then
     Stop 'Errore nella ricerca degli zeri'      
  Endif
  Write(*,'(1A,1F15.12,1A,I3)') 'x0= ',x0,'; steps= ',steps

Contains

  Function fun(x)
    Implicit None
    Real(rk), Intent(in) :: x
    Real(rk) :: fun
    fun=x**(-7) - 2*(x**(-13))
  End Function fun

  Function dfun(x)
    Implicit None
    Real(rk), Intent(in) :: x
    Real(rk) :: dfun
    dfun=2*13*(1/x**14)-7*(1/x**8)
  End Function dfun

End Program Drive_zero
