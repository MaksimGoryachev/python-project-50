# Gendiff (Difference Calculator)

---

### Hexlet tests and linter status:
[![Actions Status](https://github.com/MaksimGoryachev/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MaksimGoryachev/python-project-50/actions)

---

## Description

Difference Calculator is a program that determines the difference between two data structures. This is a popular task, for which there are many online services, for example, json diff. A similar mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.

Utility Features:

Support for different input formats: yaml, json
Generating a report in the form of plain text, stylish and json

---

## Usage example:

gendiff --format plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False

Setting "group1.baz" was updated. From 'bas' to 'bars'

Section "group2" was removed

---
