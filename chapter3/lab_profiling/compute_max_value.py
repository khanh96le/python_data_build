import numpy as np
from numpy.linalg import eigvals

def run_experiment(nilter = 100):
    k = 100
    results = [ ]
    for _ in xrange(nilter):
        mat = np.random.randn(k, k)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results

some_result = run_experiment()
print 'Largest one we saw: %s' % np.max(some_result)


