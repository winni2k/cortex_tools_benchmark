import cortexpy.__main__

PABIES_CDS = 'fixtures/Pabies_coding_sequence/Pabies1.0-all-cds.ctx'


def test_442_base_unitig(benchmark):
    initial_kmer = 'ATGGAGGCCGTGAAATCTTTGGAGGATGTGTTCGGCATGAAGGGTGG'
    cmdline_args = ['view',
                    'traversal',
                    PABIES_CDS,
                    initial_kmer,
                    '--output-type',
                    'kmers',
                    '--output-format',
                    'json',
                    '--colors',
                    '0',
                    '--max-nodes',
                    '1000']
    benchmark(cortexpy.__main__.main, cmdline_args)
