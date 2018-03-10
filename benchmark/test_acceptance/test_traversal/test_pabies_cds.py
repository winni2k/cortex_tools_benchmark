import cortexpy.__main__

from ...commands import build_traverse_command

PABIES_CDS = 'fixtures/Pabies_coding_sequence/Pabies1.0-all-cds.ctx'


def test_442_base_unitig(benchmark, tmpdir):
    intermediate_graph = tmpdir / 'traversal.pickle'
    initial_kmer = 'ATGGAGGCCGTGAAATCTTTGGAGGATGTGTTCGGCATGAAGGGTGG'
    traverse_args = build_traverse_command(graphs=[PABIES_CDS],
                                           initial_kmers=initial_kmer,
                                           colors=[0],
                                           out=intermediate_graph)
    benchmark(cortexpy.__main__.main, [str(a) for a in traverse_args])
    # print_traversal(intermediate_graph)
