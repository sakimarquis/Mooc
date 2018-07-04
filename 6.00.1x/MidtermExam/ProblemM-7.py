def McNuggets(n):
    for a in range(n/6+2):
        for b in range(n/9+2):
            for c in range(n/20+2):
                if 6*a + 9*b + 20*c == n:
                    return True
    return False

print McNuggets(28)

