# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())

recipes = []
for _ in range(n):
    recipe = tuple(map(int, input().split()))
    recipes.append(recipe)
    
questions = []
for _ in range(q):
    question = tuple(map(int, input().split()))
    questions.append(question)
    
recipe_prefix = [0] * (200000 + 2)   # 200000 is its constraint

for recipe in recipes:
    recipe_prefix[recipe[0]] += 1
    recipe_prefix[recipe[1] + 1] -= 1
    
for i in range(1, len(recipe_prefix)):
    recipe_prefix[i] += recipe_prefix[i - 1]
    
for i in range(len(recipe_prefix)):
    if recipe_prefix[i] >= k:
        recipe_prefix[i] = 1
    else:
        recipe_prefix[i] = 0

for i in range(1, len(recipe_prefix)):
    recipe_prefix[i] += recipe_prefix[i - 1]
    
for question in questions:
    count = recipe_prefix[question[1]] - recipe_prefix[question[0] - 1]
    print(count, sep="\n")