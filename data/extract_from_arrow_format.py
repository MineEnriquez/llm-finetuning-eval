from pathlib import Path

from datasets import load_from_disk

ds = load_from_disk(Path(__file__).parent / "raw" / "banking77")
print(ds)                      # sizes of train and test

labels = ds["train"].features["label"].names
for ex in ds["train"].select(range(10)):
    print(labels[ex["label"]], "→", ex["text"])
    
ds["train"].to_csv(Path(__file__).parent / "raw" / "banking77" / "train.csv")
ds["test"].to_csv(Path(__file__).parent / "raw" / "banking77" / "test.csv")