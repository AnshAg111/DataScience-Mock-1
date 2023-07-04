def calculate_mean(numbers):
    count=len(numbers)
    total=sum(numbers)
    if len(numbers) == 0:
        return None
    else:
        return total / count 
numbers = [1, 2, 3, 4, 5]
mean = calculate_mean(numbers)
print(mean)
