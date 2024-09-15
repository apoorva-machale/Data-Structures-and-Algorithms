//347 - Top K frequent elements

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        
        unordered_map<int, int> m;
        for (int i = 0; i < n; i++) {
            m[nums[i]]++;
        }
        
        vector<vector<int>> buckets(n + 1);
        for (auto it = m.begin(); it != m.end(); it++) {
            buckets[it->second].push_back(it->first);
        }
        cout<<"\nBucket Elements ";
	// Traversing an nested vector
  	for(auto row_obj : buckets)
    	{
        	cout<<"{";
        	for (auto elem: row_obj)
        	{
        	    cout<<elem<<" ";
        	}cout<<"}, ";
    	}
        vector<int> result;
        
        for (int i = n; i >= 0; i--) {
            if (result.size() >= k) {
                break;
            }
            if (!buckets[i].empty()) {
                result.insert(result.end(), buckets[i].begin(), buckets[i].end());
            }
        }
        
        return result;
    }
};

int main(){
	Solution obj;
	vector<int> nums= {1,1,1,2,2,3,3};
	vector<int> ans;
	ans =  obj.topKFrequent(nums,2);
	cout<<"\nTop K Frequent Elements ";
	for(int i=0;i<ans.size();i++){
		cout<<" "<<ans[i];
	}
	cout<<"\n";
	return 0;
}

/*OUTPUT
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ g++ -o k_freq top_k_freq_elements.cpp -std=c++11
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ ./k_freq

Bucket Elements {}, {}, {3 2 }, {1 }, {}, {}, {}, {}, 
Top K Frequent Elements  1 3 2
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ 

*/
