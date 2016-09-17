// Aug 2016

struct Node {
    int data;
    struct Node* next;
};
// address of head node is used to traverse complete list
// LL is identified by address of head node
// start at head and go next and go next
// time complex O(n)

Node* A; // pointer to node
A = NULL;

Node* temp = (Node*)malloc(sizeof(Node)); // Node* temp = new Node();
(*temp).data = 2; // temp->data = 2;
(*temp).link = NULL; // temp->link = NULL
A = temp;

#########################################################

//Insert node at beginning
struct Node* head;
void Insert (int x){
    Node* temp = new Node();
    temp->data = x;
    temp->next = head;
    head = temp;
}
void Print() {
    struct Node* temp = head;
    while (temp != NULL){
        printf("%d", temp->data);
        temp=temp->next;
    }
    printf("\n");
}
int main() {
    head = NULL;
    Insert(x);
    Print();
}

#########################################################
// Insert at any given position
struct Node {
    int data;
    struct Node* next;
};
struct Node* head; //global
void Insert (int data, int n){
    Node* temp1 = (Node*)malloc(sizeof(Node));
    temp1->data = data;
    temp1->next = NULL;
    if (n==1){
        temp1->next = head;
        head = temp1;
        return;
    }
    Node* temp2 = head;
    for (i=0;i<n-2;i++){
        temp2=temp2->next;
    }
    temp1->next = temp2->next;
    temp2->next = temp1;
}
void Print();
int main() {
    head = NULL; 
    Insert(2,1);
    Insert(3,2);
    Insert(4,1);
    Insert(5,2);
    Print();
}
// Delete at any position
struct Node {
    int data;
    struct Node* next;
};
struct Node* head;
void main() {
    
}

#########################################################
//TODO
// Reverse linked list -- iteration
void Reverse(){
    struct Node *current, *prev, * next;
    current = head;
    prev = NULL;
    while ( current != NULL) {
        next = current->next
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
}

#########################################################
// recursion traverse print
void Print (struct Node* p){
    if (p == NULL) return;
    printf("%d", p->data); // call this after traverse for rev print
    Print(p->next); 
}
void ReversePrint(struct Node* p){
    if (p == NULL) return;
    ReversePrint(p->next);
    printf("%d", p->data);
}

#########################################################

//TODO
// reverse linked list recursion

void ReverseLL(struct Node* p) {
    if (p->next == NULL) {
        head = p;
        return
    }
    ReverseLL(p->next);
    struct Node* q = p->next;
    q->next = p;
    p->next = NULL;
}

#########################################################
// doubly linked list
struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
}
struct Node* GetNewNode(int x){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = x;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode
}
// Insert at head doubly linked list
void InsertAtHead(int x){
    struct Node* newNode = GetNewNode(x);
    if (head == NULL){
        head = newNode;
        return;
    }
    head->prev = newNode;
    newNode->next = head;
    head = newNode;
}

#########################################################
// Binary Search Tree
// we always have address for root node
struct BstNode {
  int data;
  struct BstNode* left;
  struct BstNode* right;
}
// create a new node in dynamic memory
struct BstNode* root = NULL;

BstNode* GetNewNode (int data){
  struct BstNode* newNode = (struct BstNode*)malloc(sizeof(BstNode));
  newNode->data = data;
  newNode->left = newNode->right = NULL;
  return newNode;
}

BstNode* Insert(struct BstNode* root, int data) {
  if (root == NULL){
    root = GetNewNode(data);
  }
  else if (data <= root->data) {
    root->left = Insert(root->left, data);
  }
  else {
    root->right = Insert(root->right, data);
  }
  return root;
}

bool Search (struct BstNode* root, int data) {
  if (root == NULL) {
    return false;
  }
  if (root->data == data) {
    return true;
  } else if (data > root->data) {
    return Search (root->right, data);
  } else {
    return Search (root->left, data);
  }
}

void main(){
  root = Insert(root, 15);
  Insert(root, 10);
  Insert(root, 20);
  Search(root, 20);
}

#########################################################

// BST traversal
// level order traversal
// breadth first search BFS
// visit node, put address of children in queue and then use those

void BFSTraverse (struct Node* root) {
  if (root == NULL) {
    return;
  }
  queue<Node*> Q;
  Q.push(root);
  while (Q != empty){
    current = Q.front();
    cout<<current->data<<" ";
    if (current->left != NULL) { Q.push(current->left); }
    if (current->right != NULL) { Q.push(current->right); }
    Q.pop();
  }
}

#########################################################
// depth first search DFS
// preorder DLR
// inorder LDR
// postorder LRD

struct Node {
  int data;
  struct Node* left;
  struct Node* right;
}
void PreOrder(struct Node* root) {
  if (root == NULL) { return; }
  printf ("%c", root->data);
  PreOrder(root->left);
  PreOrder(root->right);
}

#########################################################

// given a BT check if it is BST or not

// Solution with O(n)2 approach 1
// check if all elements in left are less than root->data
int isSubtreeLesser (struct Node* root, int value) {
  if (root == NULL) return 1;
  if root->data < value &&
  if isSubtreeLesser (root->left, value) &&
  if isSubtreeLesser (root->right, value) {
    return 1;
  } else {
    return 0;
  }
}
int isSubtreeGreater (struct Node* root, int value) {
  if (root == NULL) return 1;
  if ( root->data > value &&
  isSubtreeGreater (root->left, value) &&
  isSubtreeGreater (root->right, value) ) {
    return 1;
  } else {
    return 0;
  }
}

int isBST (struct Node* root){
  // exit condition
  if (root == NULL) return 1;
  if ( isSubtreeLesser (root->left, root->data) &&
  isSubtreeGreater (root->right, root->data) &&
  isBST(root->left) &&
  isBST(root->right) ) {
    return 1;
  } else {
    return 0;  
  }
}

// solution with O(n) approach 2
// root : -infinity to +infinity
// left : -infinity to root->data
// right : root->data to +infinity
int isBSTUtil (struct Node* root, int min, int max) {
  if (root == NULL) return 1;
  if ( root->data > min &&
      root->data < max &&
      isBSTUtil(root->left, min, root->data) &&
      isBSTUtil(root->right, root->data, max) ) {
    return 1;
  } else {
    return 0;
  }
}

bool isBST (Node* root) {
  return isBSTUtil (root, INT_MIN, INT_MAX);
}

// solution in order traversel approach 3
bool isBSTInOrderHelper(BinaryTree *p, int& prev) {
  if (!p) return true;
  if (isBSTInOrderHelper(p->left, prev)) {
    if (p->data > prev) {
      prev = p->data;
      return isBSTInOrderHelper(p->right, prev);
    } else {
      return false;
    }
  } else {
    return false;
  } 
}

#########################################################

// delete a node from BST
struct Node {
  int data;
  struct Node* left;
  struct Node* right;
}

// return will be root (as it can be modified)
struct Node* deleteBST (struct Node* root, int data) {
  // we have to find the node 1st
  if (root == NULl) return root;
  else if (data > root->data) {
    root->right = deleteBST(root->right, data)
  }
  else if (data < root->data) {
    root->left = deleteBST(root->left, data)
  }
  else {
    // found the node so lets get ready to delete it
    // case 1 - this is a leaf node
    if (root->left == NULL && root->right == NULL) {
      delete root;
      root = NULL;
    }
    // case 2 when single child
    // no left child
    else if (root->left == NULL) {
      struct Node *temp = root;
      root = root->right;
      delete temp;
    }
    else if (root->right == NULL) {
      struct Node *temp = root;
      root = root->left;
      delete temp;
    }
    // case 3
    // in between, has 2 child
    else {
      struct Node *temp = FindMin(root->right);
      root->data = temp->data;
      root->right = deleteBST(root->right, temp->data);
    }
  }
  return root;
}

#########################################################
// find min or max in BST

// iterative
int FindMin(struct Node* root) {
  if (root == NULL) return -1;
  while (root->left != NULL) {
    root = root->left;
  }
  return root->data;
}

// recursion
int FindMax (struct Node* root) {
  if (root == NULL) { return -1; }
  else if (root->right == NULL) { return root->data; }
  return FindMax(root->right);
}

#########################################################

// find height of BST
// ie max nos of edges from root to leaf node
int FindHeight (struct Node* root) {
  if (root == NULL) {
    return -1;
  }
  leftHeight = FindHeight(root->left);
  rightHeight = FindHeight (root->right);
  return max(leftHeight, rightHeight) + 1;
}






