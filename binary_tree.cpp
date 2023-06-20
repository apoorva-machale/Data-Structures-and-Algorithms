// Tree traversal in C++

#include <iostream>
using namespace std;

struct Node {
  int data;
  struct Node *left, *right;
  /*Node(int data) {
    this->data = data;
    left = right = NULL;
  }*/
};

// Preorder traversal
void preorderTraversal(struct Node* node) {
  if (node == NULL)
    return;

  cout << node->data << "->";
  preorderTraversal(node->left);
  preorderTraversal(node->right);
}

// Postorder traversal
void postorderTraversal(struct Node* node) {
  if (node == NULL)
    return;

  postorderTraversal(node->left);
  postorderTraversal(node->right);
  cout << node->data << "->";
}

// Inorder traversal
void inorderTraversal(struct Node* node) {
  if (node == NULL)
    return;

  inorderTraversal(node->left);
  cout << node->data << "->";
  inorderTraversal(node->right);
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
 int n=5,x;

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

  cout << "\nPreorder traversal ";
  preorderTraversal(root);

  cout << "\nPostorder traversal ";
  postorderTraversal(root);

  return 0;
  
};



//output
/*
apoorva@ubuntu:~$ cd Documents/
apoorva@ubuntu:~/Documents$ cd cpp/
apoorva@ubuntu:~/Documents/cpp$ g++ -o bi_tree binary_tree.cpp 
apoorva@ubuntu:~/Documents/cpp$ ./bi_tree 
Inorder traversal 5->12->6->1->9->
Preorder traversal 1->12->5->6->9->
Postorder traversal 5->6->12->9->1->*/
