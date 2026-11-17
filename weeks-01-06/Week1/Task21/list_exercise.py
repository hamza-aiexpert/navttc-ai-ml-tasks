# Task 21 - List data type
nums = [10, 20, 30, 40, 50]
print("List:", nums, "| length:", len(nums))
print("Index/slice:", nums[0], nums[-1], nums[1:4], nums[::-1])

nums.append(60); nums.insert(0, 5); nums.extend([70, 80])
print("After append/insert/extend:", nums)
nums.remove(5); popped = nums.pop()
print("After remove/pop:", nums, "| popped", popped)

mixed = [3, 1, 4, 1, 5, 9, 2, 6]
print("count of 1:", mixed.count(1), "| index of 4:", mixed.index(4))
mixed.sort(); print("sorted:", mixed)
mixed.sort(reverse=True); print("reverse sorted:", mixed)

squares = [x ** 2 for x in range(1, 8)]
evens = [x for x in squares if x % 2 == 0]
print("squares:", squares, "| even squares:", evens)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("transpose:", [list(r) for r in zip(*matrix)])
a = [1, 2, 3]; b = a.copy(); b.append(4)
print("copy keeps original unchanged:", a, b)
print("max/min/sum:", max(nums), min(nums), sum(nums))
