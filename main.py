def birlashtir_roxat(roxat1, roxat2):
    return list(set(roxat1 + roxat2))

print(birlashtir_roxat([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5]
