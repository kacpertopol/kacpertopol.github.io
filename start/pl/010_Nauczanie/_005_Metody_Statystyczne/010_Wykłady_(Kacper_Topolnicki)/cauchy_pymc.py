#!/usr/bin/env python

from scipy.stats import cauchy
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt

observed = cauchy.rvs(size=256, loc=0.0, scale=2.0)

cauchy_model = pm.Model()
with cauchy_model:
    x0 = pm.Uniform("x0", lower=-10.0, upper=10.0)
    gamma = pm.Uniform("gamma", lower=0.0, upper=10)
    x = pm.Cauchy("x", alpha=x0, beta=gamma, observed=observed)
    idata = pm.sample()

az.plot_trace(idata)
plt.show()
