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

  cout << "\nPostorder traversal ";
  postorderTraversal(root);

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
Node number3
Node number7
your choice = l or rl
Node number7
your choice = l or rr
Node number9
your choice = l or rl
your choice = l or rr
Node number2
your choice = l or rl
your choice = l or rl
Inorder traversal 2->7->9->3->7->
Inorder traversal without recursion 2->7->9->3->7->
Preorder traversal 3->7->2->9->7->
Postorder traversal 2->9->7->7->3-> */
