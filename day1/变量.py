"""     变量命名规则。

    基本数据类型：整数、浮点数、字符串、布尔值。

    类型转换。 """

    #常见错误：
    # 错误1：认为变量类型固定；
    # 错误2：混淆变量作用域；在函数内修改全局变量需要使用关键字global或在函数内重新赋值 
    # 错误3：变量命名不规范

""" 练习题
    题目1（入门）
    编写一个程序，要求用户输入姓名和年龄，并输出：
    你好，[姓名]！你今年[年龄]岁。

    题目2（中级）
    创建一个变量distance_km存储距离（公里），将其转换为英里（1公里≈0.6214英里），并输出结果。

    题目3（进阶）
    设计一个温度转换程序，用户输入摄氏度（如25），程序将其转换为华氏度（公式：华氏度 = 摄氏度 * 9/5 + 32），并输出：
    25摄氏度 = 77.0华氏度 """

""" 深入思考
如果变量的命名和赋值可以显著影响代码的可维护性，你会如何设计一套规则来管理项目中成千上万的变量？
例如，如何处理临时变量、全局变量和常量？

（提示：思考变量作用域、命名约定、代码模块化与封装） """
def main(solution=1):
    try:    
        if solution==1:    
            age=int(input("请输入您的年龄"))
            name=input("请输入您的姓名")
            print(f"您好，{name}!,您今年{age}岁了")
        elif solution==2:
            distance_km=float(input("你想查询多少km"))
            print(f"{distance_km}km=={0.6214*distance_km}miles")        
        elif solution==3:
            temp_cesieas=float(input("你想查询多少摄氏度"))
            temp_wals=temp_cesieas*9/5+32
            print(f"{temp_cesieas}摄氏度=={temp_wals}华氏度")   
        else:
            print("请输入有效的问题编号，1,2,3")   
    except ValueError:
        print("请输入有效的数字")  
if __name__ == "__main__":
    solution=3
    main(solution=solution)

""" 
思考：
    使用配置类+属性访问全局变量；
    用_前缀表示模块私有变量；
    其他函数变量生命不超过200行代码 """