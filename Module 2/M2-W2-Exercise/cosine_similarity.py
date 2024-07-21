import numpy as np


def compute_cosine(v1, v2):
    dot_product = np.dot(v1, v2)
    v1_len = np.linalg.norm(v1)
    v2_len = np.linalg.norm(v2)
    cos_sim = dot_product/(v1_len*v2_len)
    return cos_sim
