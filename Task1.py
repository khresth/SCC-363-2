def Task1(a, b, c, point1, number_set, prob_set, num, point2, mu, sigma, xm, alpha, point3, point4):
    if point1 <= a:
        prob1 = 0
    elif point1 >= b:
        prob1 = 1
    elif point1 <= c:
        prob1 = ((point1 - a)**2) / ((b - a) * (c - a))
    else:
        prob1 = 1 - ((b - point1)**2) / ((b - a) * (b - c))

    MEAN_t = (a + b + c) / 3
    if c >= (a + b) / 2:
        MEDIAN_t = a + np.sqrt((b - a) * (c - a) / 2)
    else:
        MEDIAN_t = b - np.sqrt((b - a) * (b - c) / 2)

    MEAN_d = sum(n * p for n, p in zip(number_set, prob_set))
    VARIANCE_d = sum(p * (n - MEAN_d)**2 for n, p in zip(number_set, prob_set))

    flaw_A = stats.lognorm.rvs(s=sigma, scale=np.exp(mu), size=num)
    flaw_B = stats.pareto.rvs(alpha, scale=xm, size=num)
    total_impact = flaw_A + flaw_B

    prob2 = np.mean(total_impact > point2)
    prob3 = np.mean((total_impact > point3) & (total_impact < point4))

    SLE = MEDIAN_t * prob2
    ALE = MEAN_d * SLE

    return (prob1, MEAN_t, MEDIAN_t, MEAN_d, VARIANCE_d, prob2, prob3, ALE)
