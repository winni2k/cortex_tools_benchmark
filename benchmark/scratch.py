LETTERS = list('ACGT')


def test_string_join(benchmark):
    the_list = list(LETTERS[i % 4] for i in range(100))
    benchmark(''.join, the_list)


def test_tuple_convert(benchmark):
    the_list = list(LETTERS[i % 4] for i in range(100))
    benchmark(tuple, the_list)

def test_split(benchmark):
    the_string = ''.join(LETTERS[i % 4] for i in range(100))
    benchmark(list, the_string)
