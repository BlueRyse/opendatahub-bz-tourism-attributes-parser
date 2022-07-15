# OpenDataHub BZ Tourism attribute parser

These Python scripts parses all the attributes from the ODH tourism API and creates either an XML or a CSV (depending on the script you use) file with all the attributes.

The list of calls for each dataset is inside the datasets.py file. They are represented inside a dictionary, and used in both of the scripts.

To retrieve all the attributes of all the datasets simply execute one of the scripts (depending on which format you like).

To see the CSVs correctly, set the comma ',' as a separator in your CSV viewer (e.g. libreoffice).

Note that the scripts currently work only with the datasets inside datasets.py, we didn't test the other datasets yet.  