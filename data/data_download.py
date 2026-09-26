from datasets import load_dataset

# PolyAI/banking77 on the Hub is script-based, which datasets>=4 no longer supports.
BASE_URL = "https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets/master/banking_data"

dataset = load_dataset(
    "csv",
    data_files={"train": f"{BASE_URL}/train.csv", "test": f"{BASE_URL}/test.csv"},
)
dataset = dataset.rename_column("category", "label").class_encode_column("label")
dataset.save_to_disk("data/raw/banking77")
print(dataset)
