// Tree traversal in C++

#include <iostream>
#include <stack>
#include <vector>
using namespace std;

struct Node {
  int data;
  struct Node *left, *right;
};

// Preorder traversal
void preorderTraversal(struct Node* node) {
  if (node == NULL)
    return;

  cout << node->data << "->";
  preorderTraversal(node->left);
  preorderTraversal(node->right);
}

// Preorder traversal without recursion
void preorder_wo_recursion(struct Node* node){
	if (node == NULL)
    		return;
	Node* p = node;
	stack<Node*> s;
	s.push(p);
	while(!s.empty()){
	        p = s.top();
                s.pop();
		cout<<p->data <<"->";
		if(p->right !=NULL)
			s.push(p->right);
		if(p->left !=NULL)
			s.push(p->left);
	}
}

// Postorder traversal
void postorderTraversal(struct Node* node) {
  if (node == NULL)
    return;

  postorderTraversal(node->left);
  postorderTraversal(node->right);
  cout << node->data << "->";
}

// Postorder traversal without recursion
void postorder_wo_recursion(struct Node* node){
	if (node == NULL)
    		return;
	Node* p = node;
	stack<Node*> s1,s2;
	s1.push(p);
	while(!s1.empty()){
		p = s1.top();
                s1.pop();
		//p = s1.pop(); In C++ the method, it doesn't return the value removed from the stack. The reason is that there's no way in general to write such a function correctly from an exception-safety point of view.You need to store the value first and then remove it with pop... e.g.
		s2.push(p);
		if(p->left !=NULL)
			s1.push(p->left);
		if(p->right !=NULL)
			s1.push(p->right);
	}
	while(!s2.empty()){
		p = s2.top();
                s2.pop();
		//p = s2.pop();
		cout<<p->data <<"->";
	}
}

// Inorder traversal
void inorderTraversal(struct Node* node) {
  if (node == NULL)
    return;

  inorderTraversal(node->left);
  cout << node->data << "->";
  inorderTraversal(node->right);
}

// Inorder traversal without recursion
void inorder_wo_recursion(struct Node* node) {
	if (node == NULL)
    		return;
	stack<Node*> stk;
        vector<int> path;
        Node* current = node;

        while (!stk.empty() || current != NULL) {
            while (current != NULL) {
                stk.push(current);
                current = current->left;
            }
            Node* temp = stk.top();
            path.push_back(temp->data);
            stk.pop();
            current = temp->right;
        }
        for (int i = 0; i < path.size(); i++) {
          cout<< path[i] << "->";
        }
 
}

void insert(Node* root, Node* pnew){
	char ch;
	cout<<"your choice = l or r";
	cin>>ch;
	if(ch == 'l'){
		if(root->left == NULL)
			root->left = pnew;
		else
			insert(root->left, pnew);	
	}else if(ch == 'r'){
		if(root->right == NULL)
			root->right = pnew;
		else
			insert(root->right, pnew);
	}
	else
		cout<<"Invalid character";
	
}

Node* create(Node* root){
 int n,x;
 cout<<"Enter number of nodes";
 cin>>n;

 while(n){
 	Node* pnew = new Node;
 	Node* temp = new Node;
 	cout<<"Node number";cin>>x;
 	pnew -> data = x;
 	if(root == NULL){
 		root = pnew;
 	}else{
 		temp  = root;
 		insert(temp,pnew);
 	}
 	n--;
 }
 return root;
}


int main() {
  Node* root = NULL;
  
  root = create(root);
 	
  cout << "Inorder traversal ";
  inorderTraversal(root);
  
  cout << "\nInorder traversal without recursion ";
  inorder_wo_recursion(root);

  cout << "\nPreorder traversal ";
  preorderTraversal(root);
  
  cout << "\nPreorder traversal without recursion ";
  preorder_wo_recursion(root);

  cout << "\nPostorder traversal ";
  postorderTraversal(root);
  
  cout << "\nPostorder traversal without recursion ";
  postorder_wo_recursion(root);

  return 0;
  
};



//output
/*
apoorva@ubuntu:~$ cd Documents/
apoorva@ubuntu:~/Documents$ cd cpp/
apoorva@ubuntu:~/Documents/cpp$ cd Binary\ Tree/
apoorva@ubuntu:~/Documents/cpp/Binary Tree$ g++ -o binary binary_tree.cpp 
apoorva@ubuntu:~/Documents/cpp/Binary Tree$ ./binary
Enter number of nodes5
Node number7
Node number4
your choice = l or r9
Invalid characterNode number4
your choice = l or rl
Node number4
your choice = l or rr
Node number0
your choice = l or rl
your choice = l or rr
Inorder traversal 4->0->7->4->
Inorder traversal without recursion 4->0->7->4->
Preorder traversal 7->4->0->4->
Preorder traversal without recursion 7->4->0->4->
Postorder traversal 0->4->4->7->
Postorder traversal without recursion 0->4->4->7->*/
