import os

class ArtisanTestCommand(PhpunitTestCommand):

    def find_phpunit_bin(self, directory):
        return 'php artisan test'

    def run_in_terminal(self, command):
        osascript_command = 'osascript '
        sublime_phpunit_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/sublime-phpunit'

        if self.get_setting('phpunit-sublime-terminal', 'Term') == 'iTerm':
            osascript_command += '"' + sublime_phpunit_path + '/open_iterm.applescript"'
            osascript_command += ' "' + command + '"'
        else:
            osascript_command += '"' + sublime_phpunit_path + '/run_command.applescript"'
            osascript_command += ' "' + command + '"'
            osascript_command += ' "PHPUnit Tests"'

        self.lastTestCommand = command
        os.system(osascript_command)

class RunArtisanTestCommand(ArtisanTestCommand):

    def run(self, *args, **kwargs):
        file_name, phpunit_config_path, phpunit_bin, active_view, directory = self.get_paths()

        self.run_in_terminal('cd ' + phpunit_config_path + self.get_cmd_connector() + phpunit_bin + ' ' + file_name)

class RunAllArtisanTestsCommand(ArtisanTestCommand):

    def run(self, *args, **kwargs):
        file_name, phpunit_config_path, phpunit_bin, active_view, directory = self.get_paths()

        self.run_in_terminal('cd ' + phpunit_config_path + self.get_cmd_connector() + phpunit_bin)


class RunSingleArtisanTestCommand(ArtisanTestCommand):

    def run(self, *args, **kwargs):
        file_name, phpunit_config_path, phpunit_bin, active_view, directory = self.get_paths()

        current_function = self.get_current_function(active_view)

        self.run_in_terminal('cd ' + phpunit_config_path + self.get_cmd_connector() + phpunit_bin + ' ' + file_name + " --filter '/::" + current_function + "$/'")

class RunLastArtisanTestCommand(ArtisanTestCommand):

    def run(self, *args, **kwargs):
        file_name, phpunit_config_path, phpunit_bin, active_view, directory = self.get_paths()

        if 'Test' in file_name:
            RunSingleArtisanTestCommand.run(self, args, kwargs);
        elif self.lastTestCommand:
            self.run_in_terminal(self.lastTestCommand)

class RunArtisanTestsInDirCommand(ArtisanTestCommand):

    def run(self, *args, **kwargs):
        file_name, phpunit_config_path, phpunit_bin, active_view, directory = self.get_paths()

        self.run_in_terminal('cd ' + phpunit_config_path + self.get_cmd_connector() + phpunit_bin + ' ' + directory)
