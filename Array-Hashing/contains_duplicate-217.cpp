#include <iostream>
#include <unordered_set>
using namespace std;

class Array_problem{
	public:
	bool find_duplicates(string nums){
		static unordered_set <int> s;
		for(int i=0;i<nums.size();i++){
			if(s.find(nums[i]) != s.end())
				return true;
			s.insert(nums[i]);
		}
		return false;
	
	}
	
};

int main(){
	Array_problem obj;
	string nums;
	cout<<"\nEnter string to find if it has duplicate letters ";
	cin>>nums;
	bool ans = obj.find_duplicates(nums);
	if(ans)
		cout<<"\nThe string has duplicates.";
	else
		cout<<"\nThe string does not have duplicates.";
	return 0;
}

//Include -std=c++11 to recognize usage of latest versions so that it doesn't give errors for unordered_set header file 


/*
OUTPUT

apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ g++ -o duplicates contains_duplicate-217.cpp -std=c++11
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ ./duplicates

Enter string to find if it has duplicate letters anagram

The string has duplicates. */
