# MatrixPyBridge-MCDR
A Python plugin to sync messages between Minecraft server and Matrix chat rooms. Works like [MatrixSpigotBridge](https://www.spigotmc.org/resources/matrixspigotbridge.96738/).

一个用于在 Minecraft 服务器和 Matrix 聊天室之间同步消息的 Python 插件，类似 [MatrixSpigotBridge](https://www.spigotmc.org/resources/matrixspigotbridge.96738/)。

This is a rewrite of [MatrixSync-MCDR](https://github.com/Mooling0602/MatrixSync-MCDR). For my previous codes not look good, I decide to rewrite a better one, and improve my Python skill while developing this.
> And the previous name of the plugin isn't nice, too.

这是 [MatrixSync-MCDR](https://github.com/Mooling0602/MatrixSync-MCDR) 的重制版。由于之前的代码看起来不太好，我决定重写一个更好的版本，并在开发过程中提升我的 Python 技能。
> 之前的插件名称也不太好听。

## Developing Status 开发状态
Writing source codes still...

还在编写源代码……

i18n will implement later...

多语言支持将稍后完善……

## Dependencies 依赖
- Python
> python>=3.11 is better

- MCDReforged
> Use latest version or at least mcdreforged>=2.14.1

- [Optional, MCDR]AsyncRconClient
> Provide async rcon support

- [Optional, MCDR]ImAPI
> Provide Im message model, so this plugin can work instead of ImAPI's MatrixDriver

- [Optional, MCDR, developing]ImModel
> Instead of full ImAPI, provide Im message model and Im message command source so users in matrix chat rooms can use MCDR commands

- [Optional, MCDR]BatterySaver
> Provide remote battery management in matrix chat room

- [Optional, MCDR]MoreGameEvents
> Provide death and advancements events, so this bridge can transfer game events messages to the matrix chat rooms

- [Optional, MCDR]InitServer
> Provide APIs to manage server configurations like `server.properties` and more

- [Optional, MCDR, developing]MoolingTeleport
> Allow players send, receive, reject and cancel teleport requests in matrix chat rooms

- [Optional, MCDR, developing]UndocMCDRAPIs
> Provide APIs not in MCDR's public documents but usable

- [Optional, PyPI, developing]MoolingLib
> A personal python lib developed by [Mooling0602](https://github.com/Mooling0602)

- And more...
