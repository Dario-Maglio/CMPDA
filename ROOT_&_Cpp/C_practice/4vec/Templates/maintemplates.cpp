#include <iostream>
#include "fourvectortampletes.h"
#include "twoparticles.h"

int main() {
  FourVector<double> v1(32., 40., 30., 500.);
  FourVector<float> v2(24., 47., 60., 600.);
  std::cout<<"V2 y momentum :"<< v2.get_py() <<std::endl;
  v2.set_py(42);
  std::cout<<"V2 y momentum :"<< v2.get_py() <<std::endl;
  v2 = v2 * 4;
  std::cout<<"V2 y momentum :"<< v2.get_py() <<std::endl;
  std::cout<<"Total momentum: "<<(v1+v2).pt()<<std::endl;
  std::cout<<"Mass: "<<(v1+v2).mass()<<std::endl;
  Particle<double> electron("electron", -1, v1);
  Particle<double> positron("positron", +1, v2);
  positron.set_py(32);
  std::cout<<positron.get_name()<<" y momentum:"<<positron.get_py()<<std::endl;
  electron.print();
  positron.print();
};
