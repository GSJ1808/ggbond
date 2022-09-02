---
title: 124. Binary Tree Maximum Path Sum
categories: Tree
---
# 124. Binary Tree Maximum Path Sum

Tags: recursion
link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# 题目

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return *the maximum **path sum** of any **non-empty** path*.

二叉树中的路径是节点序列，其中序列中的每对相邻节点都有一条连接它们的边。一个节点最多只能在序列中出现一次。请注意，路径不需要通过根。
路径的路径总和是路径中节点值的总和。
给定二叉树的根，返回任意非空路径的最大路径和。

## **Example 1:**

![exx1.jpg](124%20Binary%20Tree%20Maximum%20Path%20Sum%20f35ca33978064280b1a24b1ad4126c1c/exx1.jpg)

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

## **Example 2:**

![exx2.jpg](124%20Binary%20Tree%20Maximum%20Path%20Sum%20f35ca33978064280b1a24b1ad4126c1c/exx2.jpg)

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

# 解题思路

   `4
   / \
  11 13
 / \
7   2`

由于这是一个很简单的例子，很容易就能找到最长路径为 7->11->4->13，那么怎么用递归来找出正确的路径和呢？根据以往的经验，树的递归解法一般都是递归到叶节点，然后开始边处理边回溯到根节点。这里就假设此时已经递归到结点7了，其没有左右子节点，如果以结点7为根结点的子树最大路径和就是7。然后回溯到结点 11，如果以结点 11 为根结点的子树，最大路径和为 7+11+2=20。但是当回溯到结点4的时候，对于结点 11 来说，就不能同时取两条路径了，只能取左路径，或者是右路径，所以当根结点是4的时候，那么结点 11 只能取其左子结点7，因为7大于2。所以，对于每个结点来说，要知道经过其左子结点的 path 之和大还是经过右子节点的 path 之和大。递归函数返回值就可以定义为以当前结点为根结点，到叶节点的最大路径之和，然后全局路径最大值放在参数中，用结果 res 来表示。

在递归函数中，如果当前结点不存在，直接返回0。否则就分别对其左右子节点调用递归函数，由于路径和有可能为负数，这里当然不希望加上负的路径和，所以和0相比，取较大的那个，就是要么不加，加就要加正数。然后来更新全局最大值结果 res，就是以左子结点为终点的最大 path 之和加上以右子结点为终点的最大 path 之和，还要加上当前结点值，这样就组成了一个条完整的路径。而返回值是取 left 和 right 中的较大值加上当前结点值，因为返回值的定义是以当前结点为终点的 path 之和，所以只能取 left 和 right 中较大的那个值，而不是两个都要，参见代码如下：

```cpp
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int res = INT_MIN;
        nodePathSum(root,res);
        return res;

    }
    int nodePathSum(TreeNode *node, int &maxPathSum)
    {
        if(!node)return 0;
        int left = max(nodePathSum(node->left,maxPathSum),0);
        int right = max(nodePathSum(node->right,maxPathSum),0);
        maxPathSum = max(maxPathSum,node->val+left+right);
        return max(left,right)+node->val;
    }
};
```