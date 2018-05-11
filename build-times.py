data1 = [8,14,20,25,29,34,38,43,47,51,55,59,63,67,70,74,78,81,85,88,92,95,99,102,106,109,112,116,119,122,125,129,132,135,138,141,144,147,150,154,157]
positions1 = [i for i in range(1,42)]
data5 = [29,51,70,88,106,122,138,154,169,183,198,212,226,240,254,267,280,293,306,319] # ab 8
positions5 = [i for i in range(5,101,5)]
data10 = [319,344,369,393,417,441,464,487,510,533,555,577,599,621,642,663,685,705,726,747,767] #ab 1
positions10 = [i for i in range(100,301,10)]
time_per_unit = []
increase_per_unit = []
data = data1 + data5[8:] + data10[1:]
positions = positions1 + positions5[8:] + positions10[1:]
print(len(data1), len(positions1))
print(len(data5), len(positions5))
print(len(data10), len(positions10))

print(data)
print(positions)

#time_per_unit.append(data1[0])
#increase_per_unit.append(0)

for index, value in enumerate(data):
    step = positions[index] - positions[index-1] if index > 0 else 1
    increase_per_unit.append((data[index] - data[index-1])/step if index > 0 else 0)
    time_per_unit.append(value/positions[index])
print("time_per_unit:", time_per_unit)
print("increase:", increase_per_unit)

from matplotlib import pyplot

#pyplot.plot(data)
pyplot.plot(positions, time_per_unit, label="time per unit")
pyplot.plot(positions, increase_per_unit, label="time increase per unit")
pyplot.plot(positions, [8*n**(-0.2) for n in positions], label = "what the code says")

pyplot.xlabel("batch size")
pyplot.ylabel("time in s")

pyplot.legend()

pyplot.show();

