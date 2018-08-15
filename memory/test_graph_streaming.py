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
CHROM_GRAPH_8KB = 'fixtures/yeast/NC_001133.9.8kbp.ctx'
CHROM_GRAPH_16KB = 'fixtures/yeast/NC_001133.9.16kbp.ctx'
CHROM_GRAPH_64KB = 'fixtures/yeast/NC_001133.9.64kbp.ctx'

GRAPHS = {
    #'8kb': CHROM_GRAPH_8KB,
    #'16kb': CHROM_GRAPH_16KB,
    '64kb': CHROM_GRAPH_64KB,
}


@pytest.mark.parametrize('graph_size', GRAPHS.keys())
def test_graph_parser_streaming(graph_size):
    graph = GRAPHS[graph_size]
    buffer = io.BytesIO(open(graph, 'rb').read())
    header = Header.from_stream(buffer)
    buffer = io.BytesIO(buffer.read())
    stream_kmers_and_coverage_and_edges_and_add_to_list(buffer, header)


from memory_profiler import profile

@profile
def stream_kmers_and_coverage_and_edges_and_add_to_list(buffer, header):
    buffer.seek(0)
    kmers = [kmer for kmer in kmer_generator_from_stream_and_header(buffer, header)]
    for kmer in kmers:
        kmer.kmer
    for kmer in kmers:
        kmer.coverage
    for kmer in kmers:
        kmer.edges



if __name__ == '__main__':
    for graph_size in GRAPHS.keys():
        test_graph_parser_streaming(graph_size)
