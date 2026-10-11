import asyncio
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier(app_name="PAUSA")

async def main():
    await notifier.send(title="Hello world!", message="Sent from Python")

asyncio.run(main())


