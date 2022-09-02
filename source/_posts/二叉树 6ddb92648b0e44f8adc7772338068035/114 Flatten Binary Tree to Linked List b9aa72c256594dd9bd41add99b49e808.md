---
title: 114. Flatten Binary Tree to Linked List
categories: Tree
---
# 114. Flatten Binary Tree to Linked List

Tags: recursion
link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# 题目

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
- The "linked list" should be in the same order as a **[pre-order traversal](https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR)** of the binary tree.

给定二叉树的根，将树展平为“链表”：
“链表”应该使用相同的 TreeNode 类，其中右子指针指向列表中的下一个节点，左子指针始终为空。
“链表”的顺序应该与二叉树的前序遍历相同。

## **Example 1:**

![flaten.jpg](114%20Flatten%20Binary%20Tree%20to%20Linked%20List%20b9aa72c256594dd9bd41add99b49e808/flaten.jpg)

```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

## **Example 2:**

```
Input: root = []
Output: []
```

# 解题思路

该题的解题思路和**[897. Increasing Order Search Tree](897%20Increasing%20Order%20Search%20Tree%20f9511b055f9347c48e7505efaf4e0598.md)** 的解题思路一模一样。只不过是897题使用的中序遍历，这道题使用先序遍历。

```cpp
class Solution
{
public:
    void flatten(TreeNode *root)
    {
        flattenTree(root);
    }
    TreeNode *flattenTree(TreeNode *node)
    {
        if (!node)
            return node;
        TreeNode *left = flattenTree(node->left);
        TreeNode *right = flattenTree(node->right);
        TreeNode *tmp = left;
        if (tmp)
        {
            while (tmp->right)
            {
                tmp = tmp->right;
            }
            tmp->right = right;
            node->right = left;
            node->left = nullptr;
        }
        return node;
    }
};
```