A transformer model is a type of deep learning model used primarily for natural language processing (NLP) tasks, such as machine translation, text generation, and language understanding. It was introduced in the 2017 paper "Attention is All You Need" by Vaswani et al.

The key innovation in transformer models is the self-attention mechanism, which allows the model to weigh the importance of different words in a sequence relative to each other, regardless of their position. This is in contrast to previous models like RNNs (Recurrent Neural Networks) or LSTMs (Long Short-Term Memory), which process input sequentially and struggle with long-range dependencies.


import torch
import torch.nn as nn

# Simple transformer model for text classification
class SimpleTransformer(nn.Module):
    def __init__(self, vocab_size, embed_size, num_heads, num_layers, num_classes):
        super(SimpleTransformer, self).__init__()
        
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.transformer = nn.Transformer(
            d_model=embed_size, 
            nhead=num_heads, 
            num_encoder_layers=num_layers, 
            num_decoder_layers=num_layers
        )
        self.fc = nn.Linear(embed_size, num_classes)
    
    def forward(self, src, tgt):
        # src: input sequence, tgt: target sequence (can be same for simplicity)
        src = self.embedding(src)  # [batch_size, seq_len, embed_size]
        tgt = self.embedding(tgt)  # [batch_size, seq_len, embed_size]
        
        # Transformer expects inputs in (seq_len, batch_size, embed_size)
        src = src.transpose(0, 1)
        tgt = tgt.transpose(0, 1)
        
        transformer_out = self.transformer(src, tgt)
        
        # We take the output from the last token
        output = transformer_out[-1, :, :]
        output = self.fc(output)
        
        return output

# Parameters
vocab_size = 10000  # Size of vocabulary (for example)
embed_size = 128  # Embedding size
num_heads = 8  # Number of attention heads
num_layers = 6  # Number of transformer layers
num_classes = 2  # Number of classes for classification (e.g., binary classification)

# Example input
src = torch.randint(0, vocab_size, (32, 10))  # 32 sequences of length 10 (batch_size, seq_len)
tgt = torch.randint(0, vocab_size, (32, 10))  # Target sequences for training

# Create model and forward pass
model = SimpleTransformer(vocab_size, embed_size, num_heads, num_layers, num_classes)
output = model(src, tgt)

print(output.shape)  # Output shape will be [batch_size, num_classes]
