from flask.ext.assets import Bundle, Environment
from note_book import app

bundles = {
    'libs_js': Bundle(
        'js/lib/jquery-1.11.2.min.js',
        'js/lib/angular.min.js',
        'js/lib/bootstrap.min.js',
        output='js/libs.min.js',
    ),
    'libs_css': Bundle(
        'less/bootstrap.less',
        'less/bootstrap-theme.less',
        output='css/libs.min.css',
        filters='less'
    ),
    'main_js': Bundle(
        'js/base.js',
        filters='yui_js',
        output='js/main.min.js',
    ),
    'main_css': Bundle(
        'less/base.less',
        output='css/main.min.css',
        filters='less'
    ),
}

assets = Environment(app)
assets.register(bundles)