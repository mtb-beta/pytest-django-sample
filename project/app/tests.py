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
    response = client.get('/')
    assert response.status_code == 200
