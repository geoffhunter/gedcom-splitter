# gedcom-splitter
Note: this utility needs the .py and .txt files in the gedcom-file-processor repository to function

A utility to split a GEDCOM format file.

This utility allows the user to extract a branch of a family tree, from a GEDCOM format file, and create a new GEDCOM file. 

It allows the user to specify a family in params. It then processes the GEDCOM file, tagging all ancestors of the specified family, and all relatives of these ancestors. 

It then produces a ‘New.ged’ file containing all the details from the source GEDCOM file, but only for the tagged individuals and families.

The process of creating the new GED file is separated from the process of tagging, to allow manual tagging to be done, for example to un-tag individuals that are still living, and their families, to protect their privacy if required.

