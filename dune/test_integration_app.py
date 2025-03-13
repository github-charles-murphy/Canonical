import requests

# According to policy, we run code locally under port 7777
SERVICE_URL="http://localhost:7777"

def test_service_up():
    r = requests.get(SERVICE_URL)
    assert r.status_code == 200

# Check both happy path (blockchain exists) and its opposite (no blockchain)
def test_happypath():
    r = requests.post(SERVICE_URL + '/blockchain', data = {'name': 'ethereum'})
    assert r.status_code == 200
    assert r.json()['exists'] == True

def test_unhappy():
    r = requests.post(SERVICE_URL + '/blockchain', data = {'name': 'bene gesserit'})
    assert r.status_code == 200
    assert r.json()['exists'] == False
