def production_time(amount, base=8):
    return base* (amount **0.8)

# 20 Frauen als Batch

def batch_gather(amount, base, gather_speed, eval_time):
    prod_time = production_time(amount, base)
    if eval_time < prod_time:
        return 0
    else:
        gather_time = eval_time - prod_time
        return gather_speed*gather_time*amount

# 20 Frauen einzeln
def single_gather(amount, base, gather_speed, eval_time):
    max_workers = min(int(eval_time/base), amount) # Anzahl der Arbeiter die bis zu diesem Zeitpunkt gebaut werden können
    total_gather = 0;
    for i in range(max_workers):
        remaining_time = eval_time - (i+1)*base;
        total_gather += remaining_time*gather_speed;
    return total_gather

from matplotlib import pyplot as plt
from numpy import arange


eval_time = 300
gather_speed = 0.7
amount = 30
base = 8

evals = arange(0,eval_time, 0.1)
plt.plot(evals, [batch_gather(amount, base, gather_speed, timestep) for timestep in evals], label="batch")
plt.plot(evals, [single_gather(amount, base, gather_speed, timestep) for timestep in evals], label="single")

plt.xlabel("time in s")
plt.ylabel("resources gathered")
plt.legend()
plt.show();




