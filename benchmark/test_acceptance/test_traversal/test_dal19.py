import cortexpy.__main__
from ...commands import build_traverse_command

DAL19_GRAPH = 'fixtures/DAL19/oases_pear.dal19_illumina_oases_reads.joined.dal19_subgraph.ctx'
dal19_psi_kmer = 'TATGCAAAAAATGTTGGAGAGGTATCAAAAGTATTCACAAGAAAGTG'


def test_assembly_with_one_color(benchmark, tmpdir):
    intermediate_graph = tmpdir / 'traversal.pickle'
    traverse_args = build_traverse_command(graphs=[DAL19_GRAPH],
                                           initial_kmers=dal19_psi_kmer,
                                           colors=[5],
                                           out=intermediate_graph)
    benchmark(cortexpy.__main__.main, [str(a) for a in traverse_args])


def test_assembly_with_two_colors(benchmark, tmpdir):
    intermediate_graph = tmpdir / 'traversal.pickle'
    traverse_args = build_traverse_command(graphs=[DAL19_GRAPH],
                                           initial_kmers=dal19_psi_kmer,
                                           colors=[0, 5],
                                           out=intermediate_graph)
    benchmark(cortexpy.__main__.main, [str(a) for a in traverse_args])


def test_assembly_with_ten_colors(benchmark, tmpdir):
    intermediate_graph = tmpdir / 'traversal.pickle'
    traverse_args = build_traverse_command(graphs=[DAL19_GRAPH],
                                           initial_kmers=dal19_psi_kmer,
                                           colors=list(range(10)),
                                           out=intermediate_graph)
    benchmark(cortexpy.__main__.main, [str(a) for a in traverse_args])
