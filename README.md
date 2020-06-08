# Difference calculator
[![Maintainability](https://api.codeclimate.com/v1/badges/1d3accb9e09bfeb138d6/maintainability)](https://codeclimate.com/github/Artlyne/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1d3accb9e09bfeb138d6/test_coverage)](https://codeclimate.com/github/Artlyne/python-project-lvl2/test_coverage)
[![Build Status](https://travis-ci.com/Artlyne/python-project-lvl2.svg?branch=master)](https://travis-ci.com/Artlyne/python-project-lvl2)

Utility for finding differences in configuration files. Supports JSON and YAML formats.

### INSTALLATION
To install the package, type the following command in your terminal:
```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.python.org/pypi/ artlyne-gendiff
```
[![asciicast](https://asciinema.org/a/AMn2P72QpjZpW7jMh9aZRHL31.svg)](https://asciinema.org/a/AMn2P72QpjZpW7jMh9aZRHL31)

### USAGE
```
usage: gendiff [-h] [-f {plain,json}] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {plain,json}, --format {plain,json}
                        set format of output
```
example:
```
$ gendiff --format plain first_config.json second_config.yaml
Property 'proxy' was removed
Property 'timeout' was changed. From '50' to '20'
Property 'verbose' was added with value: 'True'
```

### FORMATS

Available three different formats for display the difference.

#### Extended (default)
```
{
    common: {
        setting1: Value 1
      - setting2: 200
        setting3: True
      + setting4: blah blah
      + setting5: {
          key5: value5
          key6: value6
        }
      - setting6: {
          key: value
        }
      - site: {
          base: {'hexlet': 'python'}
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
    }
  - group2: {
      abc: 12345
    }
  + group3: {
      fee: 100500
    }
}
```
[![asciicast](https://asciinema.org/a/cjxAi004Ipwno8AJHU2W81rul.svg)](https://asciinema.org/a/cjxAi004Ipwno8AJHU2W81rul)

#### Plain (optional)
```
Property 'common.setting2' was removed
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: 'complex value'
Property 'common.setting6' was removed
Property 'common.site' was removed
Property 'common.group1.baz' was changed. From 'bas' to 'bars'
Property 'common.group1.group2' was removed
Property 'common.group1.group3' was added with value: 'complex value'
```
[![asciicast](https://asciinema.org/a/Z7u8dqBy0cqJBc3izhVW5eWpf.svg)](https://asciinema.org/a/Z7u8dqBy0cqJBc3izhVW5eWpf)

#### Json (optional)
```
{
  "common": [
    "nested",
    {
      "setting1": [
        "same",
        "Value 1"
      ],
      "setting2": [
        "removed",
        "200"
      ],
      "setting3": [
        "same",
        true
      ],
      "setting4": [
        "added",
        "blah blah"
      ],
      "setting5": [
        "added",
        {
          "key5": "value5",
          "key6": "value6"
        }
      ],
      "setting6": [
        "removed",
        {
          "key": "value"
        }
      ],
      "site": [
        "removed",
        {
          "base": {
            "hexlet": "python"
          }
        }
      ]
    }
  ],
  "group1": [
    "nested",
    {
      "baz": [
        "changed",
        [
          "bas",
          "bars"
        ]
      ],
      "foo": [
        "same",
        "bar"
      ]
    }
  ],
  "group2": [
    "removed",
    {
      "abc": "12345"
    }
  ],
  "group3": [
    "added",
    {
      "fee": "100500"
    }
  ]
}
```
[![asciicast](https://asciinema.org/a/YAKTK3mW3QMbos0oymXqN02SE.svg)](https://asciinema.org/a/YAKTK3mW3QMbos0oymXqN02SE)
