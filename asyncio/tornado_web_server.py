import asyncio
import tornado
from random import random

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        sleep_time = random()
        await asyncio.sleep(sleep_time)
        self.write(f"Slept for {sleep_time:.2f} seconds")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(9000)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())