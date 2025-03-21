#Ryan Bendelson, Liam Booth, and Joe Thatcher Code
import numpy as np #Import numpy as np
from scipy.stats import binom
from scipy.integrate import trapezoid
#python -m pip install -U pip
#python -m pip install -U matplotlib
import matplotlib.pyplot as plt #Run above two comment lines in Anaconda Prompt before running this script

print("Question 2 Answer: See the \"Eraser Posterior Distribution\" generated graphs/plots (The non-uniform prior plot skews less to the right and has a higher peak.)")

# Subdivision size for spaceof success probabilities
N = 1000

# Sample the space of success probabilities from 1/dp evenly spaced pieces of [0,1]
p_grid = np.linspace(0, 1, N)

# The prior distribution is uniform; so we define it as an array of 1's
prior = np.ones(1000)

# Plotting
## Instantiate a plot of the prior distribution (plt.plot(x-values,y-values))
plt.plot(p_grid, prior)
## Label axes and create title and display
plt.xlabel("p (Probability of Success)")
plt.ylabel("Probability Density")
plt.title("Prior Distribution")
## Display the plot!
plt.show()

# Number of successes/heads for coin flip: change these values!
num_success_coin = 1
# Number of trials
num_trials_coin = 1

# Likelihoods: P(Data| Model(p))
# Here Data = {num_success, num_trials} and Model(p) is the binomial distribution
# with parameter p. The likelihood is a function of p.
likelihood_coin = binom.pmf(num_success_coin, n=num_trials_coin, p=p_grid)

# The posterior distribution is proportional to the prior distribution times the likelihood
posterior_coin_unnormalized = likelihood_coin * prior

# Normalize the posterior distribution so that the area under its curve is 1
# trapezoid(distribution, x-values) computes the area under the distribution
posterior = posterior_coin_unnormalized/trapezoid(posterior_coin_unnormalized, p_grid)

# Plotting
plt.plot(p_grid, posterior, label='Posterior', color='blue')
plt.plot(p_grid, prior, 'r--', label='Prior')
plt.xlabel('p (Probabability of Success')
plt.ylabel('Probability Density')
plt.title('Posterior Distribution')
plt.legend()
plt.show()

#Question 2 Answer: See the "Eraser Posterior Distribution" generated graphs/plots (The non-uniform prior plot skews less to the right and has a higher peak.)
'''
For the eraser: after looking at the posterior distribution assuming a uniform prior, try using the posterior distribution from your coin flips as the new prior, what has changed?
'''
uPrior = posterior

# Number of successes/heads for coin flip: change these values!
num_success_coin = 25 #Times eraser lands white side up
# Number of trials
num_trials_coin = 38 #Times eraser was flipped

# Likelihoods: P(Data| Model(p))
# Here Data = {num_success, num_trials} and Model(p) is the binomial distribution
# with parameter p. The likelihood is a function of p.
likelihood_coin = binom.pmf(num_success_coin, n=num_trials_coin, p=p_grid)

# The posterior distribution is proportional to the prior distribution times the likelihood
posterior_coin_unnormalized = likelihood_coin * uPrior

# Normalize the posterior distribution so that the area under its curve is 1
# trapezoid(distribution, x-values) computes the area under the distribution
posterior = posterior_coin_unnormalized/trapezoid(posterior_coin_unnormalized, p_grid)

# Plotting
plt.plot(p_grid, posterior, label='Eraser Posterior', color='blue')
plt.plot(p_grid, uPrior, 'r--', label='Uniform Prior')
plt.xlabel('p (Probabability of Success')
plt.ylabel('Probability Density')
plt.title('Eraser Posterior Distribution')
plt.legend()
plt.show()

# Number of successes/heads for coin flip: change these values!
num_success_coin = 19 #Times coin flip results in heads
# Number of trials
num_trials_coin = 36 #Times coin was flipped

# Likelihoods: P(Data| Model(p))
# Here Data = {num_success, num_trials} and Model(p) is the binomial distribution
# with parameter p. The likelihood is a function of p.
likelihood_coin = binom.pmf(num_success_coin, n=num_trials_coin, p=p_grid)

# The posterior distribution is proportional to the prior distribution times the likelihood
posterior_coin_unnormalized = likelihood_coin * uPrior

# Normalize the posterior distribution so that the area under its curve is 1
# trapezoid(distribution, x-values) computes the area under the distribution
cPrior = posterior_coin_unnormalized/trapezoid(posterior_coin_unnormalized, p_grid)

# Number of successes/heads for coin flip: change these values!
num_success_coin = 25 #Times eraser lands white side up
# Number of trials
num_trials_coin = 38 #Times eraser was flipped

# Likelihoods: P(Data| Model(p))
# Here Data = {num_success, num_trials} and Model(p) is the binomial distribution
# with parameter p. The likelihood is a function of p.
likelihood_coin = binom.pmf(num_success_coin, n=num_trials_coin, p=p_grid)

# The posterior distribution is proportional to the prior distribution times the likelihood
posterior_coin_unnormalized = likelihood_coin * cPrior

# Normalize the posterior distribution so that the area under its curve is 1
# trapezoid(distribution, x-values) computes the area under the distribution
posterior = posterior_coin_unnormalized/trapezoid(posterior_coin_unnormalized, p_grid)

# Plotting
plt.plot(p_grid, posterior, label='Eraser Posterior', color='blue')
plt.plot(p_grid, cPrior, 'r--', label='Coin Flip Prior')
plt.xlabel('p (Probabability of Success')
plt.ylabel('Probability Density')
plt.title('Eraser Posterior Distribution')
plt.legend()
plt.show()
