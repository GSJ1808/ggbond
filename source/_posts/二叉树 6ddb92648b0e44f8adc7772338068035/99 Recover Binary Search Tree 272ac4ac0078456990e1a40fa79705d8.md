---
title: 99. Recover Binary Search Tree
categories: Tree
---
# 99. Recover Binary Search Tree

Tags: Depth-First Search
link: https://leetcode.com/problems/recover-binary-search-tree/

# 题目

You are given the `root` of a binary search tree (BST), where the values of **exactly** two nodes of the tree were swapped by mistake. *Recover the tree without changing its structure*.

您将获得二叉搜索树 (BST) 的根，其中树的恰好两个节点的值被错误地交换了。在不改变其结构的情况下恢复树。

## **Example 1:**

![recover1.jpg](99%20Recover%20Binary%20Search%20Tree%20272ac4ac0078456990e1a40fa79705d8/recover1.jpg)

```
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
```

## **Example 2:**

![recover2.jpg](99%20Recover%20Binary%20Search%20Tree%20272ac4ac0078456990e1a40fa79705d8/recover2.jpg)

```
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
```

# 解题思路

中序遍历能够将BST按从大到小的顺序输出。因此可以用两个指针来指向两个顺序错误的结点。

第一个错误的结点值会比后面的值大，第二个错误的结点值会比前一个结点值小。

```cpp
class Solution
{
public:
    TreeNode *first, *second, *pre;
    void inorder(TreeNode *node)
    {
        if (!node)
            return;
        inorder(node->left);
        if (!pre)
            pre = node;
        else
        {
            if (pre->val > node->val)
            {
                if (!first)
                    first = pre;
                second = node;
            }
            pre = node;
        }
        inorder(node->right);
    }
    void recoverTree(TreeNode *root)
    {
        inorder(root);
        swap(first->val, second->val);
    }
};
```