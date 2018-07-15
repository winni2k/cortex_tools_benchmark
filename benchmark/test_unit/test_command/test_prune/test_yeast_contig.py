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
MIN_TIP_LENGTH=2

def test_prune_1kbp_contig_one_color(benchmark):
    print_args = CortexpyCommandBuilder().prune(graph=CHROM_GRAPH, min_tip_length=MIN_TIP_LENGTH)
    benchmark(cortexpy.__main__.main, print_args)


def test_prune_1kbp_contig_three_colors(benchmark):
    print_args = CortexpyCommandBuilder().prune(graph=CHROM_GRAPH3, min_tip_length=MIN_TIP_LENGTH)
    benchmark(cortexpy.__main__.main, print_args)



# def test_prune_1kbp_contig_with_cache(benchmark):
#     print_args = CortexpyCommandBuilder().prune(graph=CHROM_GRAPH, min_tip_length=MIN_TIP_LENGTH)
#     print_args += ['--binary-search-cache-size', '1024']
#     benchmark(cortexpy.__main__.main, print_args)


def test_prune_1kbp_contig_mccortex(benchmark, tmpdir):
    seq_file = tmpdir / 'seqs.fa'
    SeqIO.write([SeqRecord(Seq(INITIAL_KMER), id='0')], str(seq_file), 'fasta')
    print_args = MccortexCommandBuilder().clean(CHROM_GRAPH, tips=MIN_TIP_LENGTH)
    benchmark(os.system, ' '.join(print_args))


