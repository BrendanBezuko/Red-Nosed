def check_report(r):
    diffs = []
    for i in range(len(r) - 1):
        diffs.append(r[i + 1] - r[i])

    return (
        all(1 <= abs(d) <= 3 for d in diffs) and
        (all(d > 0 for d in diffs) or all(d < 0 for d in diffs))
    )


def total_safe(reports):
    return sum(check_report(r) for r in reports)


reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

print(total_safe(reports))
