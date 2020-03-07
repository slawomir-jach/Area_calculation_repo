def list_duplicates_of(seq, item):
    start_at = -1
    list = []
    while True:
        try:
            loc = seq.index(item, start_at+1)
        except ValueError:
            break
        else:
            list.append(loc)
            start_at = loc
    return list

source = "ABABDBAAEDSBQEWBAFLSAFB"
print(list_duplicates_of(source, 'B'))