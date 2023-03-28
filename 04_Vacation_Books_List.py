pages = int(input())
pages_for_1_hour = int(input())
total_days = int(input())

total_time_needed = pages // pages_for_1_hour
pages_day = total_time_needed // total_days

print(pages_day)

