lines = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
times, tot = [], 0

for line in lines:
    l = line.split()
    hh,mm,ss = l[1].split(":")
    end = int(hh)*60*60 + int(mm)*60 + float(ss)
    start = end - float(l[2][0:-1]) + 0.001
    times.append([end,start])

times = sorted(times)


for time in times: # 주체
    cnt = 0
    for time2 in times:
        if time2[0] >= time[0] and time2[1] < time[0] + 1:
            cnt += 1
    tot = max(tot,cnt)
print(tot)
