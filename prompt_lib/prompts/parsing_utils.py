
def retry_parse_fail_prone_cmd(
    func,
    max_retries: int = 3,
    exceptions=(
        ValueError,
        KeyError,
        IndexError,
    ),
):
    def wrapper(*args, **kwargs):
        retries = max_retries
        while retries:
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                retries -= 1
                print(f"An error occurred: {e}. Retrying...")
        return None

    return wrapper
