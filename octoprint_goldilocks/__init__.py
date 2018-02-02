# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

__plugin_name__ = "Goldilocks"



class GoldilocksPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("Goldilocks")


    def get_update(self):
        return dict(
            goldilocks=dict(
                displayName="Goldilocks",
                displayVersion=self._plugin_version,

                type="github_release",
                user="ianmackinnon",
                repo="OctoPrint-Goldilocks",
                current=self._plugin_version,

                pip="https://github.com/ianmackinnon/OctoPrint-Goldilocks/archive/{target_version}.zip"
            )
        )

    def action_handler(self, _comm, _line, action, *args, **kwargs):
        self._logger.info("Goldilocks received \"%s\" action from printer", action)

    def gcode_rewrite_q(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        self._logger.info("Goldilocks Q \"%s\"", cmd)
        return cmd

    def gcode_rewrite_s(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        self._logger.info("Goldilocks S \"%s\"", cmd)
        return cmd

    def gcode_receive(self, comm, line, *args, **kwargs):
        self._logger.info("Goldilocks R \"%s\"", line)
        return line




def __plugin_load__():
    global __plugin_implementation__
    global __plugin_hooks__

    plugin = GoldilocksPlugin()

    __plugin_implementation__ = plugin
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": plugin.get_update,
        "octoprint.comm.protocol.action": plugin.action_handler,
        "octoprint.comm.protocol.gcode.queuing": plugin.gcode_rewrite_q,
        "octoprint.comm.protocol.gcode.sending": plugin.gcode_rewrite_s,
        "octoprint.comm.protocol.gcode.received": plugin.gcode_receive,
    }
