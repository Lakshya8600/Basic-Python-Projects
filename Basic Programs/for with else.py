car = ["nano", "maruti suzuki", "duster"]

for cars in car:
    print(cars)

else : print("_______________without break____________")
print()

for cars in car:
    print(cars)
    if cars == "maruti suzuki":
        break

else : print("_______________with break____________")