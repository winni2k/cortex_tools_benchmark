import pytest

import cortexpy.__main__
from ...commands import CortexpyCommandBuilder

graph0 = 'fixtures/yeast/g1000.traverse.ctx'
graph1 = 'fixtures/yeast/g750.traverse.ctx'
graph2 = 'fixtures/yeast/g122.traverse.ctx'


@pytest.mark.timeout(20)
def test_view_traversal_3521_kmers(benchmark):
    traverse_args = CortexpyCommandBuilder().view_traversal(graph=graph0)
    benchmark(cortexpy.__main__.main, traverse_args)


@pytest.mark.timeout(20)
def test_view_traversal_12233_kmers(benchmark):
    traverse_args = CortexpyCommandBuilder().view_traversal(graph=graph1)
    benchmark(cortexpy.__main__.main, traverse_args)


@pytest.mark.timeout(20)
def test_view_traversal_26726_kmers(benchmark):
    traverse_args = CortexpyCommandBuilder().view_traversal(graph=graph2)
    benchmark(cortexpy.__main__.main, traverse_args)
