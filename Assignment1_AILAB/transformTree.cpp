//Apply transformations on the tree to get the desired output.
//Transformation is swap the left subtree with right subtree and vice versa.

#include <bits/stdc++.h>
using namespace std;

class TreeNode
{
public:
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) { val = x; }
};

void Swap(TreeNode **a, TreeNode **b)
{
    TreeNode *temp = *a;
    *a = *b;
    *b = temp;
}

TreeNode **firstPtr;
TreeNode **secondPtr;
void pairwiseSwap(TreeNode **root, int &count)
{
    if (!(*root))
        return;
    if (!(*root)->left && !(*root)->right)
    {
        secondPtr = root;

        count++;
        if (count % 2 == 0)
            Swap(firstPtr, secondPtr);

        else
            firstPtr = secondPtr;
    }
    if ((*root)->left)
        pairwiseSwap(&(*root)->left, count);

    if ((*root)->right)
        pairwiseSwap(&(*root)->right, count);
}
TreeNode *newNode(int data)
{
    TreeNode *temp = new TreeNode(data);
    temp->left = temp->right = NULL;
    return temp;
}

void printInorder(TreeNode *node)
{
    if (node == NULL)
        return;
    printInorder(node->left);

    cout << node->val << " ";
    printInorder(node->right);
}

TreeNode *buildTree(int preorder[], int inorder[], int n)
{

    TreeNode *root = NULL;
    stack<TreeNode *> st;
    set<TreeNode *> s;
    for (int pre = 0, in = 0; pre < n;)
    {

        TreeNode *node = NULL;
        do
        {
            node = new TreeNode(preorder[pre]);
            if (root == NULL)
            {
                root = node;
            }
            if (st.size() > 0)
            {
                if (s.find(st.top()) != s.end())
                {
                    s.erase(st.top());
                    st.top()->right = node;
                    st.pop();
                }
                else
                {
                    st.top()->left = node;
                }
            }
            st.push(node);
        } while (preorder[pre++] != inorder[in] && pre < n);

        node = NULL;
        while (st.size() > 0 && in < n &&
               st.top()->val == inorder[in])
        {
            node = st.top();
            st.pop();
            in++;
        }

        if (node != NULL)
        {
            s.insert(node);
            st.push(node);
        }
    }

    return root;
}

int main()
{
    int in[] = {9, 8, 4, 2, 10, 5, 10, 1, 6, 3, 13, 12, 7};
    int pre[] = {1, 2, 4, 8, 9, 5, 10, 10, 3, 6, 7, 12, 13};
    int len = sizeof(in) / sizeof(int);
    TreeNode *root = buildTree(pre, in, len);
    cout << "Inorder traversal before swap:\n";
    printInorder(root);
    cout << "\n";
    int c = 0;
    pairwiseSwap(&root, c);
    cout << "Inorder traversal after swap:\n";
    printInorder(root);
    cout << "\n";

    return 0;
}
