import torch
import math

def attention_scores(q: torch.Tensor, k: torch.Tensor, num_heads: int) -> torch.Tensor:
    """
    Returns scores of shape (batch, heads, query_length, key_length).
    """
    # size from shape
    batch_size = q.shape[0]
    query_len = q.shape[1]
    key_len = k.shape[1]
    model_width = q.shape[2]
    head_width = model_width//num_heads

    # ( B,S,H,d_h)
    q_split = torch.reshape(q,(batch_size,query_len,num_heads,head_width))
    k_split = torch.reshape(k,(batch_size,key_len,num_heads,head_width))

    q_head = torch.transpose(q_split,1,2)
    k_head = torch.transpose(k_split,1,2)

    raw_scores = torch.einsum("bhid,bhjd->bhij",q_head,k_head)
    scores = raw_scores/math.sqrt(head_width)

    return scores
    
