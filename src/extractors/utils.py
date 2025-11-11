thonimport os

def ensure_directory(path):
    """
    Ensure the directory exists, create it if not.

    :param path: Directory path to check
    """
    if not os.path.exists(path):
        os.makedirs(path)