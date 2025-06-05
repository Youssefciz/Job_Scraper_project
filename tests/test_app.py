import pytest

# Skip tests if required dependencies are not installed
flask = pytest.importorskip('flask')
requests = pytest.importorskip('requests')
bs4 = pytest.importorskip('bs4')

import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index_route_returns_200(client, monkeypatch):
    monkeypatch.setattr(app, 'render_template', lambda template: 'index')
    response = client.get('/')
    assert response.status_code == 200

@patch('app.scrape_linkedin')
def test_scrape_jobs_returns_json(mock_scrape_linkedin, client, monkeypatch):
    monkeypatch.setattr(app, 'render_template', lambda template: 'index')
    mock_scrape_linkedin.return_value = [
        {'title': 'Test', 'company': 'Company', 'location': 'Location', 'link': 'http://example.com'}
    ]
    response = client.get('/scrape_jobs?keyword=test&page=0')
    assert response.status_code == 200
    data = response.get_json()
    assert 'jobs' in data
    assert 'job_count' in data
    assert data['job_count'] == len(mock_scrape_linkedin.return_value)
