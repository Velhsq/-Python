def my_func(doc: str):
    with open(doc, 'r', encoding='utf-8') as document:
        doc_list = document.readlines()
        word_count = dict()
        count = 1
        for i in doc_list:
            word_count.update({count: len(i)})
            count += 1

        print(f'количество строк: {len(doc_list)}')
        print(word_count)

my_func('HW5.2.txt')