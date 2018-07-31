from contextlib import redirect_stdout

from itertools import islice
import pstats, cProfile

import io

import cortexpy.__main__
from benchmark.commands import CortexpyCommandBuilder, MccortexCommandBuilder
from pympler import summary, muppy, tracker, refbrowser

from cortexpy.graph.parser import RandomAccess
from cortexpy.graph.parser.header import Header
from cortexpy.graph.parser.streaming import kmer_generator_from_stream_and_header

CHROM_GRAPH = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
CHROM_GRAPH3 = 'fixtures/yeast/NC_001133.9.c3.1kbp.ctx'
CHROM_GRAPH_ALL = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'


def test_traverse_1kbp_contig_one_color(benchmark):
    print_args = CortexpyCommandBuilder().traverse(graphs=[CHROM_GRAPH],
                                                   initial_contig=INITIAL_KMER)

    def something():  # unnecessary function call
        cortexpy.__main__.main([str(a) for a in print_args])

    benchmark.pedantic(something, iterations=1, rounds=5, warmup_rounds=1)


def stream_kmers_and_coverage_and_edges(buffer, header):
    buffer.seek(0)
    for kmer in kmer_generator_from_stream_and_header(buffer, header):
        kmer.kmer
        kmer.coverage
        kmer.edges


def test_cython_speed():
    graph = 'fixtures/yeast/NC_001133.9.16kbp.ctx'
    buffer = io.BytesIO(open(graph, 'rb').read())
    header = Header.from_stream(buffer)
    buffer = io.BytesIO(buffer.read())

    cProfile.runctx("stream_kmers_and_coverage_and_edges(buffer, header)", globals(), locals(), "Profile.prof")
    s = pstats.Stats("Profile.prof")
    raise Exception(s.strip_dirs().sort_stats("time").print_stats())


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
                print('10 kmers')
                kmers = list(islice(ra_generator, 10))
                tr.print_diff()
                print('100 kmers')
                kmers2 = list(islice(ra_generator, 100))
                tr.print_diff()
                print('1000 kmers')
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
