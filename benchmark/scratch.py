from contextlib import redirect_stdout

from itertools import islice

import cortexpy.__main__
from benchmark.commands import CortexpyCommandBuilder, MccortexCommandBuilder
from pympler import summary, muppy, tracker, refbrowser

from cortexpy.graph.parser import RandomAccess

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


def test_kmer_memory_usage():
    with open('memory_profiler.log', 'w') as fp:
        with redirect_stdout(fp):
            tr = tracker.SummaryTracker()
            tr.print_diff()
            with open(CHROM_GRAPH, 'rb') as gp:
                ra = RandomAccess(gp)
                tr.print_diff()
                ra_generator = iter(ra.values())
                tr.print_diff()
                kmers = list(islice(ra_generator, 10))
                tr.print_diff()
                kmers2 = list(islice(ra_generator, 100))
                tr.print_diff()
                kmers3 = list(islice(ra_generator, 1000))
                tr.print_diff()
                print('kmer.kmer')
                for kmer in kmers3:
                    kmer.kmer
                tr.print_diff()
                print('kmer.coverage')
                for kmer in kmers3:
                    kmer.coverage
                tr.print_diff()
                print('kmer.edges')
                for kmer in kmers3:
                    kmer.edges
                tr.print_diff()
