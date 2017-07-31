import setuptools

setuptools.setup(
    name='jupyterlab_git',
    version='0.1.0',
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook',
    ],

    package_data={'jupyterlab_git': ['static/*']},
)

#Hey this is a  comment
# this is another comment
# Third Comment
