import logging

from os import system

log = logging.getLogger('pyflix.utils.output')


class Output(object):
    def __init__(self, stream_url, parent):
        self.stream_url = stream_url
        self.parent = parent

    def run(self):
        player_command = self._player()
        command = "%s %s" % (player_command, "")
        log.debug("VLC command: %s" % command)
        system(command)

    def _player(self):
        return ""


class VLCOutput(Output):
    def _player(self):
        command = "vlc %s -q" % self.stream_url
        return command
