def func_b():
    from module_a import helper  # 延迟导入
    print("Function B using:")
    return helper()

if __name__=="__main__":
    func_b()