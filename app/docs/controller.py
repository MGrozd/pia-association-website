from pathlib import Path

from flask import send_file

from . import documents

@documents.route('/statute')
def statute():
    path = Path(__file__).parent / 'static' / 'assets' / 'STATUT.pdf'
    return send_file(path, as_attachment=True)