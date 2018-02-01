#先行版
```
def cal(num, k, count=0):
    if num != 0 and k != 0 and num % k == 0:
        count += 1
        cal(num / k, k, count)
    else:
        return count


res = cal(32, 2)
print(res)
```
发现 res是None, 于是找到https://www.jianshu.com/p/c1dcf423e128。递归一层一层的进入，那么返回值也要一层一层的往外传。
又想到python递归默认次数限制的坑，顺带查一下统计在这里
#最终版
```
# 编写函数factors(num, k)，
# 函数功能是：求整数num中包含因子k的个数，
# 如果没有该因子则返回0，
# 例如：32=2×2×2×2×2，则factors(32,2)=5。
# 要求输入输出均在主函数中完成。

def cal(num, k, count=0):
    if num != 0 and k != 0 and num % k == 0:
        count += 1
        return cal(num / k, k, count)
    else:
        return count


res = cal(32, 2)
print(res)

import sys
print(sys.getrecursionlimit())
```

可通过
```
[`setrecursionlimit()`](https://docs.python.org/3.4/library/sys.html#sys.setrecursionlimit "sys.setrecursionlimit").

```
去修改默认的次数限制。
