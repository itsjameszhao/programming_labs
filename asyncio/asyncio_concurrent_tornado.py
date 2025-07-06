import asyncio
import time
import requests  # The synchronous/blocking library
import tornado.web
import tornado.ioloop

# --- Configuration ---
PORT = 9000
URL = f"http://127.0.0.1:{PORT}"
N_REQUESTS = 10  # How many requests to make concurrently

# --- 1. The Asynchronous Tornado Web Server (Simulates a slow API) ---
class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        # This simulates a slow network or database call.
        # It's a blocking sleep, but that's fine inside a standard
        # Tornado handler that isn't using `async def`.
        await asyncio.sleep(0.5)
        self.write(f"Slept for 0.5 seconds")

def make_app():
    return tornado.web.Application([(r"/", MainHandler)])

async def run_server():
    """Starts the Tornado server and lets it run forever."""
    app = make_app()
    app.listen(PORT)
    print(f"Tornado server started at {URL}")
    await asyncio.Event().wait() # Keep the server running in the background

# --- 2. The Concurrent Client Code ---

# This is your correct implementation.
async def async_send_blocking_request():
    """
    Sends a single blocking request in a non-blocking way by using
    the asyncio event loop's default executor (a thread pool).
    """
    loop = asyncio.get_running_loop()
    # The `await` hands control back to the event loop until the
    # blocking call, running in another thread, is complete.
    response = await loop.run_in_executor(
        None,  # Use the default ThreadPoolExecutor
        requests.get, # The blocking function to run
        URL    # The argument to pass to requests.get
    )
    return response

async def run_client():
    """
    Runs multiple requests concurrently and measures the total time.
    """
    print("\n--- Client starting ---")
    print(f"Making {N_REQUESTS} requests to {URL} concurrently...")
    
    start_time = time.time()

    # Create all the tasks (coroutines) up front
    tasks = [async_send_blocking_request() for _ in range(N_REQUESTS)]

    # Process responses as they are completed
    status_codes = []
    for i, task in enumerate(asyncio.as_completed(tasks)):
        response = await task
        status_codes.append(response.status_code)
        # print(f"Response #{i+1} received with status: {response.status_code}")

    end_time = time.time()
    total_time = end_time - start_time

    print(f"\nAll {len(status_codes)} responses received.")
    print("--- EXECUTION ANALYSIS ---")
    print(f"Total time taken: {total_time:.2f} seconds")

    # This is the key comparison
    serial_time = 0.5 * N_REQUESTS
    print(f"Theoretical serial time: {serial_time:.2f} seconds")
    if total_time < serial_time * 0.8: # (allow for some overhead)
        print("Conclusion: Requests were executed CONCURRENTLY.")
    else:
        print("Conclusion: Requests were executed SERIALLY.")

async def main():
    # Start the server as a background task
    server_task = asyncio.create_task(run_server())
    
    # Give the server a moment to start up
    await asyncio.sleep(0.1)
    
    # Run the client logic
    await run_client()
    
    # Stop the server task so the program can exit cleanly
    server_task.cancel()
    try:
        await server_task
    except asyncio.CancelledError:
        print("\nTornado server has been shut down.")


if __name__ == "__main__":
    asyncio.run(main())