```python
import numpy as np

def speaker(state, qud):
    # Define the possible utterances
    utterances = ['blm', 'wlm', 'blw', 'wlw', 'b', 'w', 'l', 'm']

    # Define the cost of each utterance
    costs = np.array([1, 1, 2, 2, 1, 1, 1, 1])

    # Define the meaning function
    meanings = {
        'blm': lambda s: s == 'black',
        'wlm': lambda s: s == 'white',
        'blw': lambda s: s == 'black',
        'wlw': lambda s: s == 'white',
        'b': lambda s: s == 'black',
        'w': lambda s: s == 'white',
        'l': lambda s: s in ['black', 'white'],
        'm': lambda s: s in ['black', 'white']
    }

    # Compute the utility of each utterance
    utilities = np.array([meanings[utt](state) for utt in utterances]) - costs

    # Choose an utterance with probability proportional to exp(utility)
    probabilities = np.exp(utilities)
    probabilities /= probabilities.sum()
    return np.random.choice(utterances, p=probabilities)
```