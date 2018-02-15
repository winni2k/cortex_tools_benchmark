import json

from cortexpy.test.runner import Cortexpy

DAL19_GRAPH = 'fixtures/DAL19/oases_pear.dal19_illumina_oases_reads.joined.dal19_subgraph.ctx'


class TestDal19IlluminaAndOasesJointGraphTraversal(object):
    def test_traverses_all_of_locus_3_of_4(self):
        # given
        traversal_colors = (0, 5)
        expected_locus_3_4_unitig = (
            'GGCCTTTCTATTCACGGATTCACAACCTGGATTCAAGAGCTGGTGTGGCTATCGTTAGCAGCCAT'
            'TATTAGGTCTCAATTTTTAGCGCCTCCCTCTTTCTACTAGGTGCTTGTTCTCCTTACCCGGGATCT'
            'GATCTACATAAGACTGTAACTGTCTTGGAGTGCATCAGGGA')
        expected_locus_3_4_unitig_right_node = 'GGATCTGATCTACATAAGACTGTAACTGTCTTGGAGTGCATCAGGGA'
        # start_kmer = 'GATCTGATCTACATAAGACTGTAACTGTCTTGGAGTGCATCAGGGAG'
        dal19_psi_kmer = 'TATGCAAAAAATGTTGGAGAGGTATCAAAAGTATTCACAAGAAAGTG'
        runner = Cortexpy()

        # when
        completed_process = runner.view_traversal(contig=dal19_psi_kmer, graph=DAL19_GRAPH,
                                                  colors=traversal_colors, max_nodes=10000)

        # then
        graph_json = json.loads(completed_process.stdout)
        print(graph_json)
        locus_3_4_unitigs = list(
            filter(lambda u: u['right_node'] == expected_locus_3_4_unitig_right_node,
                   graph_json['nodes']))
        assert 1 == len(locus_3_4_unitigs)
        locus_3_4_unitig = locus_3_4_unitigs[0]
        assert expected_locus_3_4_unitig == locus_3_4_unitig['unitig']
