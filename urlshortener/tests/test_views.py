import pytest
from rest_framework.test import APIClient
from rest_framework.reverse import reverse


@pytest.fixture(scope='module')
def api_client():
    return APIClient()


@pytest.fixture(scope='module')
def shorten_endpoint():
    return reverse('url_shorten')


@pytest.fixture(scope='module')
def urls_list_endpoint():
    return reverse('urls_list')


@pytest.fixture(scope='module')
def valid_shorten_jsons():
    return [
        {'long_text': 'http://test.com/test/test/test/test/test/111'},
        {'long_text': 'http://test.com/test/test/test/test/test/222'}
    ]


@pytest.mark.django_db
@pytest.mark.parametrize('invalid_shorten_json',
                         [
                             {'long_text': 'normal_text'},
                             {'long_text': ''},
                             {'any_key': 'http://test.com/test/test'},
                             {'': 'http://test.com/test/test'}
                         ]
                         )
def test_shorten_invalid_json(api_client, shorten_endpoint, invalid_shorten_json):
    '''test getting bad request response for invalid request json'''
    response = api_client.post(shorten_endpoint, invalid_shorten_json)
    assert response.status_code == 400


@pytest.mark.django_db
def test_shorten_once(api_client, shorten_endpoint, valid_shorten_jsons):
    '''test shorten a url first request'''
    response = api_client.post(shorten_endpoint, valid_shorten_jsons[0])
    assert response.status_code == 201
    keys = ('short_text', 'visits_count')
    for key in keys:
        assert key in response.json()
    assert response.json()['visits_count'] == 1


@pytest.mark.django_db
def test_shorten_twice(api_client, shorten_endpoint, valid_shorten_jsons):
    '''test shorten a url again requests'''
    first_response = api_client.post(shorten_endpoint, valid_shorten_jsons[0])
    second_response = api_client.post(shorten_endpoint, valid_shorten_jsons[0])
    assert second_response.status_code == 200
    first_resonse_json = first_response.json()
    second_resonse_json = second_response.json()
    assert second_resonse_json['visits_count'] == 2
    assert second_resonse_json['short_text'] == first_resonse_json['short_text']


@pytest.mark.django_db
def test_urls_list(api_client, shorten_endpoint, urls_list_endpoint, valid_shorten_jsons):
    '''test listing urls'''
    for valid_json in valid_shorten_jsons:
        api_client.post(shorten_endpoint, valid_json)
    response = api_client.get(urls_list_endpoint)
    assert response.status_code == 200
    assert len(response.json()) == len(valid_shorten_jsons)


@pytest.mark.django_db
@pytest.mark.parametrize('url_id,response_code', [(1, 200), (2, 404)])
def test_urls_retrieve(api_client, shorten_endpoint, valid_shorten_jsons, url_id, response_code):
    '''test retrieving a url (found and not found)'''
    api_client.post(shorten_endpoint, valid_shorten_jsons[0])
    url_retrieve_endpoint = reverse('url_retrieve', kwargs={'pk': url_id})
    response = api_client.get(url_retrieve_endpoint)
    assert response.status_code == response_code
