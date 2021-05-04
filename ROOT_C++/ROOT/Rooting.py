#Example of JITting

import ROOT

cpp_code = """
int f(int i) { return i*i; }
class A {
public:
A() { cout << "Hello PyROOT!" << endl; }
};
"""
# Inject the code in the ROOT interpreter
ROOT.gInterpreter.ProcessLine(cpp_code)
#ROOT.gInterpreter.ProcessLine('#include "my_cpp_library.h"') for example
#ROOT.gSystem.Load('./my_cpp_library.so') for load libraries

# We find all the C++ entities in Python!
a = ROOT.A() # this prints Hello PyROOT!
x = ROOT.f(3) # x = 9
print(x)
