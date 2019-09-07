CTX=/home/kiran/repositories/mccortex/bin/mccortex63

$CTX build -f -m 1G -k 47 -S -s pKPC_UVA01 -1 pKPC_UVA01.fasta pKPC_UVA01.ctx
$CTX thread -f -m 1G -1 pKPC_UVA01.fasta -o pKPC_UVA01.ctp.gz pKPC_UVA01.ctx
$CTX contigs -f -m 1G -o pKPC_UVA01.contigs.no_links.fasta pKPC_UVA01.ctx
$CTX rmsubstr -f -m 1G -o pKPC_UVA01.contigs.no_links.rmsubstr.fasta pKPC_UVA01.contigs.no_links.fasta
$CTX contigs -f -m 1G -p pKPC_UVA01.ctp.gz -o pKPC_UVA01.contigs.with_links.fasta pKPC_UVA01.ctx
$CTX rmsubstr -f -m 1G -o pKPC_UVA01.contigs.with_links.rmsubstr.fasta pKPC_UVA01.contigs.with_links.fasta

$CTX build -f -m 1G -k 47 -S -s pKPC_UVA02 -1 pKPC_UVA02.fasta pKPC_UVA02.ctx
$CTX thread -f -m 1G -1 pKPC_UVA02.fasta -o pKPC_UVA02.ctp.gz pKPC_UVA02.ctx
$CTX contigs -f -m 1G -o pKPC_UVA02.contigs.no_links.fasta pKPC_UVA02.ctx
$CTX rmsubstr -f -m 1G -o pKPC_UVA02.contigs.no_links.rmsubstr.fasta pKPC_UVA02.contigs.no_links.fasta
$CTX contigs -f -m 1G -p pKPC_UVA02.ctp.gz -o pKPC_UVA02.contigs.with_links.fasta pKPC_UVA02.ctx
$CTX rmsubstr -f -m 1G -o pKPC_UVA02.contigs.with_links.rmsubstr.fasta pKPC_UVA02.contigs.with_links.fasta
