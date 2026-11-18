"""
Tests for WebhookServer.
"""

from unittest.mock import patch

import pytest
from aiohttp.test_utils import TestClient, TestServer

from aioyookassa.contrib.webhook_server import DEFAULT_WEBHOOK_PATH, WebhookServer
from aioyookassa.core.webhook_handler import WebhookHandler


@pytest.fixture
def server():
    """Create WebhookServer instance without IP validation."""
    return WebhookServer(handler=WebhookHandler(), validate_ip=False)


def get_post_paths(app):
    """Return paths of all POST routes registered in the app."""
    return [
        route.resource.canonical
        for route in app.router.routes()
        if route.method == "POST"
    ]


class TestCreateApp:
    """Test WebhookServer.create_app."""

    def test_default_path(self, server):
        """Test that create_app registers route on default path."""
        app = server.create_app()
        assert get_post_paths(app) == [DEFAULT_WEBHOOK_PATH]

    def test_custom_path(self, server):
        """Test that create_app registers route on custom path."""
        app = server.create_app(path="/api/v1/webhooks/yookassa")
        assert get_post_paths(app) == ["/api/v1/webhooks/yookassa"]

    @pytest.mark.asyncio
    async def test_custom_path_handles_requests(self, server):
        """Test that webhook endpoint responds on custom path only."""
        app = server.create_app(path="/payments/yookassa/webhook")
        async with TestClient(TestServer(app)) as client:
            response = await client.post("/payments/yookassa/webhook", data="{")
            assert response.status == 400

            response = await client.post(DEFAULT_WEBHOOK_PATH, data="{")
            assert response.status == 404


class TestRun:
    """Test WebhookServer.run."""

    @pytest.mark.parametrize("path", [DEFAULT_WEBHOOK_PATH, "/custom/webhook"])
    def test_run_uses_create_app(self, server, path):
        """Test that run builds the app via create_app with given path."""
        with patch(
            "aioyookassa.contrib.webhook_server.web.run_app"
        ) as run_app, patch.object(
            server, "create_app", wraps=server.create_app
        ) as create_app:
            server.run(host="127.0.0.1", port=9000, path=path)

        create_app.assert_called_once_with(path=path)
        app = run_app.call_args.args[0]
        assert get_post_paths(app) == [path]
        assert run_app.call_args.kwargs == {"host": "127.0.0.1", "port": 9000}
