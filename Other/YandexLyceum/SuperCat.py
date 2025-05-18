def format_text_block(h, w, fn):
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return str(e)

    res = []
    cnt = 0

    for line in lines:
        if cnt >= h:
            break
        line = line.replace('\n', '')  
        chunks = [line[i:i + w] for i in range(0, len(line), w)]
        if not chunks:  
            chunks = ['']
        for ch in chunks:
            if cnt >= h:
                break
            res.append(ch)
            cnt += 1

    return '\n'.join(res)