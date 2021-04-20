from numpy.random import default_rng
from fitting.crossvalidation import frrsa

# Specify a seed for reproducible results.
rng = default_rng(seed=4)

n_units = 100 # How many measurement channels?
n_objects = 100 # How many objects aka conditions?
n_outputs = 2 # How many different outputs?

# Simulate output and inputs.
output = rng.integers(low=0, high=100, size=(n_objects,n_objects,n_outputs))
inputs = rng.integers(low=0, high=100, size=(n_units,n_objects))


#%% Call the main funtion.
outer_k = 2
outer_reps = 3
splitter = 'random'
hyperparams = None
score_type = 'pearson'
rng_state = None
sanity = False
parallel = True

predicted_RDM, predictions, unfitted_scores, crossval, betas, fitted_scores = frrsa(output,
                                                                                        inputs, 
                                                                                        outer_k, 
                                                                                        outer_reps, 
                                                                                        splitter, 
                                                                                        hyperparams, 
                                                                                        score_type, 
                                                                                        sanity=sanity, 
                                                                                        rng_state=rng_state,
                                                                                        parallel=parallel)


#%% End of script