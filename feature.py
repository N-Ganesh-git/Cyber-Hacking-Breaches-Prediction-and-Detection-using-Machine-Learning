import re
from urllib.parse import urlparse
import numpy as np


def extract_features_from_url(url: str):
    """
    MUST match the exact feature logic used during training.
    Returns a 1D list of 22 numeric features.
    """
    try:
        url = str(url)
    except:
        url = ""

    parsed = urlparse(url)

    hostname = parsed.netloc
    path = parsed.path
    query = parsed.query

    length_url = len(url)
    length_hostname = len(hostname)
    count_dot = url.count('.')
    count_hyphen = url.count('-')
    count_at = url.count('@')
    count_qmark = url.count('?')
    count_equal = url.count('=')
    count_slash = url.count('/')
    count_digit = sum(c.isdigit() for c in url)
    count_alpha = sum(c.isalpha() for c in url)

    ratio_digits = count_digit / (length_url + 1e-5)
    ratio_alpha = count_alpha / (length_url + 1e-5)

    has_ip = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    has_https_in_domain = 1 if ('https' in hostname.lower() and not url.lower().startswith('https')) else 0
    has_login = 1 if 'login' in url.lower() else 0
    has_secure = 1 if 'secure' in url.lower() else 0
    has_bank = 1 if 'bank' in url.lower() else 0

    length_path = len(path)
    count_path_slash = path.count('/')
    count_query_params = query.count('&') + (1 if '=' in query else 0)

    tld_len = 0
    if '.' in hostname:
        tld_len = len(hostname.split('.')[-1])

    features = [
        length_url,
        length_hostname,
        count_dot,
        count_hyphen,
        count_at,
        count_qmark,
        count_equal,
        count_slash,
        count_digit,
        count_alpha,
        ratio_digits,
        ratio_alpha,
        has_ip,
        has_https_in_domain,
        has_login,
        has_secure,
        has_bank,
        length_path,
        count_path_slash,
        count_query_params,
        tld_len,
    ]

    return features


class FeatureExtraction:
    """
    Small wrapper class, like in your old project.
    """

    def __init__(self, url: str):
        self.url = url

    def get_features_array(self):
        """
        Returns features as shape (1, n_features) numpy array
        ready for model.predict().
        """
        features = extract_features_from_url(self.url)
        return np.array(features, dtype=float).reshape(1, -1)
