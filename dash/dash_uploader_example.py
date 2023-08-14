from pathlib import Path
import uuid
import dash_uploader as du
import dash
from dash import dcc, html, Input, Output, State, callback_context, ctx

app = dash.Dash(__name__)



UPLOAD_FOLDER_ROOT = r"C:\tmp\Uploads"
du.configure_upload(app, UPLOAD_FOLDER_ROOT)

def get_upload_component(id):
    return du.Upload(
        id=id,
        text="Drag-and-drop file here",
        text_completed="Upload completed for: ",
        cancel_button=True,
        disabled=False,
        max_file_size=10000,  # in Mb
        upload_id="Electromagnetics",  # Unique session id
        default_style={"minHeight": "None", "lineHeight": "None"},
        max_files=10,
        text_disabled="The uploader is disabled",
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
    output=Output("dash-uploader", "text"),
    id="dash-uploader",
)
def get_a_list(uploadedFiles):

    #uploadedFiles.uploaded_files gives a list of Path objects containing the full path to the uploaded files
    list_of_files = uploadedFiles.uploaded_files
    file_names = []
    
    if list_of_files:
        for files in list_of_files:
            file_names.append(str(files).split("\\")[-1])
            
    return f"Upload successful for: {str(file_names)}"



if __name__ == '__main__':
    app.run_server(debug=True)
