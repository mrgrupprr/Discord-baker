import os
import tempfile
import pytest

pytest.importorskip('requests')

import application


def test_backup_creates_file(tmp_path):
    app = application.application
    original_dir = application.BACKUP_DIR
    application.BACKUP_DIR = str(tmp_path)
    if not os.path.exists(application.BACKUP_DIR):
        os.makedirs(application.BACKUP_DIR)
    with app.test_client() as client:
        resp = client.post('/backup', json={'key': application.exchangepass})
        assert resp.data == b'success'
        files = list(tmp_path.iterdir())
        assert len(files) == 1
    application.BACKUP_DIR = original_dir
