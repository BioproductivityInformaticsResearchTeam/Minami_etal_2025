#!/bin/bash

# liftover 実行

paftools.js liftover Bd1_t314-q192.cs_long.paf Bdistachyon_192_gene_exons.edited.Bd1_Bd5.Phytozome9.gff3.Bd1.gene.bed > Bd1_Bdistachyon_192_gene.liftover.bed
paftools.js liftover Bd2_t314-q192.cs_long.paf Bdistachyon_192_gene_exons.edited.Bd1_Bd5.Phytozome9.gff3.Bd2.gene.bed > Bd2_Bdistachyon_192_gene.liftover.bed
paftools.js liftover Bd3_t314-q192.cs_long.paf Bdistachyon_192_gene_exons.edited.Bd1_Bd5.Phytozome9.gff3.Bd3.gene.bed > Bd3_Bdistachyon_192_gene.liftover.bed
paftools.js liftover Bd4_t314-q192.cs_long.paf Bdistachyon_192_gene_exons.edited.Bd1_Bd5.Phytozome9.gff3.Bd4.gene.bed > Bd4_Bdistachyon_192_gene.liftover.bed
paftools.js liftover Bd5_t314-q192.cs_long.paf Bdistachyon_192_gene_exons.edited.Bd1_Bd5.Phytozome9.gff3.Bd5.gene.bed > Bd5_Bdistachyon_192_gene.liftover.bed
