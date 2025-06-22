from mcdreforged.api.all import *  # Type checking will be not happy, but the simplest way to import MCDR documented APIs. Relax anyway, this will be improved later.


def on_load(server: PluginServerInterface, _prev_module):
    server.logger.info("Loading MatrixPyBridge...")


def on_unload(server: PluginServerInterface):
    server.logger.info("Unloading MatrixPyBridge...")
