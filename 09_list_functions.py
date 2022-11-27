lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)
friends.extend(lucky_numbers)

friends.append("Creed")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.pop()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends.index("Kevin"))

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

friends.sort()
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)

lucky_numbers2 = lucky_numbers.copy
print(lucky_numbers2)
