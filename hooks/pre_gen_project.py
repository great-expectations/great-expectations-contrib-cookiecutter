import sys

# Check for 'Expectations' suffix
package_name = "{{ cookiecutter.package_name }}"
package_slug = "{{ cookiecutter.package_slug }}"
for value in (package_name, package_slug):
    if not value.lower().endswith("expectations"):
        print("ERROR: Your package name is not valid (did not end with 'Expectations')")
        sys.exit(1)

# Check for required values
package_description = "{{ cookiecutter.package_description }}"
github_username = "{{ cookiecutter.github_username }}"
for value in (package_description, github_username):
    if "Required" in value:
        print("ERROR: You did not complete a required field")
        sys.exit(2)
