import sublime
import sublime_plugin
import os

def plugin_loaded ():
    # Show project in all views of all windows
    for window in sublime.windows ():
        for view in window.views ():
            show_project (view)

def show_project(view):
    # Is there a project file defined?
    project_file = view.window ().project_file_name ()
    if project_file is not None:
        # Get the project filename without path or extension
        project_name = os.path.splitext (os.path.basename (project_file))[0]
        view.set_status ("00ProjectName", "[" + project_name + "]")

# Display the current project name in the status bar
class ProjectInStatusbar(sublime_plugin.EventListener):
    # When you create a new empty file
    def on_new(self, view):
        show_project (view)
