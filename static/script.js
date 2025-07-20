function startCompare() {
  const docId = document.getElementById("docId").value;
  const dataId = document.getElementById("dataId").value;

  // Load PDF
  const pdfViewer = document.getElementById("pdfViewer");
  pdfViewer.src = `/get_pdf?doc_id=${encodeURIComponent(docId)}`;

  // Panel 2: Load extracted fields from PDF
  fetch(`/extract_fields?doc_id=${encodeURIComponent(docId)}`)
    .then(res => res.json())
    .then(data => {
      console.log("Extracted Fields:", data);
      const extractedList = document.getElementById("extractedFieldsList");
      extractedList.innerHTML = "";
      data.forEach(row => {
        const li = document.createElement("li");
        li.textContent = `${row.Field}: ${row.Value}`;
        extractedList.appendChild(li);
      });
    });

  // Panel 3 & 4: Load data from backend
  fetch(`/get_data?data_id=${encodeURIComponent(dataId)}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("form1Content").innerHTML = formatData(data.form1);
      document.getElementById("form2Content").innerHTML = formatData(data.form2);
    });
}

function formatData(obj) {
  return Object.entries(obj)
    .map(([k, v]) => `${k}: ${v}`)
    .join("<br>");
}
