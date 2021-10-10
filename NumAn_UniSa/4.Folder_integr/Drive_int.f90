Program Drive_integr
  
  Use LibraryDer
  
  Implicit None
  Real(rk), Parameter::a=0._rk,b=pi
  Real(rk), Allocatable:: x(:), y(:)                    !Vettori di lunghezza variabile
  Real(rk) ::integr_s,integr_t
  Integer(rk) :: i,N

  open (1,file='Int.dat')
  Do N=2,10000,2
     Allocate(x(0:N),y(0:N))                            !Alloca spazio in memoria per array dinamici
     Forall (i=0: N) x(i)=a+i*(b-a)/N                   !Istruzione Do contratta
     y=Sin(x)
     if(integrate(x,y,integr_s,'simpson')/=0) stop  
     if(integrate(x,y,integr_t,'trapezi')/=0) stop
     print *,N,integr_s,integr_t, log10(abs(integr_t-2._rk)/2._rk), log10(abs(integr_s-2._rk)/2._rk)
     write(1,'(5(x,E19.12))') log10(real(N,rk)),integr_s,integr_t,&
          log10(abs(integr_t-2._rk)/2._rk), log10(abs(integr_s-2._rk)/2._rk)
     Deallocate (x,y)
  End do
  close(1)
  
End Program Drive_integr
