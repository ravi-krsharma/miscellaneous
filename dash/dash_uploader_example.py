from pathlib import Path
import uuid

import dash_uploader as du
import dash
# import dash_html_components as html
# from dash.dependencies import Input, Output, State
from dash import dcc, html, Input, Output, State, callback_context, ctx

app = dash.Dash(__name__)

count = 0

UPLOAD_FOLDER_ROOT = r"C:\tmp\Uploads"
du.configure_upload(app, UPLOAD_FOLDER_ROOT)

def get_upload_component(id):
    return du.Upload(
        id=id,
        text="Drag-and-drop file here",
        text_completed="",
        cancel_button=True,
        disabled=False,
        max_file_size=10000,  # in Mb
        upload_id="Electromagnetics",  # Unique session id
        default_style={"minHeight": "None", "lineHeight": "None"},
        max_files=10,
    )


def get_app_layout():

    return html.Div(
        [
            html.H1('Demo'),
            html.Div(
                [
                    get_upload_component(id='dash-uploader'),
                    html.Div(id='callback-output'),
                ],
                style={  # wrapper div style
                    'textAlign': 'center',
                    'width': '600px',
                    'padding': '10px',
                    'display': 'inline-block'
                }),
            dcc.Store(id="store"),
        ],
        
        style={
            'textAlign': 'center',
        },
    )


# get_app_layout is a function
# This way we can use unique session id's as upload_id's
app.layout = get_app_layout


@du.callback(
    output=Output("callback-output", "children"),
    id="dash-uploader",
)
def get_a_list(uploadedFiles):
    # count +=1
    global count
    count+=1
    print("\nget_a_list", uploadedFiles.uploaded_files)
    # print("\ncount", count)
    data = []
    # if filenames:
    #     with open("filenames.txt", "a") as f:
    #         f.write(str(filenames))
    #     data.append(filenames)
    # else:
    #     data = None
    # return dcc.Store(id={"type": "upload-aedt", "index": "upload"}, data=data)
    return str(uploadedFiles.uploaded_files)



if __name__ == '__main__':
    app.run_server(debug=True)
