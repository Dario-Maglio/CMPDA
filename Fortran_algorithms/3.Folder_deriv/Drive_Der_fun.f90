Program drive_der_fun

  Use LibraryDer
  
  Implicit None
  Integer(4), Parameter :: N=100
  Real(rk) :: x(0:N), dy1, dy2, dy3, dy4, ddy1, ddy2, ddy3, ddy4
  Integer(4) :: i, o, sd1, sd2, sd3, sd4, sdd1, sdd2, sdd3, sdd4
  !h_ini è la distanza iniziale tra i punti del calcolo
  
  Do i= 0,N
     x(i)= i*(3*pi)/N 
  End do

  Open(1,file='Der_fun.dat')
  Do i=0,N
     o=1
     If (Der_fun(fun,x(i),o,1._rk,1.E-3_rk,1000,sd1,dy1)/=0) Stop 'Error in o=1 h_ini=1 eps=1E-3!!!'         
     If (Der_fun(fun,x(i),o,1._rk,1.E-6_rk,1000,sd2,dy2)/=0) Stop 'Error in o=1 h_ini=1 eps=1E-6!!!'
     If (Der_fun(fun,x(i),o,0.01_rk,1.E-3_rk,1000,sd3,dy3)/=0) Stop 'Error in o=1 h_ini=0.01 eps=1E-3!!!'
     If (Der_fun(fun,x(i),o,0.01_rk,1.E-6_rk,1000,sd4,dy4)/=0) Stop 'Error in o=1 h_ini=0.01 eps=1E-6!!!'
     o = 2
     If (Der_fun(fun,x(i),o,1._rk,1.E-3_rk,1000,sd1,ddy1)/=0) Stop 'Error in o=2 h_ini=1 eps=1E-3!!!'
     If (Der_fun(fun,x(i),o,1._rk,1.E-6_rk,1000,sd2,ddy2)/=0) Stop 'Error in o=2 h_ini=1 eps=1E-6!!!'
     If (Der_fun(fun,x(i),o,0.01_rk,1.E-3_rk,1000,sd3,ddy3)/=0) Stop 'Error in o=3 h_ini=0.01 eps=1E-3!!!'
     If (Der_fun(fun,x(i),o,0.01_rk,1.E-6_rk,1000,sd4,ddy4)/=0) Stop 'Error in o=3 h_ini=0.01 eps=1E-6!!!'

     Write(1,'(I4,11(x,E23.16),8(x,I4))') i,x(i),dy1,dy2,dy3,dy4,cos(x(i)),ddy1,ddy2,ddy3,ddy4,-Sin(x(i)),&
          sd1,sd2,sd3,sd4,sdd1,sdd2,sdd3,sdd4
     Write(*,'(I4,11(x,E23.16),8(x,I4))') i,x(i),dy1,dy2,dy3,dy4,cos(x(i)),ddy1,ddy2,ddy3,ddy4,-Sin(x(i)),&
          sd1,sd2,sd3,sd4,sdd1,sdd2,sdd3,sdd4

   End do
   Close (1)

   Contains

     Function fun(x)
       Implicit None
       Real(rk), Intent(In) :: x
       Real(rk) :: fun
       fun=Sin(x)
     End Function fun
     
End program drive_der_fun
