PLAN:
=====
- TASK: banking customer intent classification. 
     - for example:  "I lost my card"  =>   lost_or_stolen_card
- DATASET:  Banking77 or Hugging Face. It has about 13,000 real customer messages across 77 intents, the labels are clear and there's  a built-in test split, which makes before/after results easy to measure
- MODEL:  a small instrucion-tuned model under 1N parameters, such as Qwen2.5*0.5B-Instruct or SmolLM2-360M-Instruct. Check the Hugging Face Hub for newer small models too. Models rhis size train quickly on free Colab or a Mac.
- METRIC: accuracy, meaning the percentage of messages where the model outputs the exact correct intent.

SETUP:
======
 
- Set up the environment :
```  
   python3 -m venv .venv
   source .venv/bin/activate
   pip install torch transformers datasets peft evaluate accelerate
```
- Check your hardware. On an Apple Silicon Mac, run 
```
   python -c "import torch; print(torch.backends.mps.is_available())". 
```
If it prints True, you can train locally. If not, use Google Colab with a free GPU.
- Explore the data in a notebook (notebooks/01_explore.ipynb). Load Banking77, look at 20 examples, count examples per intent, and note any confusing or similar intents.
- Write down your decisions in the README's "Goal" section: which task, dataset, model, and metric you chose, and why. Commit and push.