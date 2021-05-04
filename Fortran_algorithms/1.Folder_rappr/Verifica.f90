Program Verifica
 
 Implicit none
 Real(8)::R=1,G=1
 Integer(8)::I,N
 
 do N=1,1500
    R=R/2                           !Huge(R) < 2 alla 128
    print *,N,G+R, R
 end do
 print *, ' '

 print *, 'Massimo numero reale rappresentabile'
 print *, Huge(R)
 print *, 'Minimo numero reale rappresentabile (in modulo)'
 print *, Tiny(R)
 print *, 'Epsilon'
 print *, Epsilon(R)
 print *, 'Cifre significative del numero reale'
 print *, Precision(R)
 print *, 'Massimo numero naturale rappresentabile'
 print *, Huge(I)
 print *, ' '
 
End Program Verifica
