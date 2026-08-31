import math

vector_a = [1, 1, 0]
vector_b = [1, 0, 1]

dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

magnitude_a = math.sqrt(sum(a * a for a in vector_a))
magnitude_b = math.sqrt(sum(b * b for b in vector_b))

cosine_similarity = dot_product / (magnitude_a * magnitude_b)

print(f"Cosine Similarity: {cosine_similarity:.2f}")