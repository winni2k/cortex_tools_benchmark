import pytest

import cortexpy.__main__
from ...commands import CortexpyCommandBuilder

GRAPH = 'fixtures/spruce/totRNA-18.full.clean.ctx'
initial_kmer = 'AAGTCTGCTACTTTTTCAACCAGGCCAGTTGGATATTTAGCAACATC'


class TestSpruce(object):
    @pytest.mark.timeout(20)
    def test_traverse_with_one_color(self, benchmark, tmpdir):
        traverse_args = CortexpyCommandBuilder().traverse(graphs=[GRAPH],
                                                          initial_contig=initial_kmer,
                                                          out='/dev/null', cache_size=1024)
        benchmark(cortexpy.__main__.main, [str(a) for a in traverse_args])
