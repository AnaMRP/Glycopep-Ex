# Glycopep-Ex
Python script to build up an extractor of glycopeptides from feature files obtained from PEAKS Studio 8.5. 

REQUIREMENTS:

It requires mass spectrometry results from nanoLC-MS/MS experiments to be processed with the PEAKS PTM algorithm, and feature files to be exported from PEAKS as tab-delimited text files (.txt).

HOW IT WORKS:

Modify the script with the name of the file to analyze (instead of "test.txt" or "peptide_feature_1.txt") and the mass of the oxonium ion of the PTM studied. Currently set for the search of GlcNAc with 203.08 as oxonium ion. To include more oxonium ions, edit the code with the OR (|) expression (e.g. '203.08'|'162.05' for GlcNAc and Hex). 

OUTPUTS:

The program outputs simple graphs demonstrating the distribution of the PTMs searched for, as histograms of the distribution of the m/z of the modified peptides (glycopeptides) and the distribution of charges.
