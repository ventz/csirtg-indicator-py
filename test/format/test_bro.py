# -*- coding: utf-8 -*-
from csirtg_indicator.format.zbro import Bro, get_lines
import pytest
from csirtg_indicator import Indicator


@pytest.fixture
def indicator():
    i = {
            'indicator': "example.com",
            'itype': 'fqdn',
            'provider': "me.com",
            'tlp': "amber",
            'confidence': "85",
            'reporttime': '2015-01-01T00:00:00Z'
        }
    return Indicator(**i)


@pytest.fixture
def indicator_unicode(indicator):
    indicator.indicator = 'http://xz.job391.com/down/ï¿½ï¿½ï¿½ï¿½à¿ªï¿½ï¿½@89_1_60'
    return indicator


def test_format_bro(indicator, indicator_unicode):
    data = [indicator, indicator_unicode]

    text = str(Bro(data))
    print(text)
    assert text


def test_format_bro2(indicator, indicator_unicode):
    data = [indicator, indicator_unicode]

    n = list(get_lines(data))
    assert len(n) > 0

if __name__ == '__main__':
    test_format_bro()
