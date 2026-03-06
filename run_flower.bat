@echo off
REM Launch Flower dashboard for Celery monitoring
celery -A workers flower
pause
