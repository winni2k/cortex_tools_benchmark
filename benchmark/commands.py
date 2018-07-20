import attr
import cortexpy.__main__


def print_traversal(traversal_graph):
    view_args = ['view',
                 'traversal',
                 traversal_graph,
                 '--to-json',
                 '--kmers']
    cortexpy.__main__.main([str(a) for a in view_args])


def build_traverse_command(*, graphs, initial_kmers, out, colors=None):
    return CortexpyCommandBuilder().traverse(graphs=graphs, initial_contig=initial_kmers,
                                             colors=colors, out=out)


@attr.s(slots=True)
class CortexpyCommandBuilder(object):
    def get_command(self, *args):
        return [str(a) for a in args]

    def view_graph(self, *, graph):
        return self.get_command('view', 'graph', graph)

    def view_traversal(self, *, graph, out='/dev/null'):
        return self.get_command('view', 'traversal', graph, '--out', out)

    def traverse(self, *, graphs, initial_contig, out='/dev/null', colors=None):
        args = ['traverse', '-v', initial_contig]
        for g in graphs:
            args += ['--graphs', g]
        args += ['--out', out]
        if colors:
            args.append('--colors')
            args += colors
        return self.get_command(*args)

    def prune(self, *, graph, min_tip_length, out='/dev/null'):
        args = ['prune', graph, '--remove-tips', min_tip_length, '--out', out]
        return self.get_command(*args)


@attr.s(slots=True)
class MccortexCommandBuilder(object):
    mccortex_binary = attr.ib('mccortex63')

    def get_command(self, args):
        return [str(a) for a in [self.mccortex_binary] + args]

    def subgraph(self, *, graphs, initial_contig_file):
        args = [self.mccortex_binary, 'subgraph', '--seq', initial_contig_file]
        for graph in graphs:
            args.append(graph)
        args += ['--out', '/dev/null']
        return args

    def view(self, *, graph, kmers=True):
        args = [self.mccortex_binary, 'view']
        if kmers:
            args += '-k'
        args += graph
        return args

    def clean(self, *graphs, tips=0, unitigs=0, out='/devl/null'):
        args = ['clean'] + list(graphs) + [f'--tips={tips}', f'--unitigs={unitigs}', '--out', out]
        return self.get_command(args)


@attr.s(slots=True)
class CortexjdkCommandBuilder(object):
    cortexjdk_jar = attr.ib('opt/cortexjdk.jar')

    def view_command(self, *, graph):
        args = ['java', '-jar', self.cortexjdk_jar, 'View']
        args += graph
        return args
