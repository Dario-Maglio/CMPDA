#include "fourvectorshared.h"
#include <iostream>
#include <math.h>

float FourVector::mass() {
  return sqrt(E_*E_ - (px_*px_ + py_*py_ + pz_*pz_));
}

float FourVector::pt() {
  return sqrt(px_*px_ + py_*py_ + pz_*pz_);
}

FourVector FourVector::operator+(const FourVector & other ) {
  return FourVector(px_ + other.px_, py_ + other.py_, pz_ + other.pz_, E_ + other.E_);
}

void Particle::print(){
  std::cout<<"Particle with mass "<<mass()<<" and charge "<<charge_<<std::endl;
}
