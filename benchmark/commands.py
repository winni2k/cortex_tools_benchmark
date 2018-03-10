import cortexpy.__main__


def print_traversal(traversal_graph):
    view_args = ['view',
                 'traversal',
                 traversal_graph,
                 '--to-json',
                 '--kmers']
    cortexpy.__main__.main([str(a) for a in view_args])


def build_traverse_command(*, graphs, initial_kmers, colors=None, out):
    args = ['cortexpy', 'traverse',
            initial_kmers,
            '--colors',
            ','.join([str(n) for n in colors]),
            '--out', str(out)] + ['--graph {}'.format(g) for g in graphs]
    return args
