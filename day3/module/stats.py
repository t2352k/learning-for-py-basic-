def calculate_avg(lis):
    n=len(lis)
    avg=sum(lis)/n*1.0
    return avg

if __name__=="__main__":
    lis=[12,43.5,22,77,1.09]
    print(calculate_avg(lis))