import requests


LAMBDA_URL = (
    "https://s5abygnke43nwtfda6e3b66d640ozrtx.lambda-url.us-east-1.on.aws"
)


def test_lambda_health():

    response = requests.get(
        f"{LAMBDA_URL}/health"
    )

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"