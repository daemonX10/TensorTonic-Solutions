def train_bpe(corpus: list[str], vocab_size: int) -> dict:
    """
    Returns a dictionary of learned vocab entries and ordered merges.
    """
    vocab = {}
    for i in range(256):
        vocab[i] = bytes([i])

    seqs = []
    for text in corpus:
        byte_values = text.encode('utf-8')
        seq = []
        for value in byte_values:
            seq.append(value)
        seqs.append(seq)

    merges = []
    next_id = 256

    while next_id < vocab_size:
        counts  = {}
        for seq in seqs:
            for i in range(len(seq)-1):
                pair = (seq[i],seq[i+1])
                counts[pair] = counts.get(pair,0)+1

        if len(counts)==0:
            break 

        best_pair = None
        best_count = 0

        for pair in counts:
            score = (counts[pair],vocab[pair[0]],vocab[pair[1]])
            if best_pair is None or score>best_score:
                best_pair = pair
                best_score = score

        a = best_pair[0]
        b = best_pair[1]

        vocab[next_id] = vocab[a] + vocab[b]

        new_seqs = []
        for seq in seqs:
            out = []
            i = 0 
            while i < len(seq):
                is_last = (i==len(seq)-1)
                if not is_last and seq[i] ==a and seq[i+1]==b:
                    out.append(next_id)
                    i+=2
                else:
                    out.append(seq[i])
                    i+=1
            new_seqs.append(out)
        seqs = new_seqs

        merges.append([a,b,next_id])
        next_id +=1

    learned = []

    for i in range(256,next_id):
        learned.append([i,list(vocab[i])])

    return { "vocab" : learned , "merges": merges}
        

        
    
    
    
