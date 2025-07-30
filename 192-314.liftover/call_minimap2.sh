#!/bin/bash

# Minimap2 実行
minimap2 -t 18 -c --cs=long Bdistachyon_314_v3.0.Bd1-5.fa.Bd1.fasta Bdistachyon_192.Bd1-5.fasta.Bd1.fasta > Bd1_t314-q192.cs_long.paf &
minimap2 -t 18 -c --cs=long Bdistachyon_314_v3.0.Bd1-5.fa.Bd2.fasta Bdistachyon_192.Bd1-5.fasta.Bd2.fasta > Bd2_t314-q192.cs_long.paf & 
minimap2 -t 18 -c --cs=long Bdistachyon_314_v3.0.Bd1-5.fa.Bd3.fasta Bdistachyon_192.Bd1-5.fasta.Bd3.fasta > Bd3_t314-q192.cs_long.paf & 
minimap2 -t 18 -c --cs=long Bdistachyon_314_v3.0.Bd1-5.fa.Bd4.fasta Bdistachyon_192.Bd1-5.fasta.Bd4.fasta > Bd4_t314-q192.cs_long.paf & 
minimap2 -t 18 -c --cs=long Bdistachyon_314_v3.0.Bd1-5.fa.Bd5.fasta Bdistachyon_192.Bd1-5.fasta.Bd5.fasta > Bd5_t314-q192.cs_long.paf & 

