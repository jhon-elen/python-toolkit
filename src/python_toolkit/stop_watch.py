import functools
import time


class StopWatch:
    @staticmethod
    def start() -> float:
        return time.perf_counter()

    @staticmethod
    def duration(start_time: float) -> float:
        return round(time.perf_counter() - start_time, 3)


def timed(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = StopWatch.start()
        result = await func(*args, **kwargs)
        print()
        print(f"\t\t\t\tTiempo transcurrido: {StopWatch.duration(start)} s")
        return result
    return wrapper