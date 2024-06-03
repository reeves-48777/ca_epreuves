def generate_numbers():
    res = list()
    for i in range(100):
        for j in range(100):
            if i < j:
                res.append(f"{i:02} {j:02}")
    return ", ".join(res)

print(generate_numbers())