//1929 - Concatenation of Array

#include <iostream>
#include <vector>
using namespace std;

class Solution{
	public:
	vector<int> concatenation_array(vector<int> nums){
		vector<int> ans;
		for(int i=0;i<nums.size();i++){
			ans.push_back(nums[i]);
		}
		for(int i=0;i<nums.size();i++){
			ans.push_back(nums[i]);
		}
		return ans;
	}
	
}; 

int main(){
	Solution obj;
	vector<int> nums= {1,2,3,4,5,6};
	vector<int> ans;
	ans =  obj.concatenation_array(nums);
	cout<<"\nConcatenation of array ";
	for(int i=0;i<ans.size();i++){
		cout<<" "<<ans[i];
	}
	return 0;
}
