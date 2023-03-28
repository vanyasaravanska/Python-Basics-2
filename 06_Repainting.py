nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_total = (nylon + 2) * 1.5
paint_total = (paint * 1.1) * 14.5
thinner_total = thinner * 5
bags_total = 0.4
material_total = nylon_total + paint_total + thinner_total + bags_total
work_total = material_total * 0.3 * hours

total_cost = material_total + work_total

print(f"{total_cost:.2f}")