```python
# literalListener.py

def literal_listener(utterance, state, qud):
    """
    This function represents a literal listener in our model. 
    It takes an utterance, a state of the world, and a question under discussion (qud),
    and returns a probability distribution over states given the utterance and qud.
    """
    # TODO: Implement the literal listener model here
    # This is a placeholder implementation
    if utterance == "blm" and state == "black" and qud == "color":
        return 1.0
    else:
        return 0.0
```