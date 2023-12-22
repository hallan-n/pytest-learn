from pytest import fixture
from fastapi import FastAPI

@fixture
def fixture_fastapi():
    return FastAPI()