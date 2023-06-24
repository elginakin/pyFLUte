# PyFLUte

## Description:
``pyFlute`` is a python packaged targeted towards handling messy or incomplete influenza genome datasets. It is primarily built as a wrapper for [seqkit](https://bioinf.shenwei.me/seqkit/) ([doi:10.1371/journal.pone.0163962](https://doi.org/10.1371/journal.pone.0163962))

## Dependencies: 
* [seqkit](https://bioinf.shenwei.me/seqkit/) 
* Python ≥3.0

## Our Issue pyFLUte addresses:
Acquiring sequences through in-house influenza genome sequencing pipelines or   genome acquisition databases can result in 'uneven' or 'incomplete' influenza genome datasets making tedious work out of data preparation. `pyFLUte` remedies this by providing an integratabtle CLI tool for separating genome segments for downstream analysis. 

> **Warning** `.fasta` header formatting requirements
> * [GISAID](https://gisaid.org/): `Isolate name|Isolate ID | Segment` OR `Isolate name|Isolate ID | Segment number`
> * [NCBI Influenza Virus Database](https://www.ncbi.nlm.nih.gov/genomes/FLU/Database/nph-select.cgi?go=database) : `>{strain}_{segment}`

Current segment header match cases supported 
* `*_1`
* `*|1`
* `*_PB2`
* `*|PB2`

## Usage 

```
usage: pyflute.py [-h] [-i INPUT] [-o OUTPUT] [-r]

  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input directory for the FASTA file
  -o OUTPUT, --output OUTPUT
                        Output directory for the extracted sequences
  -r, --stats           Generates a report for each sorted segment file
  
```

## Examples using the example data folder 

>**Note** Example influenza genome data was aquired through the [NCBI Influenza Virus Database](https://www.ncbi.nlm.nih.gov/genomes/FLU/Database/nph-select.cgi?go=database). Accession numbers can be found in [/example_input/NCBI_example_accessions.txt](/example_input/NCBI_example_accessions.txt)

Basic use case for sorting a single `.fasta` file containing incomplete segments: 

``` 
python3 pyflute.py -i ./input_directory -o ./output_directory 
```

Sorts sequences and provides a CLI report of the resulting sorted sequences:

```
python3 pyflute.py -i ./input_directory -o ./output_directory  -r
```
output: 

|      file     | format | type | num_seqs | sum_len | min_len | avg_len | max_len |
|:-------------:|:------:|:----:|:--------:|:-------:|:-------:|:-------:|:-------:|
| 1_PB2.fasta  | FASTA  | DNA  |    77    | 179,064 |  1,942  | 2,325.5 |  2,341  |
| 2_PB1.fasta  | FASTA  | DNA  |    80    | 188,838 |  2,181  | 2,360.5 |  2,396  |
| 3_PA.fasta   | FASTA  | DNA  |    78    | 176,706 |  1,984  | 2,265.5 |  2,305  |
| 4_HA.fasta   | FASTA  | DNA  |    71    | 130,000 |  1,638  |  1,831  |  1,847  |
| 5_NP.fasta   | FASTA  | DNA  |    67    | 120,647 |  1,612  | 1,800.7 |  1,844  |
| 6_NA.fasta   | FASTA  | DNA  |    75    | 113,874 |  1,401  | 1,518.3 |  1,557  |
| 7_M.fasta    | FASTA  | DNA  |    59    |  67,602 |  1,046  | 1,145.8 |  1,189  |
| 8_NS.fasta   | FASTA  | DNA  |    55    |  58,410 |  1,024  |  1,062  |  1,068  |



### Glossary: 
1.  '**Incomplete Genome**'' OR '**Genome Completeness**': In this documentation, an 'incomplete genome' refers to a genome that is not fully recoverable by our RT-PCR ➡️ sequencing pipeline, **NOT** a defective or defective interfering genomes (DVGs) which have been observed to be players in viral pathogenesis ([Defective viral genomes are key drivers of the virus–host interaction | Nature Microbiology](https://www.nature.com/articles/s41564-019-0465-y) ). 


### Future Additions 

* interactive report summarizing complete and incomplete genome segments. 

