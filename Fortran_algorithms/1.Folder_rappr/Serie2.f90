Program Serie2
 
 Implicit none
 integer(4), Parameter::c=100000,rk=8 
 Integer(4)::i,N
 Real(rk)::Sum,Sot,a
 
 !Primo metodo: Somma della serie così com'è
 print *, 'Primo metodo'
 Do N=c,c*10,c
    Sum=0
    Do i=1,2*N
     a=((-1._rk)**i)*(i/(i+1._rk))                
     Sum=Sum+a
    End do
    print *, 'Il valore assunto è ',Sum
 End do
 print *, ''
 
 !Secondo metodo: Divisione in 2 sottoserie
 print *, 'Secondo metodo'
 Do N=c,c*10,c
    Sum=0
    Sot=0
    Do i=1,N
     a= 2._rk*i/(2._rk*i+1._rk)                
     Sum=Sum+a
     a=(2._rk*i-1._rk)/(2._rk*i)
     Sot=Sot+a
    End do
    print *, 'Il valore assunto è ',(Sum-Sot)
 End do
 print *, ''
 
 !Terzo metodo: Ricompomposizione delle due sottoserie
 print *, 'Terzo metodo'
  Do N=c,c*10,c
     Sum=0
     Sot=0
     Do i=1,N
      a= 1._rk/((2._rk*i)*(2._rk*i+1._rk))                
      Sum=Sum+a
     End do
     print *, 'Il valore assunto è ',Sum
  End do
  print *, ''
 
End Program Serie2
