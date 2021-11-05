Program Drive

  use flibrary

  Implicit none
  Real(8) :: x = -0.85, y = -0.85, x_, y_, delta, alpha=0.1
  Integer(4) :: i,j
  Integer(4), parameter :: N=10, M=10000

  delta = abs(2*x)/N
  Open(1, file='punti.dat')

  Do j=1, 4
    Do while (x < 0.9)
      Do while (y < 0.9)
        Write(1,*) x, y, alpha
        x_ = x
        y_ = y
        Do i=0, M
          Call update(x_,y_, alpha)
          Write(1,*) x_, y_, alpha
        End do
        y = y + delta
      End do
      y = -0.85
      x = x + delta
    End do
    x = -0.85
    alpha = alpha + j*0.1
  End do

  Close(1)

Contains

  Subroutine update(x,y,alpha)
    Implicit none
    Real(8) :: x, x_, y, delta, alpha
    x_= x
    x = x*cos(alpha) - (y - x**2)*sin(alpha)
    y = x_*sin(alpha) + (y - x_**2)*cos(alpha)
  End subroutine update

End program Drive
