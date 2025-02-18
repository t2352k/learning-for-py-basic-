"""
1.简明解释 
函数定义
用途：将代码块封装为可重复调用的逻辑单元，实现代码复用和模块化。
语法：def 函数名(参数): ...

    参数：
    位置参数：func(a, b)
    默认参数：def func(a=0)
    可变参数：*args（元组）、**kwargs（字典）

    返回值：
    用 return 返回结果，无 return 时默认返回 None。
    可返回多个值（实质是元组）。

变量作用域
局部变量：函数内定义的变量，仅在函数内有效。
全局变量：函数外定义的变量，需用 global 声明修改。
常见问题：函数内误改全局变量导致逻辑错误。

Lambda函数
定义：匿名函数，用于简化简单逻辑。
语法：lambda 参数: 表达式
场景：短小操作（如排序键、map()/filter() 参数）。 """

""" 
2. 常见错误与避免
错误1：变量作用域混淆
解决：在函数内用 global count 声明全局变量。

错误2：忽略可变参数的引用传递
python
def append_item(item, my_list=[]):
    my_list.append(item)  # 默认参数会累积！
    return my_list
print(append_item(1))  # 
print(append_item(2))  # [1, 2]（预期是 ？）

解决：默认参数用不可变类型（如 None），内部初始化。

错误3：滥用Lambda函数
解决：复杂逻辑用普通函数，lambda 仅用于简单表达式。 """

"""  练习题
基础：编写函数 is_even(num)，判断数字是否为偶数，返回布尔值。
进阶：创建函数 merge_dicts(dict1, dict2)，合并两个字典，若键重复则保留 dict2 的值。
高阶：用 Lambda 和 reduce() 计算列表中所有偶数的乘积。 """

""" “当函数需要修改外部数据时，直接修改参数与返回新对象哪种方式更安全？为什么函数式编程强调‘不可变数据
’？这与 Python 中可变对象（如列表）的特性有何矛盾？”
（例如：比较 sorted(list) 返回新列表 vs list.sort() 原地修改的差异） """
from functools import reduce
def main(solution=1):
    
    if solution==1:
        num=int(input("输入一个数字"))
        if num%2==0:
            return True
    elif solution==2:
        dict_1={"name": "Alice", "age": 25, "skills": ["Python"]}
        dict_2={"age": 26, "city": "Berlin", "skills": ["Java"]}
        for key,val in dict_1.items():#使用.items()才能正确遍历键、值
            if key not in dict_2:
                dict_2[key]=val
        print(dict_2)
    elif solution==3:
        
        lis = [2, 3, 4, 5, 10, 6]
        even_nums=filter(lambda x:x%2==0,lis)#filter留下满足条件的
        pro=1
        print(reduce(
            lambda x,pro:x*pro,
            even_nums,
            pro
        ))#reduce相当于把列表的数遍历一次  reduce（函数，可迭代对象，初始值）
if __name__=="__main__":
    main(1)
    main(2)
    main(3)

""" 1、直接修改参数可能意外修改外部数据，产生难以追踪的bug；返回新对象可以避免函数操作的副作用
2、强调不可变编程可以使得函数的输出仅依赖输入，便于调试和测试；可以避免多线程竞争问题，
因为多线程竞争的根源是多个线程同时读写共享的可变状态 """