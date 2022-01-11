#include<iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int amount;
    cout << "enter amount" << endl;
    cin >> amount;
    while (amount <= 0){
       cout << "please enter an amount greater than or equal to 0" << endl;
    	cin >> amount;
    }
    int n_d; //number of denominations available
    cout << "enter number of denominations" << endl;
    cin >> n_d;
    int d[n_d]; //array for denomination
    int d_cnt[n_d] = {0}; //array to store which denomination is used how many time
    cout << "enter denominations one by one" << endl;
    for (int i = 0; i < n_d; i++){
        cin >> d[i];
    	 while(d[i] > amount){
    	 	cout << "please enter valid denomination less than the amount" << endl;
    	 	cin >> d[i];
    	 }
    }
    //sort the array
    int n = sizeof(d)/sizeof(d[0]);
    sort(d, d + n_d);
   
    cout << endl;
    int cnt = 0; //initially number of denominations to be used is zero
    int temp = amount;
    int iterator = (n_d - 1), q; //denomination array iterator, quotient
    //run the loop till amount is generated
    cout << "amount to be processed: " << temp << endl;
    while(temp > 0 && iterator >= 0){ 
        q = temp/d[iterator];
        d_cnt[iterator] = q; //store how many coins of a particular denomination used
        temp = temp - q*(d[iterator]); //decrease the amount
        iterator--;
    }
    
    if(temp != 0)
    	cout << "the amount cannot be processed with given denominations" << endl;
    else{
    	for(int i = 0; i < n_d; i++){
    		cout << "[" << d[i] << "]"<< " : " << d_cnt[i] << endl;
    	}
        int sum_coin = 0;
            for (int f = 0; f < n_d; f++){
    	    sum_coin += d_cnt[f];
        }
        cout << "total coins required : " << sum_coin << endl;

    }
    
   
    
   
    return 0;
}
