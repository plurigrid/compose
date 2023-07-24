```python
# statePrior.py

def statePrior():
    # Define the possible states of the world
    states = ['black', 'white', 'both', 'neither']
    
    # Define the prior probabilities for each state
    prior_probabilities = [0.25, 0.25, 0.25, 0.25]
    
    # Return a dictionary mapping states to their prior probabilities
    return dict(zip(states, prior_probabilities))
```