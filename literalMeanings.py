# literalMeanings.py

```python
def literal_meanings(utterance):
    """
    This function maps utterances to their literal meanings.
    """
    meanings = {
        "blm": "The object is black",
        "wlm": "The object is white",
        "blm_wlm": "The object is both black and white",
        "nlm": "The object is neither black nor white"
    }
    return meanings.get(utterance, "Unknown utterance")

literalMeanings = literal_meanings
```