#include <stdio.h>

#define N 1048576

void RandomVector(int *a, int nn){
  for (int i=0;i<nn;i++) {
    a[i]=rand()%100+1; 
  }
}

//serial sum
void VecAddSerial(int *a, int *b, int *c){
  for (int i=0;i<N;i++){
    c[i] = a[i]+b[i];
  }
}

int main(void) {
  int *h_a, *h_b, *h_c;
  int size = N*sizeof(int);

  float time;
  cudaEvent_t start,stop;
  cudaEventCreate(&start);
  cudaEventCreate(&stop);

  //Alloc in Host (and filling)
  h_a = (int *)malloc(size);
  h_b = (int *)malloc(size);
  h_c = (int *)malloc(size);
  RandomVector(h_a,N);
  RandomVector(h_b,N);

  //start time
  cudaEventRecord(start);

  //Launch Serial Sum on CPU
  VecAddSerial(h_a,h_b,h_c);

 //stop time
  cudaEventRecord(stop);
  cudaEventSynchronize(stop);
  cudaEventElapsedTime(&time, start, stop);

  //Print Result
  //  for(int i=0;i<N;i++){
  //  printf ("%d) h_a:%d h_b:%d h_c:%d\n",i,h_a[i],h_b[i],h_c[i]);
  //}

  //print time
  printf("Time: %3.5f ms\n",time);

  //Cleanup
  free(h_a);
  free(h_b);
  free(h_c);

  return(0);
}