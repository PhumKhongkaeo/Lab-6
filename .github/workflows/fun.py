def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# ทดสอบฟังก์ชัน
numbers = [1, 2, 3, 4, 5]
result = sum_of_list(numbers)
print("ผลรวมของตัวเลขในรายการคือ:", result)
