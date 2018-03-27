import cortexpy.__main__
import os

from ...commands import CortexpyCommandBuilder, MccortexCommandBuilder, CortexjdkCommandBuilder

CHROM_GRAPH = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'


def test_traverse_1kbp_contig(benchmark):
    print_args = CortexpyCommandBuilder(unit_testing=True).traverse(graphs=[CHROM_GRAPH],
                                                                    initial_contig=INITIAL_KMER)
    benchmark(cortexpy.__main__.main, [str(a) for a in print_args])
