#!/bin/bash
cd /home/vszabo/PycharmProjects/bibtex-to-xls/ || exit
# shellcheck source=/dev/null
. venv/bin/activate
python3 bib
