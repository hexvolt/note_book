from flask.ext.assets import Bundle, Environment
from note_book import app

bundles = {
    'libs_js': Bundle(
        'js/lib/jquery-1.11.2.min.js',
        'js/lib/angular.min.js',
        output='js/libs.min.js',
    ),
    'main_js': Bundle(
        'js/base.js',
        filters='yui_js',
        output='js/main.min.js',
    ),
    'main_css': Bundle(
        'less/variables.less',
        'less/utils.less',
        'less/base.less',
        'less/mobile.less',
        output='css/main.min.css',
        filters='less'
    ),
}

assets = Environment(app)
assets.register(bundles)