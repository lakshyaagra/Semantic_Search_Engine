def chunk_text(text, chunk_size=100, overlap=20):
    words = text.split()

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size

        chunk = " ".join(words[start:end])
        chunks.append(chunk)

        if end >= len(words):
            break

        start = end - overlap

    return chunks


# if __name__ == "__main__":

#     with open("data/python.txt", "r", encoding="utf-8") as file:
#         text = file.read()

#     configurations = [
#         (50, 10),
#         (100, 20),
#         (200, 40)
#     ]

#     for size, overlap in configurations:

#         chunks = chunk_text(
#             text,
#             chunk_size=size,
#             overlap=overlap
#         )

#         print(f"\nChunk size: {size}, Overlap: {overlap}")
#         print("Number of chunks:", len(chunks))
#         print("First chunk:", chunks[0][:150])