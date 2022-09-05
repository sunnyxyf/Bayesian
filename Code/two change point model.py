from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
from collections import Counter
import numpy as np
import pandas as pd
import pymc3 as pm
import csv

a= pd.read_csv('two change points ATSS events.csv')
np.save('two change points ATSS events.npy',a)
data1 = np.load('two change points ATSS events.npy',allow_pickle=True)
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
            U_3 = pm.Uniform('alpha_3 / (alpha_3 + beta_3)', 0, 1)
            V_3 = pm.Gamma('alpha_3+beta_3', 1, canshu)

            tau1 = pm.DiscreteUniform("tau1", lower=0, upper=14)
            tau2 = pm.DiscreteUniform("tau2", lower=tau1, upper=15)

            alpha_1 = pm.Deterministic('alpha_1', U_1 * V_1)
            alpha_2 = pm.Deterministic('alpha_2', U_2 * V_2)
            alpha_3 = pm.Deterministic('alpha_3', U_3 * V_3)
            beta_1 = pm.Deterministic('beta_1', (1 - U_1) * V_1)
            beta_2 = pm.Deterministic('beta_2', (1 - U_2) * V_2)
            beta_3 = pm.Deterministic('beta_3', (1 - U_3) * V_3)

            with model:
                idx = np.arange(16)
                lambda_temp = pm.math.switch(tau1 >= idx, alpha_1, alpha_2)
                lambda_1 = pm.math.switch(tau2 >= idx, lambda_temp, alpha_3)
                lambda_temp1 = pm.math.switch(tau1 >= idx, beta_1, beta_2)
                lambda_2 = pm.math.switch(tau2 >= idx, lambda_temp1, beta_3)


            with model:
                observation = pm.Beta('obs', lambda_1, lambda_2, observed=data)

            with model:
                step = pm.NUTS()
                start = pm.find_MAP()
                trace = pm.sample(5000, tune=5000, step=step,start = start)

                alpha_1_samples = trace['alpha_1']
                alpha_2_samples = trace['alpha_2']
                alpha_3_samples = trace['alpha_3']
                beta_1_samples = trace['beta_1']
                beta_2_samples = trace['beta_2']
                beta_3_samples = trace['beta_3']
                tau1_samples = trace['tau1']
                tau2_samples = trace['tau2']


        result1 = Counter(tau1_samples)
        result2 = Counter(tau2_samples)
        result = Counter(result1+result2)

        for m in range(16):
            if m not in result.keys():
                result[m] = 0
        zuihzong_result = sorted(result.keys(), reverse=False)

        datas = []
        header = zuihzong_result
        datas.append(result)
        with open('two change point result.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(datas)




