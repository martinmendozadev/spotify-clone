"""Test views."""

# Django
from django.shortcuts import render


def hello(request):
    """Feed users."""
    data = {
        'username': 'name',
        'age': 'age',
        'email': 'email@example.com',
        'phone': '7771234567',
        'is_verified_account': False,
        'picture': 'null',
    }

    return render(
        request,
        'test/login.html',
        context={
            'data': data
        }
    )
