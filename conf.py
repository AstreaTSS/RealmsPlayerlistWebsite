# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Realms Playerlist Bot"
copyright = "2020-present, AstreaTSS"
author = "AstreaTSS"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_immaterial",
    "sphinx.ext.autosectionlabel",
    "hoverxref.extension",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "env"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_immaterial"
html_static_path = ["_static"]
html_title = "Realms Playerlist Bot"
html_theme_options = {
    # "font": False,

    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
        "admonition": {
            "note": "octicons/tag-16",
            "abstract": "octicons/checklist-16",
            "info": "octicons/info-16",
            "tip": "octicons/squirrel-16",
            "success": "octicons/check-16",
            "question": "octicons/question-16",
            "warning": "octicons/alert-16",
            "failure": "octicons/x-circle-16",
            "danger": "octicons/zap-16",
            "bug": "octicons/bug-16",
            "example": "octicons/beaker-16",
            "quote": "octicons/quote-16",
        },
    },

    "features": [
        "navigation.expand",
        "navigation.sections",
        "navigation.top",
        "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
    ],

    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "light-green",
            "accent": "light-green",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "light-green",
            "accent": "light-green",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],

    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/AstreaTSS/RealmsPlayerlistWebsite",
            "name": "Website source on github.com",
        },
    ],

    "repo_url": "https://github.com/AstreaTSS/RealmsPlayerlistBot",
    "repo_name": "RealmsPlayerlistBot",
    "repo_type": "github",

    "globaltoc_collapse": True,
    "toc_title_is_page_title": True,
}

# TODO: add opengraph, favicon