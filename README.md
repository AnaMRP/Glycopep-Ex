# Glycopep-Ex
Python script to build up an extractor of glycopeptides from feature files obtained from PEAKS Studio 8.5. 

REQUIREMENTS
It requires mass spectrometry results from nanoLC-MS/MS experiments to be processed with the PEAKS PTM algorithm, and feature files to be exported from PEAKS as tab-delimited text files (.txt).

HOW IT WORKS
Modify the script to include the mass of the oxonium ion of the PTM studied. Currently set for the search of GlcNAc with 203.08 as oxonium ion. To include more oxonium ions, edit the code with the or (|) expression (e.g. '203.08'|'365'). 

OUTPUTS
Histograms
