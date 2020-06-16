import json
import uuid
from datetime import datetime, date
from IPython.display import display_javascript, display_html


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat("T")
        elif isinstance(obj, date):
            return obj.isoformat()

        return json.JSONEncoder.default(self, obj)


class RenderJSONViewer(object):
    def __init__(self, json_data):
        if isinstance(json_data, dict):
            self.json_str = json.dumps(json_data, cls=CustomJSONEncoder, default=str)
        else:
            self.json_str = json
        self.uuid = str(uuid.uuid4())

    def _ipython_display_(self):
        display_html(
            (
                '<div id="{}" class="jsonViewerDiv" style="height: 600px; width:100%;"></div>'.format(self.uuid),
            ),
            raw=True
        )
        display_javascript(
            (
                """
                require([
                  "https://rawgit.com/CloudCray/jupyter-json-viewer/master/renderjson.js"
                  ], 
                  function() {
                    renderjson.set_show_to_level(1);
                    document.getElementById('%s').appendChild(renderjson(%s));
                });
                """ % (self.uuid, self.json_str),
            ),
            raw=True
        )


def render_json(json_data):
    return RenderJSONViewer(json_data)
