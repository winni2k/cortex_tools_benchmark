import attr
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


@attr.s(slots=True)
class CortexpyCommandBuilder(object):
    cortexpy_binary = attr.ib('cortexpy')
    unit_testing = attr.ib(False)

    def get_command(self, *args):
        cmd = []
        if not self.unit_testing:
            cmd.append(self.cortexpy_binary)
        cmd += args
        return cmd

    def view_graph(self, *, graph):
        return self.get_command('view', 'graph', graph)

    def traverse(self, *, graphs, initial_contig):
        args = ['traverse', '-v']
        for g in graphs:
            args += ['--graph', g]
        args += ['--out', '-']
        args.append(initial_contig)
        return self.get_command(*args)


@attr.s(slots=True)
class MccortexCommandBuilder(object):
    mccortex_binary = attr.ib('mccortex63')

    def view_command(self, *, graph, kmers=True):
        args = [self.mccortex_binary, 'view']
        if kmers:
            args += '-k'
        args += graph
        return args


@attr.s(slots=True)
class CortexjdkCommandBuilder(object):
    cortexjdk_jar = attr.ib('opt/cortexjdk.jar')

    def view_command(self, *, graph):
        args = ['java', '-jar', self.cortexjdk_jar, 'View']
        args += graph
        return args
