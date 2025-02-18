""" 
1. 控制流简明解释
用途：控制代码执行顺序，根据条件选择分支（条件语句）或重复执行代码（循环）。
条件语句（if/elif/else）：用于逻辑判断，如用户权限验证、数据过滤。
循环（for遍历序列，while满足条件时重复）：处理批量数据（如列表元素）、持续监控状态（如游戏循环）。
跳转语句：break终止循环，continue跳过当前迭代，pass占位避免语法错误。 """

""" 2. 常见错误与避免方法
错误1：缩进不一致导致逻辑错误
问题：Python依赖缩进区分代码块，混用空格和Tab会报错。
解决：统一使用tab。

错误2：while循环条件未更新，导致死循环
问题：忘记在循环内修改变量，如while count < 5但未增加count。
解决：确保循环内有更新条件的语句，或用break安全退出14。

错误3：误用=代替==进行条件判断
问题：if x = 5会触发语法错误。
解决：条件表达式用==比较值2。 """

""" 3. 练习题
初级：编写程序，输出1-100内所有能被3整除但不能被5整除的数。
中级：使用while循环计算斐波那契数列前20项（如1,1,2,3,5…）。
高级：实现猜数字游戏：随机生成1-100的数，用户输入猜测，提示“太大”或“太小”，直到猜中后显示尝试次数。 """

""" 思考问题
“如果控制流是程序的骨架，如何设计条件与循环的嵌套结构，才能既保证效率又易于维护？”
（例如：多层循环如何优化？复杂条件如何拆分为函数？） """
import random
def main(solution=1):
    
    if solution==1:
        list_1=[]
        for i in range(3,100,3):
            if i%5!=0:
                list_1.append(i)
        print(list_1)
    elif solution==2:
        count=2
        fibonacci=[1,1]
        while count<20:
            fibonacci.append(fibonacci[count-1]+fibonacci[count-2])
            count+=1
        print(fibonacci,len(fibonacci))
    elif solution==3:
        num=random.randint(1,100)
        while True:
            guess=int(input("猜一个数"))
            if guess<num:
                print("猜小了")
            elif guess>num:
                print("猜大了")
            else:
                print("猜对了")
                break

if __name__=="__main__":
    main(1)
    main(2)
    main(3)

""" 一、针对多层循环：使用yield，逐个返回，仅处理当前元素，时间复杂度相同；优化算法
二、复杂的if-elif关系：将条件逻辑封装到函数，用函数名解释；使用字典映射 """