#ifndef FILE_H
#define FILE_H
#include <math.h>
#include <iostream>

template <class type>
class FourVector {
public:
  FourVector() {}
  FourVector(type px, type py, type pz, type E) :
    px_(px), py_(py), pz_(pz), E_(E) {}

  type get_px() {return px_;}
  type get_py() {return py_;}
  type get_pz() {return pz_;}
  type get_E() {return E_;}

  type pt(){return sqrt(px_*px_ + py_*py_ + pz_*pz_);}
  type mass(){return sqrt(E_*E_ - (px_*px_ + py_*py_ + pz_*pz_));}

  template <class type2>
  operator FourVector<type2>() const {return FourVector<type2>(px_,py_,pz_,E_);}

  FourVector operator + (FourVector<type> & other) {
    return FourVector<type> (px_ + other.get_px(), py_ + other.get_py(),
                            pz_ + other.get_pz(), E_ + other.get_E());}
private:
  type px_, py_, pz_, E_;
};

template <class type>
class Particle : public FourVector<type> {
public:
  Particle() {}
  Particle(type charge, const FourVector<type> & p4):
    FourVector<type>(p4), charge_(charge) {}

  type get_charge() {return charge_;}
  void print(){
    std::cout<<"Particle with mass "<<FourVector<type>::mass()<<" and charge "<<charge_<<std::endl;
  }

private:
  type charge_;
};

#endif
