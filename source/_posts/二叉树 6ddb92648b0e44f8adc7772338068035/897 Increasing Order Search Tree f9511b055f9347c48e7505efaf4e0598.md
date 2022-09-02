---
title: 897. Increasing Order Search Tree
categories: Tree
---
# 897. Increasing Order Search Tree

Tags: recursion
link: https://leetcode.com/problems/increasing-order-search-tree/

# 题目

Given the `root` of a binary search tree, rearrange the tree in **in-order** so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

给定二叉搜索树的根，按顺序重新排列树，使树中最左边的节点现在是树的根，并且每个节点都没有左孩子，只有一个右孩子。

## **Example 1:**

![ex1.jpg](897%20Increasing%20Order%20Search%20Tree%20f9511b055f9347c48e7505efaf4e0598/ex1.jpg)

```
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
```

## **Example 2:**

![ex2.jpg](897%20Increasing%20Order%20Search%20Tree%20f9511b055f9347c48e7505efaf4e0598/ex2.jpg)

```
Input: root = [5,1,7]
Output: [1,null,5,null,7]
```

# 解题思路

这道题可以用递归来求解。首先将root节点的左子树和右子树排列好；再将root→right链接到排列好的右子树上，将左子树的最右下角的元素的right链接到root，返回左子树。

```cpp
class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        if(!root)return nullptr;
        TreeNode *left = increasingBST(root->left);
        TreeNode *right = increasingBST(root->right);
        root->right = right;
        if(root->left)
        {
            TreeNode *node = left;
            while (node->right)
            {
                node = node->right;
            }
            node->right = root;
            root->left = nullptr;
            return left;
        }
        else return root;

    }
};
```