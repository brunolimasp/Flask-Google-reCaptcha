from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='Flask_Google_reCaptcha',
    version='0.0.1',
    url='https://github.com/brunolimasp/Flask_Google_reCaptcha',
    license='MIT License',
    author='Bruno Augusto',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='augusto.han@gmail.com',
    keywords=['flask', 'recaptcha', "google"],
    description=u'Exemplo de pacote PyPI',
    install_requires=['requests', 'MarkupSafe'],
    )