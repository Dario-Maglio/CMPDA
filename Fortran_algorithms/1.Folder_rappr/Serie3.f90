Program Serie3
 
 Implicit none
 integer(4), Parameter::c=100000,rk=8
 Integer(4)::i,N
 Real(rk)::Sum,a
 
 !Primo metodo: Somma da 1 a N
 print *, 'Primo metodo'
 Do N=c,c*10,c
    Sum=0
    Do i=1,N
     a=1._rk/i                
     Sum=Sum+a
    End do
    print *, 'Il valore assunto è ',Sum
 End do
 print *, ''
 
 !Secondo metodo: Somma da N a 1
 print *, 'Secondo metodo'
  Do N=c,c*10,c
     Sum=0
     Do i=N,1,-1
      a= 1._rk/i                
      Sum=Sum+a
     End do
     print *, 'Il valore assunto è ',Sum
  End do
  print *, ''
 
End Program Serie3
