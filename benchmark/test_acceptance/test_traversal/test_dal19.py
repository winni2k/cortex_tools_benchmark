import cortexpy.__main__

DAL19_GRAPH = 'fixtures/DAL19/oases_pear.dal19_illumina_oases_reads.joined.dal19_subgraph.ctx'


def test_assembly_with_one_color(benchmark):
    dal19_psi_kmer = 'TATGCAAAAAATGTTGGAGAGGTATCAAAAGTATTCACAAGAAAGTG'
    cmdline_args = ['view',
                    'traversal',
                    DAL19_GRAPH,
                    dal19_psi_kmer,
                    '--output-type',
                    'kmers',
                    '--output-format',
                    'json',
                    '--colors',
                    5,
                    '--max-nodes',
                    1000]
    benchmark(cortexpy.__main__.main, [str(a) for a in cmdline_args])


def test_assembly_with_two_colors(benchmark):
    dal19_psi_kmer = 'TATGCAAAAAATGTTGGAGAGGTATCAAAAGTATTCACAAGAAAGTG'
    cmdline_args = ['view',
                    'traversal',
                    DAL19_GRAPH,
                    dal19_psi_kmer,
                    '--output-type',
                    'kmers',
                    '--output-format',
                    'json',
                    '--colors',
                    '0,5',
                    '--max-nodes',
                    1000]
    benchmark(cortexpy.__main__.main, [str(a) for a in cmdline_args])


def test_assembly_with_ten_colors(benchmark):
    dal19_psi_kmer = 'TATGCAAAAAATGTTGGAGAGGTATCAAAAGTATTCACAAGAAAGTG'
    cmdline_args = ['view',
                    'traversal',
                    DAL19_GRAPH,
                    dal19_psi_kmer,
                    '--output-type',
                    'kmers',
                    '--output-format',
                    'json',
                    '--colors',
                    ','.join([str(n) for n in range(10)]),
                    '--max-nodes',
                    1000]
    benchmark(cortexpy.__main__.main, [str(a) for a in cmdline_args])
