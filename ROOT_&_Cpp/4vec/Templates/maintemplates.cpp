#include <iostream>
#include "fourvectortampletes.h"
#include "twoparticles.h"

int main() {
  FourVector<double> v1(3., 5., 3., 500.);
  FourVector<double> v2(2., 4., 6., 600.);

  std::cout<<"\nTests for the setter, scalar and sum operator\n";
  std::cout<<"V2 y momentum :"<< v2.get_py() <<std::endl;
  v2.set_py(2.);
  std::cout<<"V2 y momentum :"<< v2.get_py() <<std::endl;
  v2 = v2 * 3.;
  std::cout<<"V2 y momentum :"<< v2.get_py() <<std::endl;
  std::cout<<"Sum total momentum: "<<(v1 + v2).pt()<<std::endl;
  std::cout<<"Sum mass: "<<(v1 + v2).mass()<<std::endl;

  std::cout<<"\nTests for the cast operator and sum between different types\n";
  FourVector<float> v3 = v2;
  std::cout<<"V3 tot momentum: "<<(v1 + v3).pt()<<std::endl;

  std::cout<<"\nParticle class tests\n";
  Particle<double> electron("electron", -1, v1);
  Particle<float> positron("positron", +1, v2);
  positron.set_py(3.);
  std::cout<<positron.get_name()<<" y momentum:"<<positron.get_py()<<std::endl;
  std::cout<<positron.get_name()<<" mass:"<<positron.mass()<<std::endl;
  electron.print();
  positron.print();
  Particle<float> decayed = electron + positron;
  std::cout<<decayed.get_name()<<" y momentum:"<<positron.get_py()<<std::endl;
  decayed.print();

  std::cout<<"\nThis try to make the sum between different class instances\n";
  std::cout<<"Sum mass: "<<(v1 + positron).mass()<<std::endl;

  std::cout<<"\nTests on the original particle\n";
  DecayedParticle<double> original(electron, positron);
  original.print();
  original.getFirst().print();
  original.printDetails();
};
