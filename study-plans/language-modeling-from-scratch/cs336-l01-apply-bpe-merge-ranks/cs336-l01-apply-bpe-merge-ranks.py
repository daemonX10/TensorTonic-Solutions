def encode(text: str, merges: list[list[int]]) -> list[int]:
    """
    Returns token IDs after applying the ordered merge rules.
    """
    raw_bytes = text.encode('utf-8')
    ids = []
    for byte_value in raw_bytes:
        ids.append(byte_value)

    for rule in merges:
        left_id = rule[0]
        right_id = rule[1]
        new_id = rule[2]

        output = []
        i = 0
        while i < len(ids):
            pair_found = False
            if i+1 < len(ids):
                if ids[i]==left_id and ids[i+1]==right_id:
                    pair_found =True
            if pair_found:
                output.append(new_id)
                i+=2
            else:
                output.append(ids[i])
                i+=1
        ids = output
    return ids

def decode(ids: list[int], vocab: dict[int, list[int]]) -> str:
    """
    Returns the text reconstructed from the token bytes.
    """
    all_bytes = []
    for token_ids in ids:
        token_bytes = vocab[token_ids]
        for byte_value in token_bytes:
            all_bytes.append(byte_value)
    text = bytes(all_bytes).decode('utf-8')
    return text
            
