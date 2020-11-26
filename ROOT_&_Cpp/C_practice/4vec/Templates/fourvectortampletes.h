#ifndef FILE_H
#define FILE_H
#include <math.h>
#include <iostream>

template <class type>
class FourVector {
public:
  FourVector() {}
  FourVector(type px, type py, type pz, type e) :
    px_(px), py_(py), pz_(pz), e_(e) {}

  type get_px() const {return px_;}
  type get_py() const {return py_;}
  type get_pz() const {return pz_;}
  type get_E() const {return e_;}

  void set_px(type x) {px_ = x;}
  void set_py(type x) {py_ = x;}
  void set_pz(type x) {pz_ = x;}
  void set_e(type x) {e_ = x;}

  type pt() const {return sqrt(px_*px_ + py_*py_ + pz_*pz_);}
  type mass() const {return sqrt(e_*e_ - (px_*px_ + py_*py_ + pz_*pz_));}

  template <class type2>
  operator FourVector<type2>() const {return FourVector<type2>(px_,py_,pz_,e_);}

  FourVector operator + (const type &other) {
    return FourVector<type> (px_ + other.get_px(), py_ + other.get_py(),
                            pz_ + other.get_pz(), e_ + other.get_E());}

  FourVector operator * (type scl) {
    return FourVector<type> (px_*scl, py_*scl, pz_*scl, e_*scl);}

private:
  type px_, py_, pz_, e_;
};



template <class type>
class Particle : public FourVector<type> {

public:
  Particle(const char* ID, type charge, const FourVector<type> & p4):
    FourVector<type>(p4), charge_(charge), ID_(ID) {}

  const char* get_name() {return ID_;}
  type get_charge() {return charge_;}
  void print(){
    std::cout<<"The particle with name "<< Particle<type>::get_name() <<
    " has mass "<<FourVector<type>::mass()<<" and charge "<<charge_<<std::endl;
  }

private:
  type charge_;
  const char* ID_;

};

#endif
