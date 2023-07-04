from scipy.stats import ttest_ind

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = ttest_ind(sample1, sample2)
    return p_value
sample1 = [10, 20, 30, 40, 50]
sample2 = [60, 70, 80, 90, 100]
p_value = perform_hypothesis_test(sample1, sample2)
print(p_value)
