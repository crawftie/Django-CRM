# tests/test_views.py
import pytest
from django.urls import reverse
from website.models import Doctor_Record, Hospital_Record, Doctor_Specialism


@pytest.mark.django_db
def test_list_hospitals_view_returns_200(client):
    url = reverse("list_hospitals")
    response = client.get(url)
    assert response.status_code == 200
    print("Response for List Hospitals View:", response.content)

@pytest.mark.django_db
def test_list_doctors_view_returns_200(client):
    url = reverse("list_doctors")
    response = client.get(url)
    assert response.status_code == 200
    print("Response for List Doctors View:", response.content)

@pytest.mark.django_db
def test_list_specialisms_view_returns_200(client):
    url = reverse("list_specialisms")
    response = client.get(url)
    assert response.status_code == 200
    print("Response for List Specialisms View:", response.content)