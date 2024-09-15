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

int height(Node *root){
	int lht=1,rht=1,d=0;
	if(root != NULL){
		if(root->left == NULL && root->right == NULL)
			d=1;
		else{
			lht = lht + height(root->left);
			rht = rht + height(root->right);
			if(lht>rht)
				d=lht;
			else
				d=rht;
		}
	}
	return d;
}

int non_height(Node* root){
	int lh=0,rh=0,d=0;
	Node* temp1=root;
	Node* temp2=root;
	while(temp1 != NULL){
		lh=lh+1;
		temp1=temp1->left;
	}
	while(temp2 != NULL){
		rh=rh+1;
		temp2=temp2->right;
	}
	if(lh>rh)
		d=lh;
	else
		d=rh;
	return d;
}

void rleaf(Node* root){

	if(root != NULL){
		if(root->left == NULL && root->right == NULL)
			cout<<" "<<root->data;
		else{
			rleaf(root->left);
			rleaf(root->right);
		}
	}
}

int rleafcount(Node* root){
	if(root!=NULL){
		if(root->left == NULL && root->right == NULL)
			return 1;
		else
			return(rleafcount(root->left)+rleafcount(root->right));
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

Node* invert_binary(Node* root){
	if(root == NULL)
		return NULL;
	if(!(root->left == NULL && root->right==NULL))
		swap(root->left,root->right);
	//cout<<"\t"<<root->data;
	invert_binary(root->left);
	invert_binary(root->right);
	return root;
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
  
  int d = height(root);
  cout<<"\nHeight of the tree "<<d;
  
  int h = non_height(root);
  cout<<"\nHeight of the tree without using recursion "<<h;
  
  cout<<"\nLeaf Nodes are ";
  rleaf(root);
  
  int l = rleafcount(root);
  cout<<"\nNumber of leaf nodes "<<l;
  
  cout<<"\nInvert Binary Tree";
  root = invert_binary(root);


  return 0;
  
};



/*
OUTPUT

apoorva@ubuntu:~$ cd Documents/
apoorva@ubuntu:~/Documents$ cd cpp/
apoorva@ubuntu:~/Documents/cpp$ cd Binary\ Tree/
apoorva@ubuntu:~/Documents/cpp/Binary Tree$ g++ -o binary binary_tree.cpp 
apoorva@ubuntu:~/Documents/cpp/Binary Tree$ ./binary
Enter number of nodes4
Node number1
Node number2
your choice = l or rl
Node number3
your choice = l or rr
Node number4
your choice = l or rr
your choice = l or rr
Inorder traversal 2->1->3->4->
Inorder traversal without recursion 2->1->3->4->
Preorder traversal 1->2->3->4->
Preorder traversal without recursion 1->2->3->4->
Postorder traversal 2->4->3->1->
Postorder traversal without recursion 2->4->3->1->
Height of the tree 3
Height of the tree without using recursion 3
Leaf Nodes are  2 4
Number of leaf nodes 2*/
