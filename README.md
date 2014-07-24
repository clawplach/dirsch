dirsch
======

Directory and filename schema generation and validation.

```sh
# Generate a schema file named `.dirsch.yml` from the current directory
dirsch generate

>> ls .dirsch*
.dirsch.yml

>> # Validate the current directory tree using the `.dirsch.yml` schema file
>> dirsch validate
valid
```
