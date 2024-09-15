#include <iostream>
#include <vector>
using namespace std;

class Solution{
	public:
	vector<int> replaceElements(vector<int> arr){
      		int n = arr.size();
      		int maxSoFar = arr[n-1];
      		arr[n-1] = -1;
      		for(int i=n-2;i>=0;i--)
      		{
        		int temp = maxSoFar;
        		if(maxSoFar < arr[i])
        			maxSoFar = arr[i];
        		arr[i] = temp;
      		}
      		return arr;
    	}
};

int main(){
	Solution obj;
	vector<int> arr = {17,18,5,4,6,1};
	arr = obj.replaceElements(arr);
	cout<<"\nAfter operation,array ";
	for(int i=0;i<arr.size();i++){
		cout<<" "<<arr[i];
	}
	return 0;
}

/* OUTPUT

apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ g++ -o replace replace_greatest_element_on_right.cpp -std=c++11
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ ./replace 

After operation,array  18 6 6 6 1 -1 */
