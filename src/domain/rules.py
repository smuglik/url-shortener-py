import secrets


class UrlShortenerRule:
    """Implementation of the UrlShortenerRule"""

    @staticmethod
    def generate_short_url() -> str:
        """Generate url shortener"""
        return secrets.token_urlsafe(16)
