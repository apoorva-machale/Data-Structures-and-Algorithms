//Trie Basic Operations

#include <iostream>
using namespace std;
#include <string.h>
#include <cstdlib>

// The number of children for each node
// We will construct a N-ary tree and make it
// a Trie
// Since we have 26 english letters, we need
// 26 children per node
#define N 26


struct TrieNode {
    // The Trie Node Structure
    // Each node has N children, starting from the root
    // and a flag to check if it's a leaf node
    char data; // Storing for printing purposes only
    TrieNode* children[N];
    int is_leaf;
};

TrieNode* make_trienode(char data) {
    // Allocate memory for a TrieNode
    TrieNode* node = (TrieNode*) calloc (1, sizeof(TrieNode));
    for (int i=0; i<N; i++)
        node->children[i] = NULL;
    node->is_leaf = 0;
    node->data = data;
    return node;
}

void free_trienode(TrieNode* node) {
    // Free the trienode sequence
    for(int i=0; i<N; i++) {
        if (node->children[i] != NULL) {
            free_trienode(node->children[i]);
        }
        else {
            continue;
        }
    }
    free(node);
}

TrieNode* insert_trie(TrieNode* root, string word) {
    // Inserts the word onto the Trie
    // ASSUMPTION: The word only has lower case characters
    TrieNode* temp = root;

    for (int i=0; word[i] != '\0'; i++) {
        // Get the relative position in the alphabet list
        int idx = (int) word[i] - 'a';
        if (temp->children[idx] == NULL) {
            // If the corresponding child doesn't exist,
            // simply create that child!
            temp->children[idx] = make_trienode(word[i]);
        }
        else {
            // Do nothing. The node already exists
        }
        // Go down a level, to the child referenced by idx
        // since we have a prefix match
        temp = temp->children[idx];
    }
    // At the end of the word, mark this node as the leaf node
    temp->is_leaf = 1;
    return root;
}

int search_trie(TrieNode* root, string word)
{
    // Searches for word in the Trie
    TrieNode* temp = root;

    for(int i=0; word[i]!='\0'; i++)
    {
        int position = word[i] - 'a';
        if (temp->children[position] == NULL)
            return 0;
        temp = temp->children[position];
    }
    if (temp != NULL && temp->is_leaf == 1)
        return 1;
    return 0;
}

void print_trie(TrieNode* root) {
    // Prints the nodes of the trie
    if (!root)
        return;
    TrieNode* temp = root;
    cout<<temp->data<<"->"; 
    for (int i=0; i<N; i++) {
        print_trie(temp->children[i]); 
    }
}

void print_search(TrieNode* root, string word) {
    cout<<"Searching for "<<word<<" : ";
    if (search_trie(root, word) == 0)
        cout<<"Not Found\n";
    else
        cout<<"Found\n";
}

int main() {
    // Driver program for the Trie Data Structure Operations
    TrieNode* root = make_trienode('\0');
    root = insert_trie(root, "hello");
    root = insert_trie(root, "hi");
    root = insert_trie(root, "teabag");
    root = insert_trie(root, "teacan");
    print_search(root, "tea");
    print_search(root, "teabag");
    print_search(root, "teacan");
    print_search(root, "hi");
    print_search(root, "hey");
    print_search(root, "hello");
    print_trie(root);
    cout<<"\n";
    free_trienode(root);
    return 0;
}

/*OUTPUT
apoorva@ubuntu:~/Documents/cpp/Trie$ g++ -o trie trie_basic_operations.cpp 
apoorva@ubuntu:~/Documents/cpp/Trie$ ./trie
Searching for tea : Not Found
Searching for teabag : Found
Searching for teacan : Found
Searching for hi : Found
Searching for hey : Not Found
Searching for hello : Found
->h->e->l->l->o->i->t->e->a->b->a->g->c->a->n->
*/
