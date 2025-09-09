def caesar_cipher(text: str, shift: int, mode: str = 'encrypt') -> str:
    """
    Шифр Цезаря: шифрование и расшифровка текста.
    Поддерживает русский (с ё) и английский алфавиты.
    """
    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            if 'а' <= char.lower() <= 'я' or char.lower() == 'ё':
                # Русский алфавит
                alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                is_upper = char.isupper()
                char_lower = char.lower()
                index = alphabet.find(char_lower)
                if index != -1:
                    new_index = (index + shift) % len(alphabet)
                    new_char = alphabet[new_index]
                    if is_upper:
                        new_char = new_char.upper()
                    result.append(new_char)
                else:
                    result.append(char)
            elif 'a' <= char.lower() <= 'z':
                # Английский алфавит
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
                is_upper = char.isupper()
                char_lower = char.lower()
                index = alphabet.find(char_lower)
                new_index = (index + shift) % len(alphabet)
                new_char = alphabet[new_index]
                if is_upper:
                    new_char = new_char.upper()
                result.append(new_char)
            else:
                result.append(char)
        else:
            result.append(char)

    return ''.join(result)
