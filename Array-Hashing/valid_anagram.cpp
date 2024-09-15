#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Array_Hashing{
	public:
	
	//Approach 1
	bool valid_anagram_1(string s1, string s2){
		if(s1.length() != s2.length())
			return false;
		sort(s1.begin(),s1.end());
		sort(s2.begin(),s2.end());
		if(s1 == s2)
			return true;
		else
			return false;
	}
	
	//Approach 2
	bool valid_anagram_2(string s1, string s2){
		if(s1.length() != s2.length())
			return false;
		int arr[26] = {0};
		for(int i=0;i<s1.length();i++){
			arr[s1[i] -'a']++;
			arr[s2[i] - 'a']--;
		}
		for(int i=0;i<26;i++){
			if(arr[i] != 0)
				return false;
		}
		return true;
	}
	
};

int main(){
	Array_Hashing obj;
	string string1,string2;
	cout<<"\nEnter strings which needs to be compared: ";
	cin>>string1>>string2;
	
	//bool ans = obj.valid_anagram_1(string1, string2);
	bool ans = obj.valid_anagram_2(string1, string2);
	if(ans)
		cout<<"\nValid Anagram\n";
	else
		cout<<"\nInvalid Anagram\n";
		
	return 0;
}

/*OUTPUT
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ g++ -o valid_anagram valid_anagram.cpp 
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ ./valid_anagram 

Enter strings which needs to be compared: anagram nagaram

Valid Anagram
*/
