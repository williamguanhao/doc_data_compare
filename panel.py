import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
import pandas as pd

# Simulated backend functions
def extract_fields_from_pdf(doc_id):
    return pd.DataFrame({
        "Field": ["Name", "Date", "Amount"],
        "Value": [f"John Doe ({doc_id})", "2025-07-20", "$1,000"]
    })

def get_data_by_id(data_id):
    return {
        "form1": {
            "Name": f"Alice ({data_id})",
            "Date": "2025-07-19",
            "Amount": "$999"
        },
        "form2": {
            "Name": "Bob",
            "Date": "2025-07-18",
            "Amount": "$1,001"
        }
    }

# Inputs
doc_input = widgets.Text(description="Doc ID:", placeholder="e.g. doc_001")
data_input = widgets.Text(description="Data ID:", placeholder="e.g. 123")
compare_button = widgets.Button(description="Start Comparison", button_style='success')

# Output Panels
pdf_output = widgets.Output()
fields_output = widgets.Output()
form1_output = widgets.Output()
form2_output = widgets.Output()

def start_compare(b):
    doc_id = doc_input.value.strip()
    data_id = data_input.value.strip()

    # Clear previous outputs
    pdf_output.clear_output()
    fields_output.clear_output()
    form1_output.clear_output()
    form2_output.clear_output()

    # Panel 1: PDF Viewer
    with pdf_output:
        display(HTML(f"<h4>Simulated PDF Path</h4><p>/path/to/pdf/{doc_id}.pdf</p>"))

    # Panel 2: Extracted Fields
    df = extract_fields_from_pdf(doc_id)
    with fields_output:
        display(HTML("<h4>Extracted Fields</h4>"))
        display(df)

    # Panel 3 & 4: Backend Data
    data = get_data_by_id(data_id)
    with form1_output:
        display(HTML("<h4>Data Form 1</h4>"))
        for k, v in data["form1"].items():
            display(HTML(f"<b>{k}</b>: {v}"))

    with form2_output:
        display(HTML("<h4>Data Form 2</h4>"))
        for k, v in data["form2"].items():
            display(HTML(f"<b>{k}</b>: {v}"))

compare_button.on_click(start_compare)

# Layout inputs and button
inputs = widgets.HBox([doc_input, data_input, compare_button])

# Layout panels in 2x2 grid using VBox/HBox
row1 = widgets.HBox([pdf_output, fields_output])
row2 = widgets.HBox([form1_output, form2_output])
layout = widgets.VBox([inputs, row1, row2])

display(layout)
