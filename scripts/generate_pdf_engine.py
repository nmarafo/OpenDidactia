import os
import subprocess
import fitz

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OUTPUT_DIR = os.path.join(REPO_ROOT, "docs")

CSS_STYLES = """
@page {
    size: A4 portrait;
    margin: 6mm 9mm 6mm 9mm;
}
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background: #fff;
    font-size: 6.9pt;
    line-height: 1.18;
}
.page {
    width: 100%;
    height: 284mm;
    max-height: 284mm;
    position: relative;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.page:last-child {
    page-break-after: avoid;
}

/* Header */
.top-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding-bottom: 3px;
    border-bottom: 2px solid #0f3b75;
    margin-bottom: 4px;
}
.header-left .org-title {
    font-size: 8.8pt;
    font-weight: 800;
    color: #0f3b75;
    letter-spacing: 0.3px;
    text-transform: uppercase;
}
.header-left .org-sub {
    font-size: 6.8pt;
    color: #334155;
    font-weight: 500;
    margin-top: 1px;
}
.header-right .badge-box {
    border: 1.5px solid #0f3b75;
    border-radius: 3px;
    padding: 2px 7px;
    text-align: right;
    background: #f8fafc;
}
.header-right .badge-title {
    font-size: 6.8pt;
    font-weight: 800;
    color: #0f3b75;
    letter-spacing: 0.4px;
}
.header-right .badge-sub {
    font-size: 7.2pt;
    font-weight: 800;
    color: #b91c1c;
    letter-spacing: 0.4px;
}

/* Banner */
.banner {
    background: linear-gradient(135deg, #0e3569 0%, #164e8d 100%);
    border-radius: 3px;
    padding: 4px 8px;
    color: #fff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 4px;
}
.banner-title {
    font-size: 9.8pt;
    font-weight: 800;
    letter-spacing: 0.3px;
    text-transform: uppercase;
}
.banner-sub {
    font-size: 6.8pt;
    color: #bfdbfe;
    font-weight: 500;
    margin-top: 1px;
}
.banner-badge {
    background-color: #f59e0b;
    color: #0f172a;
    font-weight: 800;
    font-size: 7.2pt;
    padding: 2.5px 6px;
    border-radius: 3px;
    white-space: nowrap;
}

/* Metadata */
.metadata-box {
    border: 1px solid #cbd5e1;
    border-radius: 3px;
    padding: 3.5px 6px;
    margin-bottom: 4px;
    background: #fdfdfd;
}
.metadata-row {
    display: flex;
    justify-content: space-between;
    font-size: 6.5pt;
    padding: 1px 0;
}
.metadata-row.divider {
    border-bottom: 1px dashed #cbd5e1;
    margin-bottom: 1px;
    padding-bottom: 2px;
}
.meta-item {
    color: #334155;
}
.meta-label {
    font-weight: 700;
    color: #0f3b75;
}

/* Dimensions */
.dimension-block {
    margin-bottom: 3.5px;
}
.dim-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 1px;
    margin-bottom: 2px;
}
.dim-title {
    font-size: 7.4pt;
    font-weight: 800;
    color: #0f3b75;
    text-transform: uppercase;
    letter-spacing: 0.2px;
}
.dim-title.critical {
    color: #991b1b;
}
.dim-sub {
    font-size: 6.4pt;
    font-style: italic;
    color: #64748b;
}

/* Table */
table.dim-table {
    width: 100%;
    border-collapse: collapse;
}
table.dim-table th {
    background-color: #f1f5f9;
    border-top: 1px solid #94a3b8;
    border-bottom: 1px solid #94a3b8;
    font-size: 6.5pt;
    font-weight: 700;
    color: #1e293b;
    padding: 2px 4px;
    text-align: left;
}
table.dim-table td {
    border-bottom: 1px solid #e2e8f0;
    padding: 2px 4px;
    vertical-align: top;
    font-size: 6.6pt;
}
td.col-id {
    width: 4%;
    font-weight: 800;
    text-align: center;
    color: #0f3b75;
}
td.col-indicator {
    width: 63%;
    line-height: 1.15;
}
td.col-val {
    width: 17%;
    white-space: nowrap;
    vertical-align: middle;
}
td.col-obs {
    width: 16%;
}
.ind-title {
    font-weight: 700;
    color: #0f172a;
}
.critical-callout {
    display: inline-block;
    background-color: #fee2e2;
    color: #991b1b;
    font-weight: 700;
    font-size: 6.1pt;
    padding: 1px 3px;
    border-left: 2px solid #dc2626;
    margin-top: 1.5px;
}
.checkbox-group {
    display: flex;
    gap: 4px;
    font-size: 6.4pt;
    color: #334155;
}

/* Dictamen */
.dictamen-box {
    border: 1.5px solid #0f3b75;
    border-radius: 3px;
    padding: 3px 5px;
    margin-top: 2px;
    margin-bottom: 3px;
    background: #f8fafc;
}
.dictamen-header {
    font-size: 6.8pt;
    font-weight: 800;
    color: #0f3b75;
    text-transform: uppercase;
    margin-bottom: 2.5px;
    letter-spacing: 0.3px;
}
.dictamen-options {
    display: flex;
    gap: 5px;
}
.dictamen-card {
    flex: 1;
    border: 1px solid #cbd5e1;
    border-radius: 3px;
    padding: 2.5px 4px;
    background: #fff;
    font-size: 6.1pt;
    line-height: 1.12;
}
.dictamen-card.danger {
    border-color: #fca5a5;
    background: #fff5f5;
}
.dictamen-card-title {
    font-weight: 800;
    font-size: 6.5pt;
    color: #0f3b75;
    margin-bottom: 1px;
}
.dictamen-card.danger .dictamen-card-title {
    color: #b91c1c;
}

/* Firmas */
.signatures-box {
    border: 1px solid #cbd5e1;
    border-radius: 3px;
    padding: 3.5px 8px;
    display: flex;
    justify-content: space-between;
    margin-bottom: 3px;
    background: #fff;
}
.sig-col {
    width: 48%;
}
.sig-title {
    font-size: 6.2pt;
    font-weight: 700;
    color: #475569;
    text-transform: uppercase;
    margin-bottom: 12px;
}
.sig-line {
    font-size: 6.2pt;
    color: #64748b;
}

/* Footer */
.page-footer {
    border-top: 1px solid #cbd5e1;
    padding-top: 1.5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 6.1pt;
    color: #64748b;
}
.page-footer-center {
    font-size: 6.2pt;
    color: #64748b;
    text-align: center;
    margin-top: 1px;
}
"""

def generate_pdf_from_html(html_content, output_pdf_path):
    temp_html_path = output_pdf_path.replace(".pdf", "_temp.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    cmd = [
        EDGE_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf_path}",
        temp_html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
    
    if os.path.exists(output_pdf_path):
        doc = fitz.open(output_pdf_path)
        pages = len(doc)
        doc.close()
        print(f"Generated: {os.path.basename(output_pdf_path)} -> Pages: {pages}")
        return pages
    else:
        print(f"Error generating {output_pdf_path}: {res.stderr}")
        return 0

print("PDF Helper initialized.")
