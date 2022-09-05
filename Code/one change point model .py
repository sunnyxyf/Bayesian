from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
from collections import Counter
import numpy as np
import pandas as pd
import pymc3 as pm
import csv


a = pd.read_csv('all ATSS events.csv')
np.save('all ATSS events.npy', a)
data1 = np.load('all ATSS events.npy', allow_pickle=True)
for line in data1:
    line_1 = np.matrix(line)
    data = line_1.reshape(19, 16)
    data = data.astype(np.float64)

    x = np.mean(data)
    y = np.var(data)
    canshu = x + y
    data_count = np.mean(data, axis=0).tolist()

    if __name__ == '__main__':
        with pm.Model() as model:

            U_1 = pm.Uniform('alpha_1 /(alpha_1+beta_1)', 0, 1)
            V_1 = pm.Gamma('alpha_1+beta_1', 1, canshu)
            U_2 = pm.Uniform('alpha_2 / (alpha_2 + beta_2)', 0, 1)
            V_2 = pm.Gamma('alpha_2+beta_2', 1, canshu)
            tau = pm.DiscreteUniform('tau', lower=0, upper=15)

            alpha_1 = pm.Deterministic('alpha_1', U_1 * V_1)
            alpha_2 = pm.Deterministic('alpha_2', U_2 * V_2)
            beta_1 = pm.Deterministic('beta_1', (1 - U_1) * V_1)
            beta_2 = pm.Deterministic('beta_2', (1 - U_2) * V_2)

            with model:
                idx = np.arange(16)
                lambda_1 = pm.math.switch(tau >= idx, alpha_1, alpha_2)
                lambda_2 = pm.math.switch(tau >= idx, beta_1, beta_2)
            with model:
                observation = pm.Beta('obs', lambda_1, lambda_2, observed=data)

            with model:
                step = pm.NUTS()
                start = pm.find_MAP()
                trace = pm.sample(5000, tune=5000, step=step, start=start)

                alpha_1_samples = trace['alpha_1']
                alpha_2_samples = trace['alpha_2']
                beta_1_samples = trace['beta_1']
                beta_2_samples = trace['beta_2']
                tau_samples = trace['tau']

        result = Counter(tau_samples)
        for m in range(16):
            if m not in result.keys():
                result[m] = 0
        zuihzong_result = sorted(result.keys(), reverse=False)

        datas = []
        header = zuihzong_result
        datas.append(result)
        with open('one change point result.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(datas)

