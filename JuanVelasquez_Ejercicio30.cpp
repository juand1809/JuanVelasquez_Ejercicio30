#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

int main(){
    ofstream outfile;
    double X = 1.0;
    double delta_x = 0.01;
    double delta_t = 0.01;
    double t = 0.0;
    double tmax = 2.0;
    double c = delta_x/delta_t;
    double beta = c*delta_t/delta_x;
    int N = X/delta_x + 1;
    double pi = 4*atan(1);
    double x;
    int i;
    double U_old [N];
    double U_new [N];
    
    for (i = 0; i < N; i++){
        x = i*delta_x;
        U_old[i] = 0.5*sin(4*pi*x/X);
        U_new[i] = U_old[i];
    }  
    
    outfile.open("data.dat");
    
    while(t < tmax){
        for(i = 1; i < N-1; i++){
            U_new[i] = (1.0-beta*beta)*U_old[i] - (0.5*beta)*(1-beta)*U_old[i+1] + (0.5*beta)*(1+beta)*U_old[i-1]; 
        }
        
        for(i = 0; i < N; i++){
            outfile << U_new[i] << " ";
        }
        outfile << "\n";
        
        for (i = 1; i < N-1; i++){
            U_old[i] = U_new[i];
        }
        
        t = t + delta_t;       
    }
    outfile.close();
    return 0;
}