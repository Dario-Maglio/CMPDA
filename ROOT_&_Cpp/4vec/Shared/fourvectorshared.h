#ifndef FILE_H
#define FILE_H
#include <math.h>

class FourVector {
public:
  FourVector() {}
  FourVector(float px, float py, float pz, float E) :
    px_(px), py_(py), pz_(pz), E_(E) {}
  float pt();
  float mass();
  FourVector operator+(const FourVector & other );
private:
  float px_, py_, pz_;
  float E_;
};

class Particle : public FourVector{
public:
  Particle(float charge, const FourVector & p4):
    FourVector(p4), charge_(charge){}
  void print();
private:
  float charge_;
};

#endif
