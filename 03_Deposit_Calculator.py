deposit_sum = float(input())
term_for_deposite = int(input())
year_percent = float(input()) / 100

total_sum = deposit_sum + term_for_deposite * ((deposit_sum * year_percent) / 12)

print(total_sum)