from setuptools import setup

setup(
    name='wikipedia_for_humans',
    version='0.3.0',
    packages=['wikipedia_for_humans'],
    url='https://github.com/OpenJarbas/wikipedia_for_humans',
    license='MIT',
    author='jarbasAI',
    install_requires=["requests", "wikipedia-api",
                      "inflection", "quebra_frases"],
    author_email='jarbasai@mailfence.com',
    description='wikipedia for humans'
)
