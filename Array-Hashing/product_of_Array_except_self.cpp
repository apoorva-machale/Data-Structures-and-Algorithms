//238 - Product of Array Except Self

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1);
        
        int prefix = 1;
        for (int i = 0; i < n; i++) {
            result[i] = prefix;
            prefix = prefix * nums[i];
        }
        
        int postfix = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] = result[i] * postfix;
            postfix = postfix * nums[i];
        }
        
        return result;
    }
};

int main(){
	Solution obj;
	vector<int> nums= {-1,1,0,-3,3};
	vector<int> ans;
	ans =  obj.productExceptSelf(nums);
	cout<<"\nProduct of Array except self ";
	for(int i=0;i<ans.size();i++){
		cout<<" "<<ans[i];
	}
	cout<<"\n";
	return 0;
}

/*OUTPUT
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ g++ -o prod product_of_Array_except_self.cpp -std=c++11
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ ./prod

Product of Array except self  0 0 9 0 0
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ 

*/
