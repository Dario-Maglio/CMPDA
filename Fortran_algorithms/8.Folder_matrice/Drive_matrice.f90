Program drive_matrix
  !Per cambiare le dim di A basta cambiare n e il formato di stampa per ogni print
  
  Use LibraryMatr

  Implicit None
  integer(4), parameter:: n=6
  Type(matrix) :: Data
  integer(4)::i

  Allocate(data%A(1:n,1:n))
  data%A=Reshape([1,2,3,4,5,7,6,8,9,10,9,13,12,14,15,16,17,19,18,20,21,22,23,25,24,26,27,28,29,31,30,32,33,34,36,35],[6,6])     !Reshape riempie prima le righe di una colonna (Nel caso di un tensore scorre gli indici da sinistra)
  Allocate(data%b(1:n))
  data%b=[1,2,3,4,5,6]
    
  Print *,''
  Print *,'            A'
  Do i=1,n
     Print '(6(x,E13.6))',data%A(i,:)
  End do
  Print *,'-----------------------------------'
  Print *,'-----------------------------------'
  Print *,''
  
  Print '(x,A,I1)','stat tridiagsup = ',tridiagsup(Data)
  Print *,'       A tri-diag-sup (v ordered)'
  Do i=1,n
     Print '(6(x,E13.6))',data%At(data%v(i),:)
  End do
  Print *,''
  Print '(x,A,6(x,I1))','v= ',data%v
  Print *,'-----------------------------------'
  Print *,'-----------------------------------'
  Print *,''

  Print '(x,A,I1)','stat det = ',det(Data)
  Print '(x,A,x,E13.6)','det A= ',data%detA
  Print *,'-----------------------------------'
  Print *,'-----------------------------------'
  Print *,''

  Print '(x,A,I1)','stat linsys = ',linsys(Data)
  Print *,'             A * x = b'
  Do i=1,n
     Print '(x,A,6(x,E13.6),x,A,(x,E13.6),x,A,(x,E13.6),x,A)','(',data%A(i,:),') (',data%x(i),') (',data%b(i),')'
  End do
  Print *,''
  Print *,'check A * x - b = 0'
  Do i=1,n
     Print '(1(x,E13.6))',Dot_product(data%A(i,:),data%x)-data%b(i)
  End do
  Print *,'-----------------------------------'
  Print *,'-----------------------------------'
  Print *,''

  Print '(x,A,I1)','stat inv = ',inv(Data)
  Print *,'             inv A'
  Do i=1,n
     Print '(6(x,E13.6))',data%iA(i,:)
  End do
  Print *,''
  Print *,'check A * inv A = I'
  Do i=1,n
     Print '(6(x,E13.6))',Matmul(data%A(i,:),data%iA)
  End do
  Print *,'-----------------------------------'
  Print *,'-----------------------------------'

End Program drive_matrix
