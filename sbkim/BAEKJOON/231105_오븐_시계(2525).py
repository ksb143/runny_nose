c_hour, c_minute = map(int, input().split())

cooking_time = int(input())

cooking_hour = cooking_time // 60
cooking_minute = cooking_time % 60

completion_minute = (c_minute + cooking_minute) % 60
cooking_hour += (c_minute + cooking_minute) // 60

completion_hour = (c_hour + cooking_hour) % 24

print(completion_hour, completion_minute)