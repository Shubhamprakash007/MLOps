from setuptools import setup, find_packages

HYPHEN = '-e .'
def get_requirements(requirements_file):
    """
    Read the requirements from a requirements file and return them as a list.
    Args:
        requirements_file (str): Path to the requirements file.
    Returns:
        list: List of requirements.
    """
    requirements = []
    with open(requirements_file, 'r') as file:
        requirements = file.readlines()
        # Remove whitespace and newline characters from each requirement
        requirements = [req.strip() for req in requirements]
        # Remove any comments or blank lines
        requirements = [req for req in requirements if req and not req.startswith('#')]
        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
    return requirements


setup(
    name = 'mlops',
    version = '0.0.1',
    description = 'Mlops',
    author = 'Shubham Prakahs',
    author_email = 'shubhampark007@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)