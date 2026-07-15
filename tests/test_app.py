import pytest
import requests

BASE_URL = "http://localhost:5001"


def test_celsius_to_fahrenheit_unit():
    """Unit test - provjera formule konverzije bez baze/appa."""
    celsius = 25
    fahrenheit = round(((celsius * 1.8) + 32), 2)
    assert fahrenheit == 77.0


def test_celsius_to_fahrenheit_zero():
    celsius = 0
    fahrenheit = round(((celsius * 1.8) + 32), 2)
    assert fahrenheit == 32.0


def test_app_is_reachable():
    """Integration test - provjerava da app radi i odgovara."""
    response = requests.get(BASE_URL, timeout=5)
    assert response.status_code == 200


def test_app_shows_student_and_college():
    """Integration test - provjerava da su STUDENT i COLLEGE env varijable prikazane."""
    response = requests.get(BASE_URL, timeout=5)
    assert "Lara Babić" in response.text
    assert "Algebra Bernays University" in response.text
