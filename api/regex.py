import re

SINGLE_TERM_QUERIES = {
    "gene": re.compile(r'^([A-Z][0-9A-Za-z]{0,13}@?(-[0-9A-Z][0-9A-Za-z]{0,6})*)$'),
    "genomic_coordinates": re.compile(r'^(chr)?([0-9]{1,2}|X|Y|MT):\d+-\d+$'),
    "chr_pos_ref_alt": re.compile(r'^(chr)?([0-9]{1,2}|X|Y|MT)-\d+-[ACGT-]+-[ACGT-]+$'),
    "aa_change": re.compile(r'^[A-Za-z]{1,3}\d+[A-Za-z]{1,3}$')
}

# MULTI_TERM_QUERIES = {
#     "gene_aa": re.compile(r'^[a-zA-Z0-9@_-]+\s[a-zA-Z]+\d+[a-zA-Z]+$')
# }
