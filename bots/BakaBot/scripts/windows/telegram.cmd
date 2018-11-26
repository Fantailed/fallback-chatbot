@echo off

CLS

IF NOT DEFINED PYTHONPATH (
    ECHO PYTHONPATH not set, trying to set...
    SET PYTHONPATH=..\..\..\venv\Lib\site-packages\programy;..\..\..\venv\Lib\site-packages\MetOffer-1.3.2.dist-info;.
    python -m programy.clients.polling.telegram.client --config ..\..\config\windows\config.telegram.yaml --cformat yaml --logging ..\..\config\windows\logging.yaml
) ELSE (
    python -m programy.clients.polling.telegram.client --config ..\..\config\windows\config.telegram.yaml --cformat yaml --logging ..\..\config\windows\logging.yaml
)