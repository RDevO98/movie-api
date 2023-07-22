from jwt import encode, decode

# use dotenv for get key (data=""movie-api", password="dev")
def create_token(data: dict) -> str:
    token: str = encode(
        payload=data,
        key="672QDxrHY4zu+HkAJ3Tixw==",
        algorithm="HS256"
    )
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(
        token,
        key="672QDxrHY4zu+HkAJ3Tixw==",
        algorithms=['HS256']
    )
    return data