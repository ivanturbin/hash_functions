import hashlib

def hash_function(input_bytes: bytes) -> bytes:
    """
    Вычисляет SHA-256 хэш для входного массива байт.
    
    Args:
        input_bytes (bytes): Входной массив байт произвольной длины
    
    Returns:
        bytes: Хэш длиной 32 байта
    """
    return hashlib.sha256(input_bytes).digest()