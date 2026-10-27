import logging
import time

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        # Pass request down the chain to the view
        response = self.get_response(request)

        # Calculate execution duration
        duration = time.time() - start_time

        # Format and log the request summary
        logger.info(f"{request.method} {request.path} - {response.status_code} - {duration:.2f}s")

        return response