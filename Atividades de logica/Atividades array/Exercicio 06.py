num = [""]*5
for i in range(5):
    num[i] = input(f"Digite {i+1}° numero")

print(sorted(num, reverse= True))