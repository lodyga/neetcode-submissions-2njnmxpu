import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List


class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        unique_words = {word 
                        for sentence in (positive + negative) 
                        for word in sentence.split()}

        word_id = {word: idx for idx,
                   word in enumerate(sorted(unique_words), 1)}

        pos = [torch.tensor([word_id[word] for word in sentence.split()]) 
               for sentence in positive]
        
        neg = [torch.tensor([word_id[word] for word in sentence.split()]) 
               for sentence in negative]
        
        return nn.utils.rnn.pad_sequence(pos + neg, batch_first=True)