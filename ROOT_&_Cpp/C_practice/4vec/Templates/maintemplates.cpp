#include <iostream>
#include "fourvectortampletes.h"

int main() {
  FourVector<double> v1(32., 40., 30., 500.);
  FourVector<double> v2(24., 47., 60., 600.);
  std::cout<<"V2 y momentum :"<< v2.get_py() <<std::endl;
  std::cout<<"Total momentum: "<<(v1+v2).pt()<<std::endl;
  std::cout<<"Mass: "<<(v1+v2).mass()<<std::endl;
  Particle<double> electron(-1, v1);
  Particle<double> positron(+1, v2);
  electron.print();
  positron.print();
};
