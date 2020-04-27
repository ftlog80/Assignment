# %%
i = 1
f_numbers = [1]
while i < 56:
    f_numbers.append(i)
    i += f_numbers[-2]
print(f_numbers)

# %%
