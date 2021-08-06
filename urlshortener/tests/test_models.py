import pytest
from datetime import datetime
from ..models import URL
from ..constants import BASE_URL, HASH_NBYTES


@pytest.fixture(scope='module')
def valid_url_object():
    return URL(long_text='http://test.com/test/test/test/test/test/111')


@pytest.mark.django_db
def test_save_url(valid_url_object):
    valid_url_object.save()
    assert valid_url_object.hash is not None
    assert len(valid_url_object.hash)//1.3 == HASH_NBYTES
    assert valid_url_object.short_text == f'{BASE_URL}{valid_url_object.hash}'
    assert str(valid_url_object) == valid_url_object.short_text
    assert valid_url_object.visits_count == 0


@pytest.mark.django_db
def test_visit_url(valid_url_object):
    valid_url_object.save()
    valid_url_object.visit()
    assert valid_url_object.visits_count == 1
    valid_url_object.visit()
    assert valid_url_object.visits_count == 2
