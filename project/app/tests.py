import pytest

from app.models import MyAppModel


@pytest.mark.django_db
def test_myapp_is_empty():
    mymodel = MyAppModel(title="sample model", content="test")
    assert mymodel.is_empty


@pytest.mark.django_db
def test_myapp_isnot_emmpty():
    mymodel = MyAppModel(title="sample model")
    assert not mymodel.is_empty


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.parametrize("path, status_code", (["/", 200], ["", 200], ["hello", 404],))
def test_url_response(client, path, status_code):
    response = client.get(path)
    assert response.status_code == status_code
