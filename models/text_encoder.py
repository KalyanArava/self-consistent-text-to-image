import torch
from transformers import BertTokenizer, BertModel


class TextEncoder:
    """
    Explicit BERT-based text encoder
    """

    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained(
            "bert-base-uncased"
        )
        self.model = BertModel.from_pretrained(
            "bert-base-uncased"
        )

    def encode(self, text: str):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=32
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        embedding = outputs.last_hidden_state.mean(dim=1)
        return embedding
