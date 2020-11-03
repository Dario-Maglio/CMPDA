#include <stdio.h>

#define N 1048576

void RandomVector(int *a, int nn){
  for (int i=0;i<nn;i++) {
    a[i]=rand()%100+1; 
  }
}

//kernel
__global__ void VecAddGpu(int *a, int *b, int *c){
  c[blockIdx.x] = a[blockIdx.x]+b[blockIdx.x];
}

int main(void) {
  int *h_a, *h_b, *h_c;
  int *d_a, *d_b, *d_c;
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

  //Alloc in Device
  cudaMalloc((void **)&d_a, size);
  cudaMalloc((void **)&d_b, size);
  cudaMalloc((void **)&d_c, size);



  //Copy input vectors form host to device
  cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
  cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

  //start time
  cudaEventRecord(start);

  //Launch Kernel  on GPU
  VecAddGpu<<<N,1>>>(d_a,d_b,d_c);
  cudaDeviceSynchronize();

  //stop time
  cudaEventRecord(stop);
  cudaEventSynchronize(stop);
  cudaEventElapsedTime(&time, start, stop);

  //Copy back the results
  cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);



  //Print Result
  //    for(int i=0;i<N;i++){
  //   printf ("%d) h_a:%d h_b:%d h_c:%d\n",i,h_a[i],h_b[i],h_c[i]);
  //}

  //print time
  printf("Time: %3.5f ms\n",time);

  //Cleanup
  free(h_a);
  free(h_b);
  free(h_c);
  cudaFree(d_a);
  cudaFree(d_b);
  cudaFree(d_c);

  return(0);
}
