## 一、代码前的思考
1，拿到一道题，想骨架的三个问题是什么？
首先看我最终想要的是什么，然后看我需要遍历什么内容，最后看我需要哪些变量

2.这件事做几次，就……”，这句规则后半句是什么？
passed = [] 整个程序只做 1 次，所以放在for循环前
all_pass = True 每个学生做 1 次，所以放在第一层for循环里
if score < 60 每个成绩做 1 次，所以放在第二层for循环里
总结：如果只做一次，放到循环外 ；如果对每个变量都做一次，则放在循环里。如果对每个变量的变量都做一次，则放到第二层for循环里

## 二、三个模版
1.字典计数模板(针对字典或列表里的内容进行计数)
```python
result={}
for x in 数据列表:
    if x in result:
        result[x]+=1
    else:
        result[x]=1
print(result)
```

2.标记变量模板（要求统计满足哪些条件时的数据）
```python
for  name, score in 数据字典   :
    all_passed=True
    for 具体数据 in score
        if       :
            all_passed=False
    if  all_passed:
        结果应该需要的内容
print()
```

3.打擂台模板（通过比较后得到最高或最低）
```python
high_num=None
high_name=None
先算出数值
for num,name in 数据字典：
    if high_num is None or num > high_num:
        high_num=num
        high_name=name
print()
```



 pairs = {')': '(', ']': '[', '}': '{'}

if ch in pairs:                                   # 遇到右括号
    if len(stack) == 0 or stack[-1] != pairs[ch]: # 栈是空的，或者栈顶不配对
        return False
    stack.pop()                                   # 配对成功，拿走栈顶的左括号


    def ping(self, t):
    self.q.append(t)                  # 新请求排到队尾
    while self.q[0] < t - 3000:       # 队头太老（早于 t-3000）
        self.q.popleft()              # 把它移出队列
    return len(self.q)                # 剩下的就是最近 3000 毫秒内的请求

    def containsDuplicate(self, nums):
    seen = set()
    for num in nums:
        if num in seen:      # 之前见过这个数
            return True      # 有重复
        seen.add(num)        # 没见过，就记下来
    return False             # 全部查完都没有重复

特征值 = 数据在这个方向上的方差。
特征值越大，数据在这个方向上分布得越开，包含的信息越多，这个主成分就越重要。
占比 = vals / vals.sum()。

全部同号 → 表达“总量”，比如身材数据里的“体型大小”。
正负混合 → 表达“对比”，比如成绩里的“偏理 vs 偏文”、便利店里的“冷 vs 热”。