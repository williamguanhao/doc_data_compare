import panel as pn
import pandas as pd
pn.extension()

doc_id = pn.widgets.TextInput(name='Document ID', placeholder='doc_001')
data_id = pn.widgets.TextInput(name='Data ID', placeholder='123')
button = pn.widgets.Button(name='Start Comparison')

output1 = pn.pane.Markdown("")
output2 = pn.pane.DataFrame(pd.DataFrame())
output3 = pn.pane.Markdown("")
output4 = pn.pane.Markdown("")

def extract_fields(doc_id_val):
    return pd.DataFrame({
        "Field": ["Name", "Date", "Amount"],
        "Value": ["John Doe", "2025-07-20", "$1,000"]
    })

def on_click(event):
    output1.object = f"Loaded PDF for `{doc_id.value}`"
    df = extract_fields(doc_id.value)
    output2.object = df
    output3.object = "Form 1: {'Name': 'John'}"
    output4.object = "Form 2: {'Name': 'Doe'}"

button.on_click(on_click)

layout = pn.Column(
    pn.Row(doc_id, data_id, button),
    pn.Row(output1, output2),
    pn.Row(output3, output4)
)

layout.servable()
