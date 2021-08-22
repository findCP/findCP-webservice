"""
    This file is part of findCP-webservice project.
    Copyright (C) 2020-2021  Alex Oarga  <718123 at unizar dot es> (University of Zaragoza)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../../.env'))

from celery import Celery


celery_app = Celery(
    broker=os.environ.get('CELERY_BROKER_URL'),
    backend=os.environ.get('CELERY_RESULT_BACKEND'),
)

celery_app.conf.update(
    task_track_started=True,
    # Time after which a running job will be interrupted.
    task_time_limit=18000,  # 2 hours
    # Time after which a successful result will be removed.
    result_expires=604800,  # 7 days
    # Always restart workers after finishing.
    worker_max_tasks_per_child=1,
    task_serializer='pickle',
    result_serializer='pickle',
    accept_content=['pickle'],
    imports = (os.environ.get('CELERY_IMPORTS'),)
)
