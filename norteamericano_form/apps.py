# -*- coding: utf-8 -*-

from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import PluginSettings, PluginURLs, ProjectType, SettingsType


class NorteamericanoCustomFormConfig(AppConfig):
    name = 'norteamericano_form'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'norteamericano_form',
                PluginURLs.REGEX: r'^norteamericano_form/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        },
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.COMMON: {
                    PluginSettings.RELATIVE_PATH: 'settings.common'},
            },
        }
    }

    def ready(self):
        pass
