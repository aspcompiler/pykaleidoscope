# PyKaleidoscope

This is a python implementation of LLVM [Kaleidoscope tutorial](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html).

There are a few changes:

1. The grammar is implemented in [Antlr](https://www.antlr.org/). We then convert the Antlr parse tree to abstract syntax tree (AST).
1. We used [visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern) to implement the code generator.
1. We used [llvmlite](https://github.com/numba/llvmlite) to generate the LLVM intermediate representation (LR).

Each commit roughly follows the lessons in Kaleidoscope Tutorial. To see code for each lesson, just checkout the corresponding commit.

To run code evaluator, look at tet_evaluator.py unit tests.

## Acknowledgement

I have also looked [a github project with the same name](https://github.com/eliben/pykaleidoscope). The main difference is that I used Antlr and visitor pattern.

## Installation

Dependencies are managed by [poetry](https://python-poetry.org/). 

If you do not have poetry, run

```
brew install poetry
```

You will need python 3.9.x. Use your favorite way to create a virtual environment, one way is to run:

```
python3 -m venv .venv
source .venv/bin/activate
```

This will create a virtual environment locally in the .venv folder that poetry will automatically recognize.

Run poetry to install the dependencies:

```
poetry install
```

## Formatting

Code formatting is standardized by [`black`](https://github.com/psf/black) and enforced by the CI. The configuration is found in the `tool-black` section of the [`pyproject.toml`](pyproject.toml). `black` can be run locally:

```shell
$ black kaleidoscope
```

## Linting

```
pylint kaleidoscope
```

## Testing

```
pytest kaleidoscope
```

## Update grammar

Install ANTLR locally following these [instructions](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md). Then run:

```
antlr4 -Dlanguage=Python3 -visitor ./gen4/qasm3.g4
```

This will regenerate the python parser.
