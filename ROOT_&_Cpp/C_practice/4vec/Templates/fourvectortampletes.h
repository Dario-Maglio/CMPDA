#ifndef FILE_H
#define FILE_H
#include <math.h>
#include <iostream>
#include <string>

template <class type>
class FourVector {

private:
  type px_, py_, pz_, e_;

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
  operator FourVector<type2> () const {
    return FourVector<type2>(px_, py_, pz_, e_);
  }

  FourVector operator + (const FourVector<type> &other) {
    return FourVector<type> (px_ + other.get_px(), py_ + other.get_py(),
                             pz_ + other.get_pz(), e_ + other.get_E());
  }

  FourVector operator * (const type &scl) {
    return FourVector<type> (px_*scl, py_*scl, pz_*scl, e_*scl);
  }
};



template <class type>
class Particle : public FourVector<type> {

private:
  int charge_;
  const std::string ID_;

public:
  Particle(const std::string &ID, int charge, const FourVector<type> &p4):
           FourVector<type>(p4), charge_(charge), ID_(ID) {}

  std::string get_name() const {return ID_;}
  int get_charge() const {return charge_;}
  FourVector<type> get_vect() const {
    return FourVector<type>(FourVector<type>::get_px(), FourVector<type>::get_py(),
                            FourVector<type>::get_pz(), FourVector<type>::get_E());
  }

  template <class type2>
  operator Particle<type2> () const {
    return Particle<type2>(ID_, charge_, get_vect());
  }

  operator FourVector<type>() const {
    return get_vect();
  }

  Particle operator + (const Particle<type> &other) {
    return Particle<type> ("Sum of two particles", charge_ + other.get_charge(),
                           get_vect() + other.get_vect());
  }

  void print() {
    std::cout<<"The "<<ID_<<"particle has mass "<<FourVector<type>::mass()<<
                " and charge "<<charge_<<std::endl;
  }
};

#endif
