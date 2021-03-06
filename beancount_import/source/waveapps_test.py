import os

import pytest

from .source_test import check_source_example

testdata_dir = os.path.realpath(
    os.path.join(
        os.path.dirname(__file__), '..', '..', 'testdata', 'source',
        'waveapps'))

examples = [
    'test_basic',
    'test_matching',
]


@pytest.mark.parametrize('name', examples)
def test_source(name: str):
    check_source_example(
        example_dir=os.path.join(testdata_dir, name),
        source_spec={
            'module': 'beancount_import.source.waveapps',
            'receipt_directory': testdata_dir,
            'link_prefix': 'waveapps.',
        },
        replacements=[(testdata_dir, '<testdata>')])
