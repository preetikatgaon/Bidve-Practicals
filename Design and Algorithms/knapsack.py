from random
import random
def build_item(n):
  res = []
for i in range(n):
  res.append((i, 1 + int(9 * random()), 1 + int(9 * random())))
return res
def powerset(items):
  res = [
    []
  ]
for item in items:
  newset = [r + [item]
    for r in res
  ]
res.extend(newset)
return res
def knapsack_value(item, max_weight):
  knapsack = []
best_weight = 0
best_value = 0
for item_set in powerset(item):
  set_weight = sum([e[1]
    for e in item_set
  ])
set_value = sum([e[2]
  for e in item_set
])
data = build_item(5)
if set_value > best_value and set_weight <= max_weight:
  best_value = set_value
best_weight = set_weight
knapsack = item_set
return knapsack, best_weight, best_value
n = 5
data = build_item(5)
print('computing', 2 ** n, 'powerset')
print('data', data)
max_w = 10
kn, opt_w, opt_v = knapsack_value(data, max_w)
print('knapsack', kn, opt_w, opt_v)