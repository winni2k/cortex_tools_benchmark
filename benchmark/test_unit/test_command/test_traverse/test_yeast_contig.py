import cortexpy.__main__
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from benchmark.commands import CortexpyCommandBuilder, MccortexCommandBuilder

CHROM_GRAPH = 'fixtures/yeast/NC_001133.9.1kbp.ctx'
INITIAL_KMER = 'CCACACCACACCCACACACCCACACACCACACCACACACCACACCAC'


def test_traverse_1kbp_contig(benchmark):
    print_args = CortexpyCommandBuilder(unit_testing=True).traverse(graphs=[CHROM_GRAPH],
                                                                    initial_contig=INITIAL_KMER)
    benchmark(cortexpy.__main__.main, [str(a) for a in print_args])


def test_traverse_1kbp_contig_mccortex(benchmark, tmpdir):
    seq_file = tmpdir / 'seqs.fa'
    SeqIO.write([SeqRecord(Seq(INITIAL_KMER), id='0')], str(seq_file), 'fasta')
    print_args = MccortexCommandBuilder().subgraph(graphs=[CHROM_GRAPH],
                                                   initial_contig_file=str(seq_file))
    benchmark(cortexpy.__main__.main, [str(a) for a in print_args])
