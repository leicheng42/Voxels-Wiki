

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Voxels Wiki'
copyright = '2023, 雷电所 RaidenINST'
author = 'Lei Cheng'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    ]

myst_enable_extensions = [
    "colon_fence",
    "attrs_block",
    "attrs_inline",
    "linkify",
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']


html_theme_options = {
    "repository_url": "https://github.com/leicheng42/Cryptovoxels-Wiki",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_source_button": True,
    "home_page_in_toc": True,
}

html_title = "Voxels Wiki by Raiden INST"
html_logo = "imags/logo.jpg"