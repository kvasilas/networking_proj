import numpy as np
x = np.loadtxt(r'C:\Users\USER\Documents\coding\projects\networking_proj\density_monitor\data\numbers.txt',
               delimiter=",", unpack=False)

print(type(x))


avgs = []
hour_start = 0
hour_sum = 0
for j in range(0,24,1):
    for i in range(hour_start,169,24):
        hour_sum += x[i]
        #print(i)
    hour_sum /= 7
    avgs.append(hour_sum)
    hour_start += 1
    hour_sum = 0

#np.asarray(avgs)
print(type(np.asarray(avgs)))
