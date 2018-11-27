
#! /bin/sh

clear

export PYTHONPATH=../../../venv/Lib/site-packages/programy:../../../venv/Lib/site-packages/MetOffer-1.3.2.dist-info:.

if [[ -z "${PYTHONPATH}" ]]; then
  echo "PYTHONPATH is undefined"
  exit
fi

python3 -m programy.clients.polling.telegram.client --config ../../config/xnix/config.telegram.yaml --cformat yaml --logging ../../config/xnix/logging.yaml

