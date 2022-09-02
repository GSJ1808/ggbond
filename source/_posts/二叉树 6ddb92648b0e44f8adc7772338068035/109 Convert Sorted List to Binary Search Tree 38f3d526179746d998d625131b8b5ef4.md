---
title: 109. Convert Sorted List to Binary Search Tree
categories: Tree
---
# 109. Convert Sorted List to Binary Search Tree

Tags: recursion
link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# 题目

Given the `head` of a singly linked list where elements are **sorted in ascending order**, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of *every* node never differ by more than 1.

给定单链表的头部，其中元素按升序排序，将其转换为高度平衡的 BST。
对于这个问题，高度平衡的二叉树被定义为每个节点的两个子树的深度相差不超过 1 的二叉树。

## **Example 1:**

![linked.jpg](109%20Convert%20Sorted%20List%20to%20Binary%20Search%20Tree%2038f3d526179746d998d625131b8b5ef4/linked.jpg)

```
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
```

## **Example 2:**

```
Input: head = []
Output: []
```

# 解题思路

首先找到链表的中间结点，该节点作为树的跟，该节点的左边的链表生成的树为左子树，

该节点右边的链表生成的树为左子树。

```cpp
class Solution {
public:
    ListNode* middleNode(ListNode* head)
    {
        if(!head) return head;
        ListNode* pre = new ListNode(0,head);
        ListNode *slow=head,*fast = head;
        while(fast->next and fast->next->next)
        {
            pre = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        pre->next = nullptr;
        return slow;
    }
    TreeNode* sortedListToBST(ListNode* head) {
        if(!head) return nullptr;
        ListNode *dummy = new ListNode(0, head);
        ListNode* middle = middleNode(head);
        TreeNode* root = new TreeNode(middle->val);
        if(dummy->next == middle) dummy->next = nullptr;
        root->left = sortedListToBST(dummy->next);
        root->right = sortedListToBST(middle->next);
        return root;
    }
};
```