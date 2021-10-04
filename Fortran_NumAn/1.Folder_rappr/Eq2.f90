Program eq2                                   !Nome e inizio programma

  Implicit None                               !non accetta dim implicite???
  Integer, Parameter :: rk=8                  !def costante !._rk def il tipo di reale  
  Real(rk) :: a,b,c                         
  Real(rk) :: x1_1,x2_1,x1_2,x2_2,x1_3,x2_3 
  Integer :: n                                !(4) defoult
  Real(rk) :: Delta,q                        

  a=1._rk                                     !Per dichiarazione sicura._rk 
  b=1._rk

  Print *,'a= ',a,' b= ',b                   
  Print '(2(A,E28.20E3))',' a= ',a,' b= ',b   !Stampa approssimata di var
                                              !2(2 volte),A(stringa),E...(var)
  Open(1,file='eq2.dat')                      !Creazione file.dat

  Do n=1,1000,1                               !,1 è il passo, ora sottointeso  !Iterazione
    c=10._rk**(-n)

    Delta=b**2-4._rk*a*c                     

    x1_1=(-b+Sqrt(Delta))/(2._rk*a)           !Sqrt è la radice
    x2_1=(-b-Sqrt(Delta))/(2._rk*a)

    x1_2=(2._rk*c)/(-b-Sqrt(Delta))         
    x2_2=(2._rk*c)/(-b+Sqrt(Delta))

    q=-0.5_rk*(b+Sign(Sqrt(Delta),b))         !Sign(a,b)= a con segno di b
    x1_3=c/q                                 
    x2_3=q/a
                                              !Scrittura su file.dat          
    Write(1,'(I6,7(x,E28.20E3))') n,c,x1_1,x2_1,x1_2,x2_2,x1_3,x2_3
                                              !Scrittura su terminale, analogo print
    Write(*,'(I6,7(x,E28.20E3))') n,c,x1_1,x2_1,x1_2,x2_2,x1_3,x2_3
    !Print '(I6,7(x,E28.20E3))',n,c,x1_1,x2_1,x1_2,x2_2,x1_3,x2_3    

    Read(*,*)                                 !Prende valore da video
  End Do

  Close(1)                                    !Chiusura file  

End Program eq2
