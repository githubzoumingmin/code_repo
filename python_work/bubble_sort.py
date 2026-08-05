# bubble_sort.py
# 冒泡排序算法实现

def bubble_sort(arr):
    """
    对传入的列表进行冒泡排序（升序）
    参数:
        arr: 待排序的列表
    返回:
        排序后的列表（原地修改，同时返回引用）
    """
    n = len(arr)
    # 外层循环控制比较的轮数，最多 n-1 轮
    for i in range(n - 1):
        # 优化标志：如果某一轮没有发生交换，说明已经有序
        swapped = False
        # 内层循环进行两两比较，每轮结束后最大元素会“浮”到末尾
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换相邻元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果没有交换发生，提前结束排序
        if not swapped:
            break
    return arr


# 测试代码（当直接运行此脚本时执行）
if __name__ == "__main__":
    # 示例1：整数列表
    sample1 = [64, 34, 25, 12, 22, 11, 90]
    print("原始列表:", sample1)
    sorted_list = bubble_sort(sample1.copy())  # 使用副本保持原列表不变
    print("排序后列表:", sorted_list)

    # 示例2：已经有序的列表（测试优化效果）
    sample2 = [1, 2, 3, 4, 5]
    print("\n原始列表:", sample2)
    sorted_list2 = bubble_sort(sample2.copy())
    print("排序后列表:", sorted_list2)

    # 示例3：包含重复元素的列表
    sample3 = [5, 2, 8, 2, 9, 1, 5]
    print("\n原始列表:", sample3)
    sorted_list3 = bubble_sort(sample3.copy())
    print("排序后列表:", sorted_list3)