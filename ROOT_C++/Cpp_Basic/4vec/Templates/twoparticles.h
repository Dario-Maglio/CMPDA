#ifndef FILE_H2
#define FILE_H2
#include <math.h>
#include <iostream>
#include "fourvectortampletes.h"

template <class type>
class DecayedParticle : public Particle<type> {
public:
  DecayedParticle(const Particle<type> &p4, const Particle<type> &k4):
     first_(p4), second_(k4), Particle<type>("Decayed particle",
            p4.get_charge() + k4.get_charge(), p4.get_vect() + k4.get_vect()) {}

  Particle<type> getFirst() const {return first_;}
  Particle<type> getSecond() const {return second_;}

  void printDetails() {
    std::cout<<"\nThis is a decayd particle with the following features:\n";
    Particle<type>::print();
    std::cout<<"The features of the products are the following:\n";
    first_.print();
    second_.print();
  }

private:
  Particle<type> first_;
  Particle<type> second_;
};

#endif
