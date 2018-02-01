---
title: Python-递归
---
下午看到一道题，于是想到用递归解决，然后就遇到了问题。题目如下：编写函数factors(num, k)，函数功能是：求整数num中包含因子k的个数，如果没有该因子则返回0，例如：32=2×2×2×2×2，则factors(32,2)=5。要求输入输出均在主函数中完成。

## 先行版

```
def factors(num, k, count=0):
    if num != 0 and k != 0 and num % k == 0:
        count += 1
        factors(num / k, k, count)
    else:
        return count


res = factors(32, 2)
print(res)
```
发现 res是None, 于是找到https://www.jianshu.com/p/c1dcf423e128。 递归一层一层的进入，那么返回值也要一层一层的往外传。

## 最终版

```
def factors(num, k, count=0):
    if num != 0 and k != 0 and num % k == 0:
        count += 1
        return factors(num / k, k, count)
    else:
        return count


res = factors(32, 2)
print(res)
```
又想到python递归默认次数限制的坑，顺带查一下统计在这里

```
import sys
print(sys.getrecursionlimit())
```
可见默认次数1000，也可通过[`setrecursionlimit()`](https://docs.python.org/3.4/library/sys.html#sys.setrecursionlimit "sys.setrecursionlimit")去修改默认的次数限制。
