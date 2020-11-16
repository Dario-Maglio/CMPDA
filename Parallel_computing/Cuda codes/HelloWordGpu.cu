#include <cuda.h>
#include <stdio.h>

__global__ void mykernel(void) {
  printf("Hello World from GPU! (block: %d thread: %d)\n",blockIdx.x,threadIdx.x);
}

int main(void) {
  mykernel <<<3,4>>>();
  cudaDeviceSynchronize();
  printf("Hello World from Host!\n");
  return 0;
}
