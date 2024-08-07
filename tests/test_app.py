from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api.app import app


def test_root_deve_retornar_ok_e_salut_mundo():
    client = TestClient(app) # Arrange

    response = client.get('/') # Act

    assert response.status_code == HTTPStatus.OK # Assert
    assert response.json() == {'message': 'Salut, Mundo!'} # Assert
