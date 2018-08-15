import io
import itertools

import pytest

from cortexpy.graph.parser.header import Header
from cortexpy.graph.parser.streaming import (
    kmer_generator_from_stream_and_header,
    kmer_list_generator_from_stream_and_header,
    kmer_string_generator_from_stream_and_header,
)

CHROM_GRAPH_1KB = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
CHROM_GRAPH_4KB = 'fixtures/yeast/NC_001133.9.4kbp.ctx'
CHROM_GRAPH_16KB = 'fixtures/yeast/NC_001133.9.16kbp.ctx'
INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'


def stream(buffer, header):
    buffer.seek(0)
    for _ in kmer_generator_from_stream_and_header(buffer, header):
        pass


def stream_kmer_lists(buffer, header):
    buffer.seek(0)
    for _ in kmer_list_generator_from_stream_and_header(buffer, header):
        pass


def stream_kmer_bytes(buffer, header):
    buffer.seek(0)
    for kmer_list in kmer_list_generator_from_stream_and_header(buffer, header):
        kmer_list.tostring()


def stream_kmer_tuples(buffer, header):
    buffer.seek(0)
    for kmer_list in kmer_list_generator_from_stream_and_header(buffer, header):
        tuple(kmer_list)


def stream_kmer_strings(buffer, header):
    buffer.seek(0)
    for _ in kmer_string_generator_from_stream_and_header(buffer, header):
        pass


def stream_kmers(buffer, header):
    buffer.seek(0)
    for kmer in kmer_generator_from_stream_and_header(buffer, header):
        kmer.kmer


def stream_kmers_and_add_to_set(buffer, header):
    kmers = set()
    buffer.seek(0)
    for kmer in kmer_generator_from_stream_and_header(buffer, header):
        kmers.add(kmer.kmer)


def stream_kmers_and_coverage(buffer, header):
    buffer.seek(0)
    for kmer in kmer_generator_from_stream_and_header(buffer, header):
        kmer.kmer
        kmer.coverage


def stream_kmers_and_edges(buffer, header):
    buffer.seek(0)
    for kmer in kmer_generator_from_stream_and_header(buffer, header):
        kmer.kmer
        kmer.edges


def stream_kmers_and_coverage_and_edges(buffer, header):
    buffer.seek(0)
    for kmer in kmer_generator_from_stream_and_header(buffer, header):
        kmer.kmer
        kmer.coverage
        kmer.edges


GRAPHS = {
    '1kb': CHROM_GRAPH_1KB,
    '4kb': CHROM_GRAPH_4KB,
    '16kb': CHROM_GRAPH_16KB
}

FUNCS = {
    'pass': stream,
    'kmer_lists': stream_kmer_lists,
    'kmer_bytes': stream_kmer_bytes,
    'kmer_tuples': stream_kmer_tuples,
    'kmer_strings': stream_kmer_strings,
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
    header = Header.from_stream(buffer)
    buffer = io.BytesIO(buffer.read())
    benchmark(func, buffer, header)
