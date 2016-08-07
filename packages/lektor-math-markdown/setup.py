from setuptools import setup

setup(
    name='lektor-math-markdown',
    version='0.1',
    author=u'Yoav Ram',
    author_email='yoavram+github@gmail.com',
    license='MIT',
    py_modules=['lektor_math_markdown'],
    install_requires=[
        'mistune_contrib'
    ],
    entry_points={
        'lektor.plugins': [
            'math-markdown = lektor_math_markdown:MathMarkdownPlugin',
        ]
    }
)
