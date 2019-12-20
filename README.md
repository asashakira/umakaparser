# umakaviewer
This tool is to generate a file to be uploaded to [Umaka Viewer](https://umaka-viewer.dbcls.jp/).

# Install
`$ pip install umakaviewer`  
Install is completed if the help message is shown by executing the command below.  
`$ umakaparser`  

# Required
1. Data that follows [Sparql Builder Metadata ver.2015](http://www.sparqlbuilder.org/doc/sbm_2015sep/) (R1)
2. Relevant ontology file(s) (R2, Optional, multiple files can be added)

A file of R1 can be generated by using [this tool](https://github.com/sparqlbuilder/metadata).
Currently, ontly the Turtle or the N-Triples formats are supported.
Prefixes used in visualization can be included in the ontology file or added as a turtle file.

# Instruction to upload

A directory is generated by executing the command below. You can skip this step unless an ontology file is used for visualization.  
`$ umakaparser build-index {the file of R2} --dist {a path for generating files}`

Then, the following command follows to get a json file to be uploaded to the Umaka Viewer. The `--assets` argument is optional.  
`$ umakaparser build {the file of R1} --assets {the path generated by build-index} --dist {a generating json file for Umaka Viewer}`  

For more details, please check the message shown by executing the tool with `--help`.

## Troubleshooting

When install is failed, please first execute the following command before installing the tool.  
`$ pip install -U setuptools`
