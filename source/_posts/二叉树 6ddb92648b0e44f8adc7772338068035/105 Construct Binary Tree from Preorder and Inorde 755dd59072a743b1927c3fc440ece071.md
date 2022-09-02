---
title: 105. Construct Binary Tree from Preorder and Inorder Traversal
categories: Tree
---
# 105. Construct Binary Tree from Preorder and Inorder Traversal

Tags: recursion
link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# 题目

Given two integer arrays `preorder`and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return *the binary tree*.

给定两个整数数组 preorder 和 inorder，其中 preorder 是二叉树的前序遍历，inorder 是同一棵树的中序遍历，构造并返回二叉树。

## **Example 1:**

![tree.jpg](105%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorde%20755dd59072a743b1927c3fc440ece071/tree.jpg)

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

## **Example 2:**

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

# 解题思路

可以确定，先序遍历中的第一个结点就是数的根节点。在中序遍历中，根节点之前的n个元素就是左子树的中序遍历，后m个元素就是根节点的右子树的中序遍历。

因此我们可以得到左子树和右子树的前序遍历和中序遍历，这道题就可以用递归来解决。

```cpp
class Solution
{
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
    {
        if (preorder.size() == 0)
            return nullptr;
        TreeNode* root = new TreeNode(preorder[0]);
        if (preorder.size() == 1)
            return root;
        int left = 0;
        for (; inorder[left] != preorder[0]; left++);
        vector<int> lp(preorder.begin() + 1, preorder.begin() + 1 + left);
        vector<int> li(inorder.begin(), inorder.begin() + left);
        vector<int> rp(preorder.begin() + 1 + left, preorder.end());
        vector<int> ri(inorder.begin() + left + 1, inorder.end());
        root->left = buildTree(lp,li);
        root->right = buildTree(rp,ri);
        return root;
    }
};
```

在上述的方法中多构建了四个数组，使得代码有些冗余，因此可以进行更改，构建一个新的函数，用额外的参数来表示数组。

```cpp
class Solution {
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return buildTree(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
    TreeNode *buildTree(vector<int> &preorder, int pLeft, int pRight, vector<int> &inorder, int iLeft, int iRight) {
        if (pLeft > pRight || iLeft > iRight) return NULL;
        int i = 0;
        for (i = iLeft; i <= iRight; ++i) {
            if (preorder[pLeft] == inorder[i]) break;
        }
        TreeNode *cur = new TreeNode(preorder[pLeft]);
        cur->left = buildTree(preorder, pLeft + 1, pLeft + i - iLeft, inorder, iLeft, i - 1);
        cur->right = buildTree(preorder, pLeft + i - iLeft + 1, pRight, inorder, i + 1, iRight);
        return cur;
    }
};
```