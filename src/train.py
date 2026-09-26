"""Fine-tune the base model on the task dataset.

Loads the train/validation splits and hyperparameters from config.py, then
runs full fine-tuning or LoRA (via peft), logging loss curves and saving
checkpoints for later evaluation.
"""
