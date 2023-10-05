# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Stratus 1.53'
copyright = '2023, Jake Kurtz'
author = 'Jake Kurtz'
release = '1.53'
current_version = '1.53'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []
extensions = ["myst_parser",'sphinx_rtd_theme',"sphinx_multiversion",]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_logo = "../stratus_logo_15.png"
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'versioning.html',
    ],
}