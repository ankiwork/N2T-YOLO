import atexit
from flet import app

from project.application.build import building_the_application
from project.application.backend.cascade_control import check_file_settings, update_launch_settings, cleanup

atexit.register(cleanup)

if check_file_settings() == 0:
    update_launch_settings()
    app(target=building_the_application)
