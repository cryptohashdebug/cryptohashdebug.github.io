AUTHOR = 'cryptohashdebug'
SITENAME = 'Entorno Digital.'
SITEURL = ""

PATH = "content"
OUTPUT_PATH = "docs"

TIMEZONE = 'America/Havana'

DEFAULT_LANG = 'es'
STATIC_PATHS = ['static']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Tema
THEME = 'themes/bootstrap2-dark'

# Plugins
PLUGIN_PATHS = ["plugins", "./plugins"]
PLUGINS = ['pelican_solicitud_plugin2', 'tag_cloud']
#PLUGINS = ['pelican_solicitud_plugin2',
#           'pelican_process_graf2',
#           'pelican_aasvg']

# Extensiones de Markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.meta': {},
        'markdown.extensions.wikilinks':{},
        'markdown.extensions.admonition':{}
        # Añada las extensión personalizadas
        #'plugins.pelican_markdown_aasvg': {},
    },
    'output_format': 'html5',
}

#MARKDOWN = {
#    'extension_configs': {
#        'markdown.extensions.extra': {},
#        'markdown.extensions.codehilite': {'css_class': 'highlight'},
#        'markdown.extensions.meta': {},
#        'markdown.extensions.wikilinks':{},
#        'markdown.extensions.admonition':{}
#        # Añada las extensión personalizadas
#        #'plugins.pelican_markdown_aasvg': {},
#    },
#    'output_format': 'html5',
#}