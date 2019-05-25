from json import load


def get_json_from_file(path):
    try:
        with open(path, 'r') as fh:
            return load(fh)
    except Exception:
        return None


def read_lines_from_file(path):
    try:
        with open(path, 'r') as fh:
            return fh.read().split('\n')
    except IOError:
        return None
