Module LibraryOde

  Use LibraryZero
  
Contains
!*********************************************************************************************************************************************
  Function euler (data) result (stat)                          !Preferibilmente predictor
    Implicit None
    Type(ode_data):: data 
    Integer(4):: stat
    
    data%y=data%y0+data%dx*data%fun(data%y0,data%x0)
    stat=0
    
  End Function euler
  
!*********************************************************************************************************************************************
   Function Picard (data) result (stat)                        !Corrector I2
    Implicit None
    Type(ode_data):: data 
    Integer(4):: stat

    data%y=data%y0+0.5_rk*data%dx*(data%fun(data%y0,data%x0)+data%fun(data%y,data%x0+data%dx))
    stat=0
    
  End Function picard

!*********************************************************************************************************************************************
   Function Taylor (data) result (stat)                        !All in one 
    Implicit None
    Type(ode_data):: data 
    Integer(4):: stat

    data%y=data%y0+data%dx*data%fun(data%y0,data%x0)+0.5_rk*(data%dx**2)*(data%dfun_t(data%y0,data%x0)&
        +matmul(data%dfun_y(data%y0,data%x0),data%fun(data%y0,data%x0)))
    stat=0
    
  End Function Taylor
  
!*********************************************************************************************************************************************
  Function IterPicard (data,para) result (stat)                !Corrector
    Implicit None
    Type(ode_data):: data
    Type(ode_para):: para
    Integer(4):: stat

    real(rk)::y_n(1:size(data%y)),y_o(1:size(data%y))

    y_n=data%y
    para%steps=0
    do while (any(abs(y_n-y_o)>para%eps).or.(para%steps==0))
       y_o=y_n
       para%steps=para%steps+1
       if (para%steps>para%max_steps) then
         stat=1
         return
       end if
       y_n=data%y0+0.5_rk*data%dx*(data%fun(data%y0,data%x0)+data%fun(y_o,data%x0+data%dx))
    end do
    data%y=y_n
    stat=0
    
  End Function IterPicard
  
!*********************************************************************************************************************************************
   Function  Runge_Kutta (data) result (stat)                  !All in one
    Implicit None
    Type(ode_data):: data
    Integer(4):: stat,i

    real(rk)::c(0:4,1:size(data%y)),a(1:4)=[1,2,2,1]

    c(0,:)=0
    do i=1,4
       c(i,:)=data%dx*data%fun(data%y0 + c(i-1,:)/a(i),data%x0 + data%dx/a(i))
    end do
    data%y=data%y0+matmul(a,c(1:,:))/6._rk
    
    !c(1,:)=data%dx*data%fun(data%y0,data%x0)
    !c(2,:)=data%dx*data%fun(data%y0 + 0.5_rk*c(1,:),data%x0 + 0.5_rk*data%dx)
    !c(3,:)=data%dx*data%fun(data%y0 + 0.5_rk*c(2,:),data%x0 + 0.5_rk*data%dx)
    !c(4,:)=data%dx*data%fun(data%y0 + c(3,:),data%x0 + data%dx)
    !data%y=data%y0+(c(1,:)+a(2)*c(2,:)+a(3)*c(3,:)+c(4,:))/6._rk
    
    stat=0
    
  End Function Runge_Kutta
  
!*********************************************************************************************************************************************
    Function shooting(Data,para) Result (stat)
  ! Compute u(x0->x1)[=data%u(1,x0->x1)] and du(x0->x1)[=data%u(2,x0->x1)]
  ! with the shooting method (with secant and Runge-Kutta)
  ! for the three cases below
  ! para%case = 'A' known  u(x0)[=y0(1)] e  u(x1)[=y1(1)]
  ! para%case = 'B' known  u(x0)[=y0(1)] e du(x1)[=y1(2)]
  ! para%case = 'C' known du(x0)[=y0(2)] e du(x1)[=y1(2)]
  ! where (x1>x0 and dx>0) or  (x1<x0 and dx<0)
  ! stat = 0 success
  ! stat = 1 no zero between ini-1000*dx and ini+1000*dx
  ! stat = 2 max_steps exceeded in secant
  ! Adolfo Avella
  ! ver:1.0 Salerno, 2013.05.13

    Implicit None
    Type(ode_data), Target :: Data
    Type(ode_para) :: para
    Integer(4) :: stat

    Real(rk) :: y0_(1:Size(Data%y0)),x0_
    Real(rk), Pointer :: var,com
    Real(rk) :: ini,exa,zero
    Integer(4) :: i,max_i

    max_i=Ceiling(Abs((Data%x1-Data%x0)/Data%dx))+1
    Allocate(Data%u(1:Size(Data%y0),1:max_i))

    y0_=Data%y0
    x0_=Data%x0

    Select Case(para%Case)
    Case('A')
       ini = Data%y0(2)
       var => Data%y0(2)
       exa = Data%y1(1)
       com => Data%y(1)
    Case('B')
       ini = Data%y0(2)
       var => Data%y0(2)
       exa = Data%y1(2)
       com => Data%y(2)
    Case('C')
       ini = Data%y0(1)
       var => Data%y0(1)
       exa = Data%y1(2)
       com => Data%y(2)
    End Select

    stat= fun_zero_bisezione(aux,ini,Data%dx,para%eps,para%eps,para%max_steps,zero,para%steps)
    If (stat==1) Then
       Print *,'No zero between:',ini-1000*data%dx,' and ',ini+1000*data%dx
       Return
    End If
    If (stat==2) Then
       Print *,'Exceeded max_steps in Secant'
       Return
    End If

    Data%y0=y0_
    Data%x0=x0_
    var=zero
    Data%u(:,1)=Data%y0
    Do i=2,max_i
       stat=Runge_Kutta(Data)
       Data%u(:,i)=Data%y
       Data%y0=Data%y
       Data%x0=Data%x0+Data%dx
    Enddo
    Data%y0=y0_
    Data%x0=x0_
    var=zero

  Contains

    Function aux(x)
      Implicit None
      Real(rk), Intent(in) :: x
      Real(rk) :: aux

      Data%y0=y0_
      Data%x0=x0_
      var=x       
      Do i=2,max_i
         stat=Runge_Kutta(Data)
         Data%y0=Data%y
         Data%x0=Data%x0+Data%dx
      Enddo
      aux=com-exa
    End Function aux

  End Function shooting
  
!*********************************************************************************************************************************************
!*********************************************************************************************************************************************
!*********************************************************************************************************************************************
  
End Module LibraryOde
