
import webbrowser
import socket
import asyncio
import threading
url = "https://libgen.is/"
async def fetch(i):
    #sock = socket.socket()
    
    r, w = await asyncio.open_connection(
        'libgen.is', 80)
    request = 'GET {} HTTP/1.0\r\nHost: libgen.is\r\n\r\n'.format(url)
    w.write(request.encode())
    await w.drain()
    
    response = b''
    print('start-', i)
    chunk = await r.read(4096)
    while chunk:
        response += chunk
        chunk = await r.read(4096)
    print('recieved-', i)

def start_browser():
    import time
    s = time.perf_counter()
    threads = []
    for x in range(10):
        obj = threading.Thread(target=fetch, args=(x,))
        threads.append(obj)
    for a in threads:
        a.start()
    for b in threads:
        b.join()
        
    
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

#start_browser()
async def main():
    await asyncio.gather(fetch(0),fetch(1),fetch(2),fetch(3),fetch(4),fetch(5), fetch(6), fetch(7), fetch(8), fetch(9))
if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
