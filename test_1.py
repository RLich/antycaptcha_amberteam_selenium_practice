import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def exercise(app):
    app.open_home_page()
    app.enter_first_exercise()