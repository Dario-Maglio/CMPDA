void MakeTree() {
    // Create file first. The TTree will be associated to it
    TFile f("SimpleTree.root","RECREATE");
    TTree data("tree","Example TTree");
    // No need to specify column names

    // Associate variable pointer to column and specify its type, double
    double x, y, z, t;
    data.Branch("x",&x,"x/D");
    data.Branch("y",&y,"y/D");
    data.Branch("z",&z,"z/D");
    data.Branch("t",&t,"t/D");

    for (int i = 0; i<128; ++i) {
        x = gRandom->Uniform(-10,10);
        y = gRandom->Gaus(0,5);
        z = gRandom->Exp(10);
        t = gRandom->Landau(0,2);
        data.Fill();
    }

    data.Write();
    f.Close();
}

void MakeErrorGraph() {
    const int n_points=10;
    double x_vals[n_points] = {1,2,3,4,5,6,7,8,9,10};
    double y_vals[n_points] = {6,12,14,20,22,24,35,45,44,53};
    double y_errs[n_points] = {10.43,5,4.7,4.5,4.2,5.1,3.9,4.1,4.8,5};

    // Instance of the graph
    auto graph = new TGraphErrors(n_points,x_vals,y_vals,nullptr,y_errs);
    graph->SetTitle("Measurement XYZ;length [cm];Arb.Units");

    // Make the plot esthetically better
    graph->SetMarkerStyle(kOpenCircle);
    graph->SetMarkerColor(kBlue);
    graph->SetLineColor(kBlue);
    graph->SetFillColor(6);
    graph->SetFillStyle(3005);

    // The canvas on which we'll draw the graph
    auto mycanvas = new TCanvas();
    //graph->Draw("A4");  A stands for new axis and 4 for smooth Fill
    //graph->Draw("APE"); PE stands for point errors
    graph->Draw("AP4");

    // Deﬁne a linear function
    auto f = new TF1("Linear law","[0]+x*[1]",.5,10.5);
    f->SetLineColor(kRed);
    f->SetLineStyle(2);
    f->SetParameters(-1,5);
    f->Draw("Same");

    // Build and Draw a legend
    auto legend = new TLegend(.1,.7,.3,.9,"Lab. Lesson 1");
    legend->AddEntry(graph,"Exp. Points","PE");
    legend->AddEntry(f,"Th. Law", "L");
    legend->Draw();

    // Draw an arrow on the canvas
    auto arrow = new TArrow(8,8,6.2,23,0.02,"|>");
    arrow->SetLineWidth(2);
    arrow->Draw();
    // Add some text to the plot and highlight the 3rd label
    auto text = new TLatex(8.2,7.5,"#splitline{Maximum}{Deviation}");
    text->Draw();
    graph->GetXaxis()->ChangeLabel(3,-1,-1,-1,kRed);
}
