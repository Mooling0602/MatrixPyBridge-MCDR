from collections.abc import Callable
from logging import Logger
from typing import Any
from nio import (
    AsyncClient,
    SyncResponse,
    SyncError,
    MatrixRoom,
    RoomMessageText,
)


class MatrixClient:
    def __init__(
        self,
        homeserver: str,
        user_id: str,
        token: str,
        device_id: str | None = "mcdr",
        logger: Logger | Callable[..., Any] | None = print,
    ):
        self.connected: bool = False
        self.client = AsyncClient(homeserver=homeserver)
        self.client.user_id = user_id
        self.client.access_token = token
        self.client.device_id = device_id
        self.logger = logger
        self.network_status: bool = True

    async def connect(self) -> None:
        if self.connected:
            if self.logger:
                _message = (
                    "You have connected the matrix client, "
                    "please disconnect it before reconnect!"
                )

                if hasattr(self.logger, "info"):
                    self.logger.info(_message)  # pyright: ignore[reportFunctionMemberAccess]
                else:
                    if callable(self.logger):
                        self.logger(f"{_message}")
            return

        async def receive_messages() -> None:
            client = self.client

            async def on_sync_response(response: SyncResponse):
                if hasattr(self.logger, "debug"):
                    self.logger.debug(f"MatrixClient response: {response}")  # pyright: ignore[reportOptionalMemberAccess, reportFunctionMemberAccess]

            async def on_sync_error(response: SyncError):
                self.network_status = False
                _message = f"Sync error with matrix homeserver: {response.status_code}"
                _ansi_color_red = "\033[31m"
                _ansi_reset_color = "\033[0m"
                if not self.logger and not callable(self.logger):
                    print(_ansi_color_red + _message + _ansi_reset_color)
                if hasattr(self.logger, "error"):
                    self.logger.error(_message)  # pyright: ignore[reportFunctionMemberAccess, reportOptionalMemberAccess]
                else:
                    if callable(self.logger):
                        self.logger(_ansi_color_red + _message + _ansi_reset_color)

            client.add_response_callback(on_sync_response, SyncResponse)  # pyright: ignore[reportArgumentType]
            client.add_response_callback(on_sync_error, SyncError)  # pyright: ignore[reportArgumentType]

            async def message_callback(
                room: MatrixRoom, event: RoomMessageText
            ) -> None:  # 处理接受到的消息回调
                raise NotImplementedError()  # 咕咕咕……
