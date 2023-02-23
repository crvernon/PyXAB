from PyXAB.synthetic_obj import *

from PyXAB.algos.VPCT import VPCT
from PyXAB.algos.HCT import HCT
from PyXAB.algos.GPO import GPO
from PyXAB.partition.BinaryPartition import BinaryPartition
from PyXAB.utils.plot import compare_regret
import numpy as np

T = 100
Target = Garland.Garland()
domain = [[0, 1]]
partition = BinaryPartition
algo = VPCT(rounds=T, domain=domain, partition=partition)


VPCT_regret_list = []
regret = 0


for t in range(1, T + 1):
    # T-HOO
    point = algo.pull(t)
    reward = Target.f(point) + np.random.uniform(-0.1, 0.1)
    algo.receive_reward(t, reward)
    inst_regret = Target.fmax - Target.f(point)
    regret += inst_regret
    VPCT_regret_list.append(regret)


# plot the regret
# regret_dic = {"VPCT": np.array(VPCT_regret_list)}
# compare_regret(regret_dic)