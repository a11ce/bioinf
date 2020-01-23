# Example python makefile pipeline

This dir shows the following example pipeline:
```
rawText.ls
    +
    |
    |
    v
procText.ls      hungarian.tl
    +            +
    |            |
    +------->+<--+
             v
        output.ls
 ```
To run, just type `make` or `make output.ls`.

# Data files

- `rawText.ls` is a list of Hungarian strings to transliterate. Our imaginary data source has replaced all the spaces with [SPACE].
- `procText.ls` is the same list of strings, but with [SPACE] replaced with a space.
- `output.ls` is the final output, a list of transliterated strings.

# Process files

- `replaceSpaces.py` replaces [SPACE] in the input and prints the result.
- `transliterate.py` transliterates given text using the transform rules supplied. See [here](https://github.com/a11ce/transliterator) for more information.