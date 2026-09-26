"""Evaluate a model on the held-out test set.

Scores both the un-tuned baseline and each fine-tuned run on the same test
split using the chosen metric (accuracy, F1, exact match, etc.), and writes
the metrics to results/ for the before/after comparison.
"""
