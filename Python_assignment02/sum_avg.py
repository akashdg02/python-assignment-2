def q13_sum_avg():
    count = int(input("How many numbers? "))
    nums = [float(input(f"Enter number {i+1}: ")) for i in range(count)]
    if nums:
        print(f"Sum: {sum(nums)} | Average: {sum(nums)/count}")
        print(f"Max: {max(nums)} | Min: {min(nums)}")