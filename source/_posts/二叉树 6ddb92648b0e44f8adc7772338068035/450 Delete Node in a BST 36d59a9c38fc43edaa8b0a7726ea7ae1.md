---
title: 450. Delete Node in a BST
categories: Tree
---
# 450. Delete Node in a BST

Tags: recursion
link: https://leetcode.com/problems/delete-node-in-a-bst/

# 题目

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return *the **root node reference** (possibly updated) of the BST*.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.

## **Example 1:**

![del_node_1.jpg](450%20Delete%20Node%20in%20a%20BST%2036d59a9c38fc43edaa8b0a7726ea7ae1/del_node_1.jpg)

```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
```

## **Example 2:**

![del_node_supp.jpg](450%20Delete%20Node%20in%20a%20BST%2036d59a9c38fc43edaa8b0a7726ea7ae1/del_node_supp.jpg)

```
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
```

# 解题思路

```cpp
class Solution
{
public:
    TreeNode *deleteNode(TreeNode *root, int key)
    {
        if (root)
            if (key < root->val)
                root->left = deleteNode(root->left, key); // We frecursively call the function until we find the target node
            else if (key > root->val)
                root->right = deleteNode(root->right, key);
            else
            {
                if (!root->left && !root->right)
                    return NULL; // No child condition
                if (!root->left || !root->right)
                    return root->left ? root->left : root->right; // One child contion -> replace the node with it's child
                                                                  // Two child condition
                TreeNode *temp = root->left; //(or) TreeNode *temp = root->right;
                while (temp->right != NULL)
                    temp = temp->right;                         //      while(temp->left != NULL) temp = temp->left;
                root->val = temp->val;                          //       root->val = temp->val;
                root->left = deleteNode(root->left, temp->val); //        root->right = deleteNode(root->right, temp);
            }
        return root;
    }
};
```