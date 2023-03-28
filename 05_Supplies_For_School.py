pencils_count = int(input())
markers_count = int(input())
preparat_l = int(input())
discount = int(input()) / 100

total_pencils = pencils_count * 5.80
total_markers = markers_count * 7.20
total_preparat = preparat_l * 1.20
total_price = total_preparat + total_pencils + total_markers
price_with_discount = total_price - total_price * discount

print(price_with_discount)