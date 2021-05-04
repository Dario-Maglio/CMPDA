#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define X 8

char mine[X+2][X+2];
char campo [X+2][X+2];
int mosse=0;
bool fine_gioco=false;

void genera_campo(void);
void visualizza_campo(void);
void carica_mossa(int x,int y);
int adiacenti(int x, int y);
void vedo(void);

int main (void){
  int x,y;
  genera_campo();
  visualizza_campo();
  vedo();
  while (mosse<(X*X)){
    printf("Inserisci le coordinate della mossa (x,y): ");
    scanf("%d,%d",&x,&y);
    carica_mossa(x,y);
    visualizza_campo();
    if (fine_gioco) {
      printf("\n-----------------Booooom--------------------\n");
      exit(0);
    }
  }
  printf("Complimenti: you survived! :D\n");
  return 0;
}



void genera_campo(void){
  int random;
  char ch;
  srand (time(NULL));
  for (int i=1;i<=X;i++){
    for(int j=1;j<=X;j++){
      random=rand()%(X/2);
      if (random)
        mine[i][j]='-';
      else{
        mine[i][j]='*';
        mosse++; 
      }
      campo[i][j]='-';
    } 
  }
}

void visualizza_campo(void){
  printf ("   1 2 3 4 5 6 7 8\n\n");
  for (int i=1;i<=X;i++){
    printf("%d  ",i);
    for(int j=1;j<=X;j++){
      if (campo[i][j]<9)
        printf("%d ", campo[i][j]);
      else
        printf("%c ", campo[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}

void vedo (void){
  printf ("  1 2 3 4 5 6 7 8\n");
  for (int i=1;i<=X;i++){
    printf("%d ",i);
    for(int j=1;j<=X;j++){
      printf("%c ", mine [i][j]);
    }
    printf("\n");
  }
  printf("\n");
}

int adiacenti(int x, int y){
  return (mine[x-1][y-1]=='*')+(mine[x-1][y]=='*')+(mine[x-1][y+1]=='*')+(mine[x][y-1]=='*')
        +(mine[x][y+1]=='*')+(mine[x+1][y-1]=='*')+(mine[x+1][y]=='*')+(mine[x+1][y+1]=='*');
  
}


void carica_mossa(int x,int y){
  if (campo[x][y]<9)
    ;
  else if (mine[x][y]=='*'){
    campo[x][y]='*';
    fine_gioco=true;
  }else{
    campo[x][y]= adiacenti(x,y);
    mosse++;
    if (campo[x][y]==0){
      for (int r=-1;r<=1;r++){
        for (int c=-1;c<=1;c++){
          carica_mossa(x+r,y+c);
        }
      } 
      /*campo[x-1][y-1]=adiacenti(x-1,y-1);
      campo[x-1][y]=adiacenti(x-1,y);
      campo[x-1][y+1]=adiacenti(x-1,y+1);
      campo[x][y-1]=adiacenti(x,y-1);
      campo[x][y+1]=adiacenti(x,y+1);
      campo[x+1][y-1]=adiacenti(x+1,y-1);
      campo[x+1][y]=adiacenti(x+1,y);
      campo[x+1][y+1]=adiacenti(x+1,y+1);
      mosse +=9;

      oppure

      carica_mossa(x-1,y);
      carica_mossa(x-1,y+1);
      carica_mossa(x,y-1);
      carica_mossa(x,y+1);
      carica_mossa(x+1,y-1);
      carica_mossa(x+1,y);
      carica_mossa(x+1,y+1);*/
      }
  }
}























