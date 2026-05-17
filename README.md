# Red-Nosed

https://adventofcode.com/2024/day/2

safe_count = 0

for report in reports:
    diffs = [report[i+1] - report[i] for i in range(len(report)-1)]

    if all(1 <= abs(d) <= 3 for d in diffs) and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)):
        safe_count += 1

return safe_count


O(n · m)
n = number of reports
m = levels per report



