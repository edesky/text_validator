Scanned text validator
======================

**under development**

[CZ] Nástroj na odhadnutí kvality naskenovaného textu, vrací hodnoty 0..1, čím blíž 1, tím líp.

A tool validating text from scanned document. Output is a number 0..1, which represents estimated quality of the text (more is better).

Usage
-----
```
$ python lib/validate.py
usage: test.py [-h] --text TEXT [--short]
test.py: error: argument --text is required
```
```
$ python lib/validate.py --text "blah||fo0"
```

Contribute
----------

MIT license