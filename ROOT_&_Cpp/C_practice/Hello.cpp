#include <iostream>
#include "header.h"
#define MIN(a,b) ((a)<(b)?(a):(b))

/***
#--> direttive al preprocessore
MIN è una macro che funziona con ogni tipo di var
***/

void myf(int a, int *ap, int &ar){
  a += 1;
  (*ap)+= 1;
  ar += 1;
}

int main()
{
  float a = 0;
  float *ap = &a;
  float &ar = a; //Reference to a
  std::cout << a << *ap << ar <<std::endl;
  {
    //Scope più interno
    int a = 5; //Shadowing a
    std::cout << a << *ap << ar <<std::endl;
  }
  int c = 4;
  myf(a, ap, c);
  std::cout << a << *ap << c <<std::endl;
  std::cout <<"Min is: "<<MIN(50,20)<<std::endl;
}
