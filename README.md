"""# data-and-prompt-injection-poc 
This repo contains two POC scripts:
1. Data Poisoning: How injecting mislabeled training data can subvert a classifier.
2. Prompt Injection: How adversarial inputs can override system prompts in an LLM wrapper.

Files
-'data_poisoning_poc.py' : Trains a simple classifier on Iris dataset with and without poisoning.
-'prompt_injection_poc.py' : Demonstrates prompt injcetion against a naive LLM API wrapper.

Requirements
pip install scikit-learn numpy openai

"""