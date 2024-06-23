# Gendiff (Difference Generator)

---

### Hexlet tests and linter status:
[![Actions Status](https://github.com/MaksimGoryachev/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MaksimGoryachev/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/be6c6ad11b42d051d4c4/maintainability)](https://codeclimate.com/github/MaksimGoryachev/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/be6c6ad11b42d051d4c4/test_coverage)](https://codeclimate.com/github/MaksimGoryachev/python-project-50/test_coverage)
[![GitHub Workflow Status](https://github.com/MaksimGoryachev/python-project-50/actions/workflows/pyci-check.yml/badge.svg)](https://github.com/MaksimGoryachev/python-project-50/actions/workflows/pyci-check.yml)

---

## Description

Difference Generator is a program that determines the difference between two data structures. This is a popular task, for which there are many online services, for example, json diff. A similar mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.

Utility Features:

* Support for different input formats: `yaml`, `json`
* Generating a report in the form of plain text, stylish and json

---

## Install

### Python

Before installing the package, you need to make sure that you have Python version 3.8 or higher installed.

```bash
>> python --version
Python 3.8.0+
```
If you don't have Python installed, you can download and install it
from [the official Python website](https://www.python.org/downloads/).


1. Clone the repository to your computer `git clone https://github.com/MaksimGoryachev/python-project-50`
2. Install the package `make setup`
---

## Usage example:

```sh
gendiff path/to/file1.json  path/to/file2.json
```

[![asciicast](https://asciinema.org/a/wYWZIa1YtvZc2KKFE0OQ4k6nU.svg)](https://asciinema.org/a/wYWZIa1YtvZc2KKFE0OQ4k6nU)

---

```sh
gendiff path/to/file1.yaml  path/to/file2.yaml
```
[![asciicast](https://asciinema.org/a/5Z6aMLJ3iP2BQ0PDnXTvC3ppy.svg)](https://asciinema.org/a/5Z6aMLJ3iP2BQ0PDnXTvC3ppy)

---

```sh
gendiff tests/fixtures/file_nested1.json tests/fixtures/file_nested2.json 
```
[![asciicast](https://asciinema.org/a/iAM3d0QeM2zrSvBvwx9JZHASQ.svg)](https://asciinema.org/a/iAM3d0QeM2zrSvBvwx9JZHASQ)

---

```sh
gendiff --format plain tests/fixtures/file_nested1.json tests/fixtures/file_nested2.json

```
[![asciicast](https://asciinema.org/a/Pjxw2dWtPCx2Kpq2mIW0mBAl2.svg)](https://asciinema.org/a/Pjxw2dWtPCx2Kpq2mIW0mBAl2)

---

```sh
gendiff --format json tests/fixtures/file_nested1.json tests/fixtures/file_nested2.json

```
[![asciicast](https://asciinema.org/a/AO86SqMdxHlKuxGcHsOKfXkHT.svg)](https://asciinema.org/a/AO86SqMdxHlKuxGcHsOKfXkHT)

---