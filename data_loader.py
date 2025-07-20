import pandas as pd

def get_data_by_id(data_id):
    if data_id == "123":
        return {
            "fields": [
                {"key": "Name", "value": "John Doe"},
                {"key": "Date", "value": "2025-07-20"},
                {"key": "Amount", "value": "$1,000"},
            ],
            "form1": {
                "Name": "John Doe",
                "Date": "2025-07-20",
                "Amount": "$1,000"
            },
            "form2": {
                "Name": "Jane Doe",
                "Date": "2025-07-19",
                "Amount": "$1,000"
            }
        }
    else:
        return {
            "fields": [],
            "form1": {},
            "form2": {}
        }


def extract_fields_from_pdf(doc_id):
    # Simulate extracting a DataFrame from the PDF
    data = {
        "Field": ["Name", "Date", "Amount"],
        "Value": ["John Doe", "2025-07-20", "$1,000"]
    }
    df = pd.DataFrame(data)
    return df