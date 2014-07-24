Design Notes
============

## Requirements

1. Define a schema to validate a tree of file and directory nodes for:
    a. name
    b. mode
    c. node type
    d. frequency
    e. depth
2. Write a library for processing the schema file and then validating a given directory and file tree
3. Provide a command line interface


## Use Cases

The goal of this project is to make a tool to ease verifying file structures
meet certain predefined conventions. The reason is not intended to be used as
a hammer with which to beat developers over the head with, but rather a tool
to aid testing of automated file system construction.

1. Enforce conventions for application project directories.
2. Enforce project file system tree layout.
3. Diagnose project build problems introduced by an invalid file system tree.


## Random Notes


## Stories

1. user describes file and folder structure in a text file in a directory
2. user validates project by running a console command
3. user validates project in IDE project views
4. user imports common rules to avoid duplication