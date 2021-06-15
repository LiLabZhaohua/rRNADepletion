# rRNADepletion

This repository contains scripts used to generate probe sequences for rRNA depletion.

These scripts were used in our manuscript:

Gu, H., Sun, Y.H. and Li, X.Z., 2021. [Novel rRNA-depletion methods for total RNA sequencing and ribosome profiling developed for avian species](https://www.sciencedirect.com/science/article/pii/S0032579121003552). Poultry Science

## Usage

1, Download and set up scripts

```
git clone https://github.com/LiLabZhaohua/rRNADepletion.git
cd rRNADepletion && chmod +x *py
```

2, Convert FASTA files to one-line FASTA:

```
./FastaSeqLinearizer.py Original_Sequence/Gallus_12S_rRNA_mitochondria_MH879470_Complete.fa Gallus_12S.fa
./FastaSeqLinearizer.py Original_Sequence/Gallus_16S_rRNA_mitochondria_MH879470_Complete.fa Gallus_16S.fa
./FastaSeqLinearizer.py Original_Sequence/Gallus_18S_rRNA_AF173612.1.fa Gallus_18S.fa
./FastaSeqLinearizer.py Original_Sequence/Gallus_28S_rRNA_XR_003078040.1.fa Gallus_28S.fa
./FastaSeqLinearizer.py Original_Sequence/Gallus_5.8S_rRNA_XR_003078039.1.fa Gallus_5.8S.fa
./FastaSeqLinearizer.py Original_Sequence/Gallus_5S_rRNA_XR_003076910.1.fa Gallus_5S.fa
```

3, Generate probe sequences

```
./RiboProbeGenerator.py Gallus_12S.fa Gallus_12S.probes.fa
./RiboProbeGenerator.py Gallus_16S.fa Gallus_16S.probes.fa
./RiboProbeGenerator.py Gallus_18S.fa Gallus_18S.probes.fa
./RiboProbeGenerator.py Gallus_28S.fa Gallus_28S.probes.fa
./RiboProbeGenerator.py Gallus_5.8S.fa Gallus_5.8S.probes.fa
./RiboProbeGenerator.py Gallus_5S.fa Gallus_5S.probes.fa
```

4, Remove multi-mapping probe sequences using UCSC BLAT against galGal6 chicken genome:

[UCSC genome browser for galGal6](https://genome.ucsc.edu/cgi-bin/hgTracks?db=galGal6&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr4%3A45667317%2D45670831&hgsid=1081465641_QMMF8QE7gaanGBtavq0aDOgVnEn3)

[UCSC BLAT for galGal6](https://genome.ucsc.edu/cgi-bin/hgBlat?hgsid=1081465641_QMMF8QE7gaanGBtavq0aDOgVnEn3&command=start)
