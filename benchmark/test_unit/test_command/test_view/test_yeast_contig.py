import pytest
from benchmark.commands import CortexpyCommandBuilder

import cortexpy.__main__

CHROM_GRAPH_1k = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
CHROM_GRAPH = 'fixtures/yeast/NC_001133.9.64kbp.ctx'

INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'


def test_view_graph_1kbp_contig(benchmark):
    print_args = CortexpyCommandBuilder().view_graph(graph=CHROM_GRAPH_1k)
    benchmark(cortexpy.__main__.main, [str(a) for a in print_args])


def test_view_traversal_1kbp_contig(benchmark):
    print_args = CortexpyCommandBuilder().view_traversal(graph=CHROM_GRAPH_1k)
    benchmark(cortexpy.__main__.main, [str(a) for a in print_args])


def test_view_traversal_contig_memory():
    print_args = CortexpyCommandBuilder().view_traversal(graph=CHROM_GRAPH)
    cortexpy.__main__.main([str(a) for a in print_args])
