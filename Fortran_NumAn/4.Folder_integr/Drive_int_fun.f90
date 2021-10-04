Program drive_int_fun

  Use LibraryDer

  Implicit None
  Integer(4) :: steps
  Real(rk) :: Ifun1,Ifun2,Ifun3,Ifun4,Ifun5,Ifun6,Ifun7,Ifun8,p
          
  If (int_fun(fun,0._rk,pi,fun(0._rk),fun(pi),1.E-6_rk,10,10000,steps,Ifun4)/=0) Then
     Stop 'Error in trapezoid min_steps=10, max_steps=10000, eps=1.E-6!!!'      
  Endif
  Write(*,'(1A,1F15.12,1A,1E8.1,1A,I5)') 'Trapezoid min_steps=10, max_steps=10000, eps=1.E-6= ',&
       Ifun4,'; rel.err.= ',Abs(Ifun4-2)/2,'; steps= ',steps  

Contains

  Function fun(x)
    Implicit None
    Real(rk), Intent(in) :: x
    Real(rk) :: fun
    fun=Sin(x)
  End Function fun

End Program drive_int_fun
