#include ROOT

TFile f("myfile.root", "RECREATE");
TNtuple myntuple("n", "n", "x:y:z:t");
// We assume to have 4 arrays of values:
// x_val, y_val, z_val, t_val

for (auto ievt: ROOT::TSeqI(128)) {
  myntuple.Fill(x_val[ievt], y_val[ievt], z_val[ievt], t_val[ievt]);
}
myntuple.Write();
f.Close();

TFile f("myfile.root");
TNtuple *myntuple;
f.GetObject("myfile", myntuple);
TH1F h("h", "h", 64, -10, 10);
for (auto ievt: ROOT::TSeqI(myntuple->GetEntries()) {
  myntuple->GetEntry(ievt);
  auto xyzt = myntuple->GetArgs(); // Get a row
  if (xyzt[2] > 0) h.Fill(xyzt[0] * xyzt[1]);
}
h.Draw();
