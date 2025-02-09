from flet import app

from project.application.build import building_the_application
from project.application.cascade_control import check_settings, update_settings

if check_settings() == 0:
    update_settings()
    app(target=building_the_application)
