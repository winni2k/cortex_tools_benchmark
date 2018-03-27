import io
import itertools
import pytest
from cortexpy.graph.parser.streaming import kmer_generator_from_stream

CHROM_GRAPH_1KB = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
CHROM_GRAPH_4KB = 'fixtures/yeast/NC_001133.9.4kbp.ctx'
INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'


def stream(buffer):
    buffer.seek(0)
    for _ in kmer_generator_from_stream(buffer):
        pass


def stream_kmers(buffer):
    buffer.seek(0)
    for kmer in kmer_generator_from_stream(buffer):
        kmer.kmer


def stream_kmers_and_add_to_set(buffer):
    kmers = set()
    buffer.seek(0)
    for kmer in kmer_generator_from_stream(buffer):
        kmers.add(kmer.kmer)


def stream_kmers_and_coverage(buffer):
    buffer.seek(0)
    for kmer in kmer_generator_from_stream(buffer):
        kmer.kmer
        kmer.coverage


def stream_kmers_and_edges(buffer):
    buffer.seek(0)
    for kmer in kmer_generator_from_stream(buffer):
        kmer.kmer
        kmer.edges


def stream_kmers_and_coverage_and_edges(buffer):
    buffer.seek(0)
    for kmer in kmer_generator_from_stream(buffer):
        kmer.kmer
        kmer.coverage
        kmer.edges


GRAPHS = {
    '1kb': CHROM_GRAPH_1KB,
    '4kb': CHROM_GRAPH_4KB
}

FUNCS = {
    'pass': stream,
    'kmers': stream_kmers,
    'kmers+set': stream_kmers_and_add_to_set,
    'kmers+cov': stream_kmers_and_coverage,
    'kmers+edges': stream_kmers_and_edges,
    'kmers+cov+edges': stream_kmers_and_coverage_and_edges,
}


@pytest.mark.parametrize('graph_size,func_type',
                         itertools.product(GRAPHS.keys(), FUNCS.keys()))
def test_graph_parser_streaming(benchmark, graph_size, func_type):
    graph = GRAPHS[graph_size]
    func = FUNCS[func_type]
    buffer = io.BytesIO(open(graph, 'rb').read())
    benchmark(func, buffer)
