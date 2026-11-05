def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_crud_cycle(client):
    item = client.post("/api/v1/items", json={"title": "First"}).json()
    url = f"/api/v1/items/{item['id']}"
    assert client.get(url).json()["title"] == "First"
    assert client.patch(url, json={"title": "Renamed"}).json()["title"] == "Renamed"
    assert client.delete(url).status_code == 204
    assert client.get(url).status_code == 404


def test_validation_and_list(client):
    assert client.post("/api/v1/items", json={"title": ""}).status_code == 422
    for n in range(3):
        client.post("/api/v1/items", json={"title": f"Note {n}"})
    assert [i["title"] for i in client.get("/api/v1/items?limit=2").json()] == ["Note 2", "Note 1"]
