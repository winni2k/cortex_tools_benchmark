import io
import itertools
import random

import pytest
from cortexpy.graph.parser import RandomAccess
from cortexpy.graph.parser.streaming import (
    kmer_string_generator_from_stream
)

CHROM_GRAPH_1KB = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
CHROM_GRAPH_2KB = 'fixtures/yeast/NC_001133.9.2kbp.ctx'
CHROM_GRAPH_4KB = 'fixtures/yeast/NC_001133.9.4kbp.ctx'
INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'


def random_access_kmers(ra, kmer_strings):
    for kmer_string in kmer_strings:
        ra[kmer_string]


GRAPHS = {
    '1kb': CHROM_GRAPH_1KB,
    '2kb': CHROM_GRAPH_2KB,
    '4kb': CHROM_GRAPH_4KB
}

CACHE_SIZE = [0, 1024, 2048, 4096]



@pytest.mark.parametrize('graph_size,cache_size',
                         itertools.product(GRAPHS.keys(), CACHE_SIZE))
def test_graph_parser_ra_kmers(benchmark, graph_size, cache_size):
    graph = GRAPHS[graph_size]
    buffer = io.BytesIO(open(graph, 'rb').read())
    kmer_strings = [string for string in kmer_string_generator_from_stream(buffer)]
    random.shuffle(kmer_strings)
    ra = RandomAccess(buffer, kmer_cache_size=cache_size)
    benchmark(random_access_kmers, ra, kmer_strings)
