def list_duplicates_of(lista, szukany_element):
    start_at = -1
    docelowa_lista = []
    while True:
        try:

            location = lista.index(szukany_element, start_at +1)
            print(location)
        except ValueError:
            break
        else:
            docelowa_lista.append(location)
            start_at = location
    return docelowa_lista


source_lista = "ABABDBAAEDSBQEWBAFLSAFB"

print(list_duplicates_of(source_lista, 'B'))
