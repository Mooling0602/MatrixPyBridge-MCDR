from typing import Optional
from logging import Logger
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
        device_id: Optional[str] = "mcdr",
        logger: Optional[Logger, callable] = print,
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
                message = (
                    "You have connected the matrix client, "
                    "please disconnect it before reconnect!"
                )

                if hasattr(self.logger, "info"):
                    self.logger.info(message)
                else:
                    self.logger(message)
            return

        async def receive_messages() -> None:
            client = self.client

            async def on_sync_response(response: SyncResponse):
                if hasattr(self.logger, "debug"):
                    self.logger.debug(f"MatrixClient response: {response}")

            def on_sync_error(response: SyncError):
                self.network_status = False
                message = (
                    "Sync error with matrix homeserver: "
                    f"{response.status_code}"
                )
                RED = "\033[31m"
                RESET = "\033[0m"
                if not self.logger:
                    print(RED + message + RESET)
                if hasattr(self.logger, "error"):
                    self.logger.error(message)
                else:
                    self.logger(RED + message + RESET)

            client.add_response_callback(on_sync_response, SyncResponse)
            client.add_response_callback(on_sync_error, SyncError)

            async def message_callback(
                room: MatrixRoom, event: RoomMessageText
            ) -> None:
                raise NotImplementedError()
