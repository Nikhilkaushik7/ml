from setuptools import setup, find_packages
hyphen = '-e .'
def get_requirements(file_path:str)->list[str]:
    with open(file_path) as file: 
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
        if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements

setup(
    name='mlproject',   
    version='0.0.1',
    author='Nikhil Kaushik',
    author_email='nikhilkaushik171@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)