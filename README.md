This repo serves as a playground to create a simple python package and to test [Travis CI](https://travis-ci.org).

# Travis CI

In Travis CI, you need only a [`.travis.yml`](.travis.yml) file.

```
language: python
python:
  - "2.7"
# command to run tests
script:
  - python tests/hello.py
```

The script section tells Travis what _tests_ to run.
