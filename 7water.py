def water_jug(jug1, jug2, target):
    visited = set()
    queue = [(0, 0)]
    while queue:
        a, b = queue.pop(0)
        if (a, b) in visited:
            continue
        print(f"({a}, {b})")
        if a == target or b == target:
            return (a, b)
        visited.add((a, b))
        queue.extend([
            (jug1, b), (a, jug2),
            (0, b), (a, 0),
            (min(jug1, a + b), a + b - min(jug1, a + b)),
            (a + b - min(jug2, a + b), min(jug2, a + b))
        ])
    return None

# Example usage
jug1, jug2, target = 4, 3, 2
print("Solution:", water_jug(jug1, jug2, target))