import cortexpy.__main__
from Bio import SeqIO

import os
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from benchmark.commands import CortexpyCommandBuilder, MccortexCommandBuilder

CHROM_GRAPH = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
CHROM_GRAPH3 = 'fixtures/yeast/NC_001133.9.c3.1kbp.ctx'
CHROM_GRAPH_ALL = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'


def test_traverse_1kbp_contig_one_color(benchmark):
    print_args = CortexpyCommandBuilder().traverse(graphs=[CHROM_GRAPH],
                                                   initial_contig=INITIAL_KMER)

    def something():  # unnecessary function call
        cortexpy.__main__.main([str(a) for a in print_args])

    benchmark.pedantic(something, iterations=1, rounds=1, warmup_rounds=1)
