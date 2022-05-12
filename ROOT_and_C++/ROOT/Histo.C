void makeHist() {
  TH1F *hist = new TH1F("histogram","My Histogram;Asse1;Asse2", 40, 0, 4);
  hist->Draw();
}

void makeHist2() {
  TH1F *hist = new TH1F("hist","My Histogram", 40, 0, 4);
  TF1 *fun = new TF1("functionName", "[0]*sin([1]*x)", 0., 4.);
  fun->SetParameters(40,4);
  hist->FillRandom("gaus");
  hist->Draw();
  fun->Draw("Same");
}

void makeTGraph() {
  TGraph *g = new TGraph;
  for (auto i : {0,1,2,3,4}) g->SetPoint(i,i,i*i);
  g->SetMarkerStyle(39);
  g->SetMarkerSize(3);
  g->SetMarkerColor(kRed);
  g->SetLineColor(kAzure);
  g->SetTitle("My Graph; The X; My Y");
  g->Draw();
}

void macro2(){
  TH2F *h = new TH2F("h","Option COL example ",300,-4,4,300,-20,20);
  h->SetStats(0);
  h->SetContour(200);
  float px, py;
  for (int i = 0; i < 25000000; i++) {
    gRandom->Rannor(px,py); //Returns two number according to a Gaussian
    h->Fill(px-1,5*py);
    h->Fill(2+0.5*px,2*py-10.,0.1);
  }
  h->Draw("colz");
}
