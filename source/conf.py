# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cloudflare APJC - Developer Labs'
copyright = '2023, Cloudflare, Inc'
author = 'Tony Sangha, Nathan Neo'
# release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
# html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "screencaps/cf_logo.svg"
html_favicon = "screencaps/favicon.ico"
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}
html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'APJC Developer Labs',

    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://devlabs.cfapjc.dev',

    # Set the color and the accent color
    # 'color_primary': 'blue',
    # 'color_accent': 'light-blue',
    'theme_color': '3E74FF',

    # Set the repo location to get a badge with stats
    # 'repo_url': 'https://github.com/project/project/',
    # 'repo_name': 'Project',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}
# html_theme_options = {
#     'base_url': 'https://devlabs.cfapjc.dev',
#     # 'canonical_url': '',
#     # 'analytics_id': 'UA-142045439-1',  # Provided by Google in your dashboard
#     'logo_only': False,
#     'display_version': False,
#     'color_primary': 'blue',
#     'color_accent': 'light-blue',
#     'prev_next_buttons_location': 'bottom',
#     'style_external_links': False,
#     'style_nav_header_background': '#353131',
#     # Toc options
#     'collapse_navigation': True,
#     'sticky_navigation': True,
#     'navigation_depth': 4,
#     'includehidden': True,
#     'titles_only': False
# }
