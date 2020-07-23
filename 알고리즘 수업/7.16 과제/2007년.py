a, b = map(int, input().split())
print(("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN",)[(sum((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[:a-1]) + (b-1)) % 7])
