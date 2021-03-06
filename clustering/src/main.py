from src.TimerHandler import TimerHandler
from fastapi import FastAPI, Request, Response, BackgroundTasks
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(process)d] [%(levelname)s] [%(name)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Start timer-thread on application startup
timer_handler = TimerHandler()
timer_handler.startTimerThread()

app = FastAPI()


@app.post("/trigger")
async def trigger(request: Request, response: Response, background_tasks: BackgroundTasks):
    logger.info("Trigger received")
    # Restart Timer-Thread if needed to query for new Task instantly (will not stop a currently running computation)
    background_tasks.add_task(timer_handler.restartTimerThread)
    return {'Trigger received'}
