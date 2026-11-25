# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    # Outline:
    #   restate: one async task per number returning n * 2, run together,
    #   results returned in the same order as numbers.
    #   Example: [1,2,3,4] -> [2,4,6,8]
    #   approach: helper coroutine doubles one number; build a list of them
    #   and await asyncio.gather(*coros).
    async def double(n):
        return n * 2

    coros = [double(n) for n in numbers]
    return await asyncio.gather(*coros)


async def fastest(jobs):
    # Outline:
    #   restate: start all jobs at once; return the label of the first to finish.
    #   example: [("A",0.06) , ("B",0.02) , ("C",0.04)] - "B"
    #   approach: helper sleeps then returns label: loop over as_completed
    #   and return the first result.
    async def run_job(label, delay):
        await asyncio.sleep(delay)
        return label

    coros = [run_job(label, delay) for label, delay in jobs]
    for finished in asyncio.as_completed(coros):
        return await finished



def echo_once(host, port, message):
    # Outline:
    #   restate: connect to (host, port), send message, return the reply as a string.
    #   Example: echo_once("127.0.0.1", 50011, "hello") - "hello"
    #   approach: Tcp socket, connect, sendall(encoded), recv, decode.
    with socket.socket(socket.Af_INET , socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        data = s.recv(1024)
    return data.decode()


def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass


if __name__ == "__main__":
    main()
