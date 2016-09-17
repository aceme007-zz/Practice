// Dec 2014
//LinkList insertAtEnd insertAtStart, reverse LinkedList
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* head; //global var

struct Node* insertAtEnd(int num){
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = num;
    temp->next = NULL;
    //1st entry move head
    if (head == NULL){
        head = temp;
    }
    else {
    //traverse till end
        struct Node* temp2 = head;
        while (temp2->next != NULL) {
            temp2 = temp2->next;
        }
        temp2->next = temp;
    }
    return head;
}

struct Node* insertAtStart(int num){
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = num;
    temp->next = NULL;
    
    if (head == NULL){
        head = temp;
    }
    else {
        temp->next = head;
        head = temp;
    }
    return head;
}

struct Node* reverse(struct Node* head){
    struct Node* prevItem = (struct Node*)malloc(sizeof(struct Node));
    struct Node* currentItem = (struct Node*)malloc(sizeof(struct Node));
    struct Node* nextItem = (struct Node*)malloc(sizeof(struct Node));
    currentItem = head;
    prevItem = NULL;
    while (currentItem != NULL){
        nextItem = currentItem->next;
        currentItem->next = prevItem;
        prevItem = currentItem;
        currentItem = nextItem;
    }
    head = prevItem;
    return head;
}


void printList(struct Node* head) {
    struct Node* temp3 = head;
    printf("List is: ");
    while (temp3 != NULL) {
            printf ("%d ", temp3->data);
            temp3 = temp3->next;
        }
        printf("\n");
}

int main(int argc, char** argv) {
    head = NULL;
    /*
    int i, num, n;
    printf("Enter total number of values :");
    scanf ("%d",&n);
   
    for (i=0; i<n; i++){
        printf("Enter a number: ");
        scanf ("%d",&num);
        insertAtEnd(num);
        printList();
    }
    */
    insertAtStart(62);
    insertAtEnd(12);
    insertAtEnd(22);
    insertAtEnd(32);
    insertAtStart(42);
    insertAtStart(52);
    printList(head);
    head = reverse(head);
    printList(head);
    return (EXIT_SUCCESS);
}