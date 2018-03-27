import os

from ...commands import CortexpyCommandBuilder, MccortexCommandBuilder, CortexjdkCommandBuilder

CHROM_GRAPH = 'fixtures/yeast/NC_001133.9.ctx'
INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'


def test_cortexpy_view_graph(benchmark):
    print_args = CortexpyCommandBuilder().view_graph(graph=CHROM_GRAPH)
    cmd = ' '.join([str(a) for a in print_args])
    benchmark.pedantic(os.system, args=(cmd,), iterations=2)

def test_mccortex_view(benchmark):
    print_args = MccortexCommandBuilder().view_command(graph=CHROM_GRAPH)
    benchmark(os.system, ' '.join([str(a) for a in print_args]))

def test_cortexjdk_view(benchmark):
    print_args = CortexjdkCommandBuilder().view_command(graph=CHROM_GRAPH)
    cmd = ' '.join([str(a) for a in print_args])
    benchmark.pedantic(os.system, args=(cmd,), iterations=2)
