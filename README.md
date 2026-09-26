# LLM Fine-Tuning & Evaluation

Fine-tune a small open-source language model on a narrow task and **measure** whether it actually got better, with honest before/after numbers.

> **Status:** 🟡 Planning · Part of a 12-week ML engineering portfolio by [@mineenriquez](https://github.com/mineenriquez)

## Why this project

This project demonstrates hands-on experience **training, fine-tuning, and evaluating machine learning models**, not just calling an API.

## Goal

1. Pick a small open model (e.g. from the Hugging Face Hub) and a focused task.
2. Measure the **baseline** performance before any training.
3. Fine-tune the model (full fine-tuning or LoRA).
4. Measure again on a **held-out test set** and compare.
5. Write up what worked, what didn't, and why.

## Tech stack

- Python 3.10+
- PyTorch
- Hugging Face `transformers`, `datasets`, `peft` (LoRA), `evaluate`
- Google Colab or a local GPU
- Weights & Biases or TensorBoard for tracking training runs (optional)

## Plan

### Week 3: Setup & baseline
- [ ] Choose the task and dataset (and document why)
- [ ] Choose the base model (small enough to train on available hardware)
- [ ] Split the data into train / validation / test sets
- [ ] Write the evaluation script and choose the metric (accuracy, F1, exact match, etc.)
- [ ] Record the baseline score of the un-tuned model

### Week 4: Fine-tune & evaluate
- [ ] Write the training script with configurable hyperparameters
- [ ] Run the first fine-tuning job and log the loss curves
- [ ] Try at least one variation (learning rate, LoRA rank, or number of epochs)
- [ ] Evaluate every run on the same test set
- [ ] Look at 10–20 examples the model still gets wrong and group the error types

## Milestones

- [ ] Baseline measured
- [ ] First successful fine-tune
- [ ] Before/after comparison table complete
- [ ] Error analysis written
- [ ] README results section finished

## Planned repo structure

```
llm-finetuning-eval/
├── data/            # dataset download/prep scripts (no large files committed)
├── src/
│   ├── train.py
│   ├── evaluate.py
│   └── config.py
├── notebooks/       # exploration
├── results/         # metrics, charts
└── README.md
```

## Results

| Model | Setup | Test metric | Notes |
|---|---|---|---|
| Base (no tuning) | — | _TBD_ | |
| Fine-tuned v1 | _TBD_ | _TBD_ | |
| Fine-tuned v2 | _TBD_ | _TBD_ | |

## Lessons learned

_To be filled in as the project progresses._
