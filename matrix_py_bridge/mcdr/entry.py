from mcdreforged.api.all import PluginServerInterface


def on_load(server: PluginServerInterface, _prev_module):
    server.logger.info("Loading MatrixPyBridge in MCDR...")


def on_server_startup(server: PluginServerInterface):
    server.logger.info("Game message listener will start!")


def on_unload(server: PluginServerInterface):
    server.logger.info("Unloading MatrixPyBridge in MCDR...")
