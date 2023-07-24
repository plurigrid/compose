# qudPrior.py

```python
# Define the prior for the question under discussion (QUD)
def qudPrior():
    # Possible QUDs: 'color', 'shape', 'both', 'neither'
    quds = ['color', 'shape', 'both', 'neither']
    
    # Uniform prior over QUDs
    qud_probs = [1/len(quds) for _ in quds]
    
    # Return a random QUD based on the probabilities
    return np.random.choice(quds, p=qud_probs)
```