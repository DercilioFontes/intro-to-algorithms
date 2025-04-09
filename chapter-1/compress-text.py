def compress_text(text):
    compressed= ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1
    compressed += text[-1] + str(count)
    return compressed

# Example usage
print(compress_text("aaabbcdeee"))
print(compress_text("aabbccdd"))
print(compress_text("Sample text to compress."))