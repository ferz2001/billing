from werkzeug.security import generate_password_hash, check_password_hash

password = 'admin'

hashed_password = generate_password_hash(password)


print("Хэш для слова 'admin':", hashed_password)
print(check_password_hash(hashed_password, password))
