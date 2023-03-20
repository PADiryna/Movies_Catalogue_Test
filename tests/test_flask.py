from main import app


def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.request.args.get('list_type', "popular")
    assert response.request.args.get('list_type', "upcoming")
    assert response.request.args.get('list_type', "top_rated")

def test_today_route():
    response = app.test_client().get('/today')
    assert response.status_code == 200


def test_search_route():
    response = app.test_client().get('/search')
    assert response.status_code == 200
    assert response.request.args.get("q", "Matrix")
    