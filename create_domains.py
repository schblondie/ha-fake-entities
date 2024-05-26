import os
import re
import sys
import ast

# Define the directory for custom components
dir_path = './custom_components/fake_entities'

# Get all Python files in the custom components directory
files = os.listdir(dir_path)
py_files = [f for f in files if f.endswith('.py')]

# Extract domain names from file names
existing_domains = [re.sub('.py$', '', f) for f in py_files]

# Read __init__.py from the custom components directory
with open(os.path.join(dir_path, '__init__.py'), 'r') as f:
    lines = f.readlines()

# Extract the list of domains from the line that starts with DOMAINS
domains_line = [line for line in lines if line.startswith('DOMAINS =')][0]
domains = ast.literal_eval(domains_line.split('=')[1].strip())

# Add new domains from command-line arguments
new_domains = sys.argv[1:]
for domain in new_domains:
    if domain not in domains:
        domains.append(domain)

# Update the line that defines DOMAINS
for i, line in enumerate(lines):
    if line.startswith('DOMAINS ='):
        lines[i] = f'DOMAINS = {domains}\n'

# Write the updated lines back to __init__.py
with open(os.path.join(dir_path, '__init__.py'), 'w') as f:
    f.writelines(lines)

# Create a Python file for each domain if it doesn't exist
for domain in domains:
    if domain not in existing_domains:
        filename = f"{domain}.py"
        with open(os.path.join(dir_path, filename), 'w') as f:
            f.write(f'import logging\n\n"""Fake {domain} Entity for Home Assistant."""\n\nfrom homeassistant.components.{domain} import (\n  # Add import statements here\n)\n\n_LOGGER = logging.getLogger(__name__)\n\nclass Fake{domain}Entity():\n  """Representation of a fake {domain} entity."""\n\n  def __init__(self, name):\n    """Initialize the {domain} entity."""\n    self._name = name\n\n  @property\n  def name(self):\n    """Return the name of the {domain} entity."""\n    return self._name\n\n  # Add more methods and properties here\n')
        print(f"Created {filename}")

# Remove any Python files not in the domains list
for file in py_files:
    if file not in ['__init__.py', 'config_flow.py', 'const.py'] and re.sub('.py$', '', file) not in domains:
        os.remove(os.path.join(dir_path, file))
        print(f"Removed {file}")