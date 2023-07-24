```python
# Import necessary libraries
import numpy as np
import gflownet as gfn

# Define the Pragmatic Listener
def pragmaticListener(state, utterance, speaker):
    # Initialize the probability of the state given the utterance and speaker
    prob_state_given_utt_speaker = np.zeros_like(state)

    # For each possible state
    for i in range(len(state)):
        # Calculate the probability of the state given the utterance and speaker
        prob_state_given_utt_speaker[i] = speaker(state[i], utterance)

    # Normalize the probabilities
    prob_state_given_utt_speaker /= np.sum(prob_state_given_utt_speaker)

    return prob_state_given_utt_speaker
```