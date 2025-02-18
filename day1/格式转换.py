""" 简明解释
用途：将数据从一种类型转换为另一种类型，解决数据类型不匹配问题（如字符串与数值运算、数据格式化输出等）。
常见场景：
    用户输入（字符串）转为数值进行数学计算
    数值结果转为字符串用于文本拼接
    布尔值与其他类型互转实现逻辑判断 """

""" 常见错误与避免方法
错误1：非数字字符串强制转数值
int("abc")  # ValueError: invalid literal for int()  
避免：先用isdigit()验证字符串是否为纯数字

错误2：浮点转整数时直接截断小数
print(int(3.9))  # 输出3（非四舍五入）  
避免：需四舍五入时用round(3.9)

错误3：误判布尔转换规则
print(bool("False"))  # 输出True（非空字符串均为True）  
避免：明确bool("False")等价于bool(len("False")>0) """

""" 4. 实际应用场景

场景1：数据清洗（CSV文件读取）
# 从CSV读取的"价格"列是字符串，需转为浮点数计算平均价格
prices = ["12.5", "8.0", "invalid", "15.3"]
valid_prices = [float(p) for p in prices if p.replace(".", "").isdigit()]
average = sum(valid_prices) / len(valid_prices)

场景2：API响应拼接
# 将API返回的数值型状态码与字符串描述结合
status_code = 404
response = "错误：" + str(status_code) + "（页面不存在）" """

""" 练习题
初级：
编写代码，将字符串"123"和"456"转换为整数后相加，结果转为字符串输出

中级：
用户输入两个数字字符串（可能含非数字字符），编写程序过滤无效输入后计算两数之和

高级：
给定混合类型列表data = ["5", 2.8, "3.14", True, None]，将其所有有效数值元素转换为浮点数后求和 """

def main(solution=1):
    if solution==1:
        str1="123"
        str2="456"
        str3=str(int(str1)+int(str2))
        print(str3)

    elif solution==2:
        str1=input("请输入一个含数字的字符串")
        str2=input("请输入一个含数字的字符串")
        num_list=['1','2','3','4','5','6','7','8','9','0','.']
        str_num1=""
        str_num2=""
        flag_zero=1
        flag_point=0
        for i in str1:
            if i in num_list:
                    str_num1+=i
        for i in str2:
            if i in num_list:
                str_num2+=i             
        str_num1=float(str_num1)
        str_num2=float(str_num2)
        print(f"去掉非数字部分的结果为{str_num2+str_num1}")   
        
    else:
        data = ["5", 2.8, "3.14", True, None]
        total = 0
        for item in data:
            try:
                total += float(item)
            except (TypeError, ValueError):
                continue
        print(total)

if __name__=="__main__":
    main(1)
    main(2)
    main(3)

