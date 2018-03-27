import cortexpy.__main__
import os

from benchmark.commands import CortexpyCommandBuilder, MccortexCommandBuilder, CortexjdkCommandBuilder

CHROM_GRAPH = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'


def test_view_graph_1kbp_contig(benchmark):
    print_args = CortexpyCommandBuilder(unit_testing=True).view_graph(graph=CHROM_GRAPH)
    benchmark(cortexpy.__main__.main, [str(a) for a in print_args])
