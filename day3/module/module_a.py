def func_a():
    from module_b import func_b  # 延迟导入
    print("Function A calling:")
    return func_b()

def helper():
    return "Helper from A"