from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_html():
    pdf_file = request.files['pdf_file']
    if pdf_file:
        pdf_path = os.path.join('uploads', pdf_file.filename)
        pdf_file.save(pdf_path)

        # Convert PDF to HTML using pdf2htmlEX
        subprocess.run(['pdf2htmlEX', pdf_path, 'output.html'])

        return send_file('output.html', as_attachment=True)
    else:
        return 'No PDF file provided.'

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
