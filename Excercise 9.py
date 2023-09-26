series = []

for i in range(1,51):
    if i <=2:
        series.append(i-1)
    else:
        series.append(series[i-1] + series[i-2])

series
