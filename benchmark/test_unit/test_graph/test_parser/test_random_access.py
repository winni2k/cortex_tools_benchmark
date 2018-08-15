import io
import random
from itertools import product

import pytest

from cortexpy.graph.parser.random_access import RandomAccess
from cortexpy.graph.parser.streaming import (
    kmer_string_generator_from_stream
)

CHROM_GRAPH = 'fixtures/yeast/NC_001133.9.ctx'
CHROM_GRAPH_1KB = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
# CHROM_GRAPH_2KB = 'fixtures/yeast/NC_001133.9.2kbp.ctx'
CHROM_GRAPH_4KB = 'fixtures/yeast/NC_001133.9.4kbp.ctx'
CHROM_GRAPH_16KB = 'fixtures/yeast/NC_001133.9.4kbp.ctx'
INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'
random.seed(42)


def stream_kmer_strings(buffer, cache_size):
    ra = RandomAccess(buffer, kmer_cache_size=cache_size)
    for kmer_string in ra:
        pass


def stream_kmers(buffer, cache_size):
    ra = RandomAccess(buffer, kmer_cache_size=cache_size)
    for kmer in ra.values():
        kmer.kmer


def random_access_kmers(buffer, cache_size, kmer_strings):
    ra = RandomAccess(buffer, kmer_cache_size=cache_size)
    for kmer_string in kmer_strings:
        kmer = ra[kmer_string]
        kmer.kmer


def random_access_single_kmer(ra, kmer_string):
    ra[kmer_string]


GRAPHS = {
    '1kb': (CHROM_GRAPH_1KB, 1024),
    '4kb': (CHROM_GRAPH_4KB, 4096),
    '16kb': (CHROM_GRAPH_16KB, 16384),
}

ALL_GRAPHS = GRAPHS.copy()
ALL_GRAPHS['all'] = (CHROM_GRAPH, 262144)


@pytest.mark.parametrize('graph_size,cached',
                         product(GRAPHS.keys(), ['cache', 'nocache']))
def test_graph_parser_ra_kmers(benchmark, graph_size, cached):
    graph_info = GRAPHS[graph_size]
    buffer = io.BytesIO(open(graph_info[0], 'rb').read())
    kmer_strings = [string for string in kmer_string_generator_from_stream(buffer)]
    random.shuffle(kmer_strings)
    if cached == 'cache':
        cache_size = graph_info[1]
    elif cached == 'nocache':
        cache_size = 0
    else:
        raise Exception()
    benchmark.pedantic(random_access_kmers, args=(buffer, cache_size, kmer_strings), rounds=3,
                       warmup_rounds=1)


@pytest.mark.parametrize('graph_size,cached',
                         product(ALL_GRAPHS.keys(), ['cache', 'nocache']))
def test_graph_parser_ra_kmers_single(benchmark, graph_size, cached):
    graph_info = ALL_GRAPHS[graph_size]
    buffer = io.BytesIO(open(graph_info[0], 'rb').read())
    kmer_string = next(kmer_string_generator_from_stream(buffer))
    if cached == 'cache':
        cache_size = graph_info[1]
    elif cached == 'nocache':
        cache_size = 0
    else:
        raise Exception()
    ra = RandomAccess(buffer, kmer_cache_size=cache_size)
    ra[kmer_string]
    benchmark(random_access_single_kmer, ra, kmer_string)


@pytest.mark.parametrize('graph_size,cached,stream_func',
                         product(GRAPHS.keys(), ['cache', 'nocache'],
                                 [stream_kmer_strings, stream_kmers]))
def test_graph_parser_ra_iter(benchmark, graph_size, cached, stream_func):
    graph_info = GRAPHS[graph_size]
    buffer = io.BytesIO(open(graph_info[0], 'rb').read())
    if cached == 'cache':
        cache_size = graph_info[1]
    elif cached == 'nocache':
        cache_size = 0
    else:
        raise Exception()
    benchmark.pedantic(stream_func, args=(buffer, cache_size), rounds=3,
                       warmup_rounds=1)
