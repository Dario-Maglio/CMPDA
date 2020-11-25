#ifndef FILE_H2
#define FILE_H2
#include <math.h>
#include <iostream>
#include "fourvectortampletes.h"

template <class type>
class TwoBodiesDecayedParticle : public Particle<type> {

public:
  TwoBodiesDecayedParticle(const Particle<type> & p4, const Particle<type> & k4):
     First_(p4), Second_(k4) {}

private:
  Particle<type> First_;
  Particle<type> Second_;
};

#endif
