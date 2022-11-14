#include<iostream>
#include<cstring>
using namespace std;

typedef struct BTREE 
{ 
  char data; 
  struct BTREE *left; 
  struct BTREE *right; 
}BTNode,*BTree;
char PreOrder[100];
char InOrder[100];
int Len;

int SearchChar(int st,int ed, char x);
BTree BuildTree(char x, int *cnt, int st, int ed, int now){
	// Build Tree Node with char x
	// No need to build
	if(x == '\0' || now == -1){
		return NULL;
	}
	(*cnt)++;
	//printf("cnt move to %d.\n",*cnt);
	//new node root
	BTree root = new BTNode;
	root = new BTNode;
	root->data = x;
	root->left = NULL;
	root->right = NULL;
	//search next node char
	if(*cnt+1 >= Len)
		return root;
	char nxtChar = PreOrder[(*cnt)+1];
	//printf("Searching for char %c.\n",nxtChar);
	int nxtRoot = SearchChar(st, now, nxtChar);
	root->left = BuildTree(nxtChar, cnt, st, now, nxtRoot);

	if(*cnt+1 >= Len)
		return root;
	nxtChar = PreOrder[(*cnt)+1];
	//printf("Searching for char %c.\n",nxtChar);
	nxtRoot = SearchChar(now+1, ed, nxtChar);
	root->right = BuildTree(nxtChar, cnt, now+1, ed, nxtRoot);

	return root;
}

void PrintBTree(BTree root){
	if(!root){
		return;
	}
	PrintBTree(root->left);
	PrintBTree(root->right);
	putchar(root->data);
	// printf("%c", root->data);
	return;
}

	
int SearchChar(int st,int ed, char x){
	for(int i = st; i < ed; ++i){
		if(InOrder[i]==x){
			//printf("Found char %c successfully. Location: %d.\n", x, i);
			return i;
		}
	}
	//Not Found
	return -1;
}
int main(){
	scanf("%s%s",PreOrder,InOrder);
	//printf("PreOrder:%s", PreOrder);
	//printf("InOrder:%s", InOrder);
	Len = strlen(PreOrder);
	int Len2 = strlen(InOrder);
	if (Len != Len2){
		printf("error");
		return -1;
	}
	int *cnt = new int;
	*cnt = -1;
	char FirstChar = *PreOrder;
	//printf("Searching for char %c.\n",FirstChar);
	int FirstNow = SearchChar(0,Len,FirstChar);
	if(FirstNow == -1){
		printf("error");
		return 0;
	}
	BTree BiTree = BuildTree(FirstChar, cnt, 0, Len, FirstNow);
	PrintBTree(BiTree);
	//if(PreOrder[strlen(PreOrder)]=='\0')
	//	printf("OK");
	//printf("%s\n%s",PreOrder,InOrder);
	return 0;
}
