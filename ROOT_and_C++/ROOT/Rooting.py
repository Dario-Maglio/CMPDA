from time import sleep

import ROOT
import numpy.random as rd

# Inject the code in the ROOT interpreter -> Example of JITting
cpp_code = """
int f(int i) {
    return i*i;
};

class A {
    public:
    A() {cout << "Hello PyROOT!" << endl;}
};
"""
ROOT.gInterpreter.ProcessLine(cpp_code)
a = ROOT.A() # this prints Hello PyROOT!
x = ROOT.f(3) # x = 9
print(x)

ROOT.gInterpreter.ProcessLine('.L Histo.C')
#ROOT.gInterpreter.ProcessLine('#include "my_cpp_library.h"') for example
#ROOT.gSystem.Load('./my_cpp_library.so') for load libraries
ROOT.makeTGraph()

# TNtuples are used for branches (columns) made of 1 number
myntuple = ROOT.TNtuple("tuple", "tuple_label", "x:y:z:t")
matrix = rd.random([7981, 4]) #why it is the maximum?
for x_val, y_val, z_val, t_val in matrix: # from ROOT (auto ievt: ROOT::TSeqI(128))
  myntuple.Fill(x_val, y_val, z_val, t_val)

# Write TNtuple to a root file
g = ROOT.TFile("Rootingfile.root", "recreate")
myntuple.Write();
g.Close()

# Read TNtuple from the file, but copy object or create them out of the file
myntuple2 = ROOT.TNtuple("tuple2", "tuple2_label", "a:b:c:d")
myhist = ROOT.TH1F("name", "title", 64, 0, 4)

f = ROOT.TFile("Rootingfile.root", "read")
keyNames = [k.GetName() for k in f.GetListOfKeys()]
print(keyNames)
for event in f.tuple:
    myntuple2.Fill(event.x, event.y, event.z, event.t)
    if event.x > 0.5: myhist.Fill(event.x + event.y + event.z + event.t)
f.Close()

# Canvas
c = ROOT.TCanvas("Fake canvas")
c.SetGrid()
c.SetLogy()
txt = "#color[804]{My LaTex text #gamma^{1024}}"
myhist.Draw()
l = ROOT.TLatex(1,1,txt) #it doesn't work
l.Draw()
c.SaveAs("RootingTuple.png")

sleep(3)
