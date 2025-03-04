from flet import app

from project.application.build import building_the_application
from project.application.backend.cascade_control import check_file_settings, update_file_settings


if check_file_settings() == 0:
    update_file_settings()
    app(target=building_the_application)
    update_file_settings()
