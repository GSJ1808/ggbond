---
title: 1022. Sum of Root To Leaf Binary Numbers
categories: Tree
---
# 1022. Sum of Root To Leaf Binary Numbers

Tags: Backtracking, Depth-First Search
link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# 题目

You are given the `root` of a binary tree where each node has a value `0` or `1`. Each root-to-leaf path represents a binary number starting with the most significant bit.

- For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent `01101` in binary, which is `13`.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return *the sum of these numbers*.

The test cases are generated so that the answer fits in a **32-bits** integer.

给定二叉树的根，其中每个节点的值为 0 或 1。每个从根到叶的路径代表一个从最高有效位开始的二进制数。
例如，如果路径是 0 -> 1 -> 1 -> 0 -> 1，那么这可以表示二进制的 01101，即 13。
对于树中的所有叶子，考虑从根到该叶子的路径表示的数字。返回这些数字的总和。
生成测试用例以使答案适合 32 位整数。

## **Example 1:**

![sum-of-root-to-leaf-binary-numbers.png](1022%20Sum%20of%20Root%20To%20Leaf%20Binary%20Numbers%2078eff24824ab4724aa23512159b1a68a/sum-of-root-to-leaf-binary-numbers.png)

```
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```

## **Example 2:**

```
Input: root = [0]
Output: 0
```

# 解题思路

这道题的解法和[第257题二叉树路径](257%20Binary%20Tree%20Paths%208e8a4a797a1b4941a77d21665f9cd04e.md)类似。首先通过DFS得到每一条二叉树的路径，并将这些路径存入到一个栈中，方便后续将二进制转换为十进制。最后将十进制相加即可

```cpp
class Solution {
public:
    stack<int> binary;
    vector<stack<int>> ans;
    void DFS(TreeNode* node)
    {
        if(!node)return;
        binary.push(node->val);
        if (!node->left and !node->right)
            ans.push_back(binary);
        if(node->left)DFS(node->left);
        if(node->right)DFS(node->right);
        binary.pop();
    }
    int convert(stack<int> &binary)
    {
        int as = 0;
        int i = 0;
        while (!binary.empty())
        {
            as+=binary.top()*pow(2,i);
            binary.pop();
            i++;
        }
        return as;
    }
    int sumRootToLeaf(TreeNode* root) {
        int res = 0;
        DFS(root);
        for(auto a : ans)
        {
            res+=convert(a);
        }
        return res;
    }
};
```

上述解法，用到了两个vector来保存临时结果，这里有一种更少占用内存的方法。

```cpp
class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        int res = 0;
        helper(root, 0, res);
        return res;
    }
    void helper(TreeNode* node, int cur, int& res) {
        if (!node) return;
        cur = cur * 2 + node->val;
        if (!node->left && !node->right) {
            res += cur;
        }
        helper(node->left, cur, res);
        helper(node->right, cur, res);
    }
};
```