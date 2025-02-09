import atexit
from flet import app

from project.application.build import building_the_application
from project.application.cascade_control import check_settings, update_launch_settings, cleanup

atexit.register(cleanup)

if check_settings() == 0:
    update_launch_settings()
    app(target=building_the_application)
