//929 - Unique email address
#include<iostream>
#include<string.h>
#include<vector>
#include<unordered_set>
using namespace std;

class Solution{
	public:
	int unique_email_address(vector<string> emails){
		unordered_set<string> st;
		for(auto &email:emails){
			string validEmail = "";
			for(auto &c:email){
				if(c=='+' || c=='@')
					break;
				if(c=='.')
					continue;
				validEmail +=c;
			}
			validEmail += email.substr(email.find('@'));
        		st.insert(validEmail);
        	}
        	return st.size();
	}
};

int main(){
	Solution obj;
	vector<string> emails = {"alice@leetcode.com", "alice.z@leetcode.com", "m.y+name@email.com"};
	int unique_emails = obj.unique_email_address(emails);
	cout<<"\nUnique Number of Emails are "<<unique_emails<<"\n";
	return 0;
}

/*OUTPUT
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ g++ -o email unique_email_adresses.cpp -std=c++11
apoorva@ubuntu:~/Documents/cpp/Array-Hashing$ ./email

Unique Number of Emails are 3
*/
