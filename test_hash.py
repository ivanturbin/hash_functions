from hash_function import hash_function

# Пример использования
input_data = b"Hello, World!"
hash_result = hash_function(input_data)
print(hash_result.hex())  # Вывод хэша в шестнадцатеричном формате