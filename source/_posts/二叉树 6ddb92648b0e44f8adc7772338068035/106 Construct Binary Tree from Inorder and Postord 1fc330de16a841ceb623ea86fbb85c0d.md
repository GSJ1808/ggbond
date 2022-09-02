---
title: 106. Construct Binary Tree from Inorder and Postorder Traversal
categories: Tree
---
# 106. Construct Binary Tree from Inorder and Postorder Traversal

Tags: recursion
link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# 题目

Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return *the binary tree*.

## **Example 1:**

![tree.jpg](106%20Construct%20Binary%20Tree%20from%20Inorder%20and%20Postord%201fc330de16a841ceb623ea86fbb85c0d/tree.jpg)

```
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

## **Example 2:**

```
Input: inorder = [-1], postorder = [-1]
Output: [-1]
```

# 解题思路

同**[105. Construct Binary Tree from Preorder and Inorder Traversal](105%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorde%20755dd59072a743b1927c3fc440ece071.md)**

```cpp
class Solution
{
public:
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder)
    {
        return buildTree(inorder, 0, inorder.size() - 1, postorder, 0, postorder.size() - 1);
    }
    TreeNode *buildTree(vector<int> &inorder, int ileft, int iright, vector<int> &postorder, int pleft, int pright)
    {
        if (ileft > iright or pleft > pright)
            return nullptr;
        TreeNode *node = new TreeNode(postorder[pright]);
        int i = 0;
        for (i = ileft; i <= iright; ++i)
        {
            if (postorder[pright] == inorder[i])
                break;
        }
        node->left = buildTree(inorder, ileft, i - 1, postorder, pleft, pleft + i - 1 - ileft);
        node->right = buildTree(inorder, i + 1, iright, postorder, pleft + i - ileft, pright - 1);
        return node;
    }
};
```