Program Expo
 
 Implicit none
 Real(8)::Sum,a,x
 Integer(4)::i,Fact
 x=10                              

 !Primo metodo: utilizzo del fattoriale
 Fact=1
 Sum=1
 Do i=1,100
    Fact=Fact*i
    print *,i,Fact                !Si osserva che a 16 x=10 Fact è già pazzo
    a=(-x)**i/Fact
    Sum=Sum+a
    if (Fact==0) exit             !Aggiunto per non perd tempo !exit dal ciclo
    if (abs(a/sum)<1.E-8_8) exit  !abs valore assoluto 
                                  !1.E exp in real 4 o modificabile_8
                                  !1.D exp in real 8
 End do
 print *,''
 print *, Sum, exp(-x)            !exp(x)= e alla x
 print *,''

 !Secondo metodo: somma alternata
 Sum=1
 a=1
 Do i=1,100
    a=a*(-x)/i                   !Differenza catastrofica
    Sum=Sum+a
    print *,i,a,Sum
    if (abs(a/sum)<1.D-15) exit  !Richiedo la precisione a -8 e va
                                 !Ma non và a -15 e x=10
 End do                         
 print *,''
 print *, Sum, exp(-x)
 print *,''

 !Terzo metodo: somme e reciproco
 Sum=1
 a=1
 Do i=1,100
    a=a*x/i
    Sum=Sum+a
    print *,i,a,Sum
    if (abs(a/Sum)<1.D-15) exit  !Va bene pure a 15
 End do
 print *,''
 print *, 1.D0/Sum, exp(-x)
 print *,''
 
End Program Expo
