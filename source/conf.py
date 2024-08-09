# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "sphinx-test"
copyright = "2024, zk-org"
author = "zk-org"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ["_templates"]
exclude_patterns = []

myst_enable_extensions = ["colon_fence", "html_image"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "insegel"
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]

# The master toctree document.
master_doc = "index"
html_theme_options = {"navigation_depth": 2}
