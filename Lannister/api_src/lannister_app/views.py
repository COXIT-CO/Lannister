from loguru import logger

# from django.shortcuts import render

logger.add(
    "loguru.log",
    level="INFO",
    format="{time} {level} {message}",
    retention="30 days",
    serialize=True,  # json format of logs
)

logger.info("Information message")

# Create your views here.
