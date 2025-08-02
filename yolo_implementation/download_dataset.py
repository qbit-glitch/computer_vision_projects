from datasets import load_dataset

dataset = load_dataset("merve/pascal-voc")

# or load the separate splits if the dataset has train/validation/test splits
train_dataset = load_dataset("merve/pascal-voc", split="train")
valid_dataset = load_dataset("merve/pascal-voc", split="validation")
test_dataset  = load_dataset("merve/pascal-voc", split="test")
