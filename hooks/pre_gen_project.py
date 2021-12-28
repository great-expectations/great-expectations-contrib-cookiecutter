import re
import sys


PROJECT_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9] Expectations$"

project_name = "{{ cookiecutter.project_name }}"

if not re.match(PROJECT_REGEX, project_name):
    print(
        f'ERROR: {project_name} is not a valid project name! Please ensure your project ends with "Expectations"'
    )

    # exits with status 1 to indicate failure
    sys.exit(1)
