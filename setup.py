from setuptools import setup


def readme_file_contents():
    with open('README.md') as readme_file:
        data = readme_file.read()
    return data


setup(
    name='honeypot',
    version='1.0.0',
    description='Simple TCP Honeypot',
    long_description=readme_file_contents(),
    author='Nimish',
    author_email='dummy@gmail.com',
    license='MIT',
    packages=['honeypot'],
    zip_safe=False,
    install_requires=[]
)

