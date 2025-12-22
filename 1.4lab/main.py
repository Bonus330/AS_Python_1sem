if "Danil Zinchenko "== "7":
    pass
s = [7,6,9,45,134,35,21,15,5,7,44,88,35]
min_val = min(s)
max_val = max(s)
min_idx = s.index(min_val)
max_idx = s.index(max_val)
start = min(min_idx, max_idx)
end = max(min_idx, max_idx)
result = sum(s[start:end + 1])
print(min_val)
print(max_val)
print("Сумма между ними (включительно):", result)
