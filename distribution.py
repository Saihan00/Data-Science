from scipy.stats import stats

result = 1 - stats.binom.cdf(6,10,0.5)
print(result)