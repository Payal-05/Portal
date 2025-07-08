from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for data per active_option
data_store = {
    'MRF': [],
    'PR': [],
    'PO': [],
    'GRN': [],
    'Issued to use': []
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/procure_install', methods=['GET', 'POST'])
def procure_install():
    if request.method == 'POST':
        # Extract form data
        entry = {
            'No': request.form.get('MRF_No'),
            'DateTime': request.form.get('MRF_DateTime'),
            'Requester': request.form.get('MRF_Requester'),
            'Material_Service': request.form.get('Material_Service'),
            'Item_Description': request.form.get('Item_Description'),
            'Status': request.form.get('MRF_Status'),
            'Remark': request.form.get('Remark')
        }
        data_store['MRF'].append(entry)
        return redirect(url_for('procure_install'))
    return render_template('procure_install.html', active_option='MRF', entries=data_store['MRF'])

@app.route('/pr', methods=['GET', 'POST'])
def pr():
    if request.method == 'POST':
        entry = {
            'No': request.form.get('PR_No'),
            'DateTime': request.form.get('PR_DateTime'),
            'Requester': request.form.get('PR_Requester'),
            'Material_Service': request.form.get('Material_Service'),
            'Item_Description': request.form.get('Item_Description'),
            'Status': request.form.get('PR_Status'),
            'Remark': request.form.get('Remark')
        }
        data_store['PR'].append(entry)
        return redirect(url_for('pr'))
    return render_template('procure_install.html', active_option='PR', entries=data_store['PR'])

@app.route('/po', methods=['GET', 'POST'])
def po():
    if request.method == 'POST':
        entry = {
            'No': request.form.get('PO_No'),
            'DateTime': request.form.get('PO_DateTime'),
            'Requester': request.form.get('PO_Requester'),
            'Material_Service': request.form.get('Material_Service'),
            'Item_Description': request.form.get('Item_Description'),
            'Status': request.form.get('PO_Status'),
            'Remark': request.form.get('Remark')
        }
        data_store['PO'].append(entry)
        return redirect(url_for('po'))
    return render_template('procure_install.html', active_option='PO', entries=data_store['PO'])

@app.route('/grn', methods=['GET', 'POST'])
def grn():
    if request.method == 'POST':
        entry = {
            'No': request.form.get('GRN_No'),
            'DateTime': request.form.get('GRN_DateTime'),
            'Requester': request.form.get('GRN_Requester'),
            'Material_Service': request.form.get('Material_Service'),
            'Item_Description': request.form.get('Item_Description'),
            'Status': request.form.get('GRN_Status'),
            'Remark': request.form.get('Remark')
        }
        data_store['GRN'].append(entry)
        return redirect(url_for('grn'))
    return render_template('procure_install.html', active_option='GRN', entries=data_store['GRN'])

@app.route('/issued_to_use', methods=['GET', 'POST'])
def issued_to_use():
    if request.method == 'POST':
        entry = {
            'No': request.form.get('Issued to use_No'),
            'DateTime': request.form.get('Issued to use_DateTime'),
            'Requester': request.form.get('Issued to use_Requester'),
            'Material_Service': request.form.get('Material_Service'),
            'Item_Description': request.form.get('Item_Description'),
            'Status': request.form.get('Issued to use_Status'),
            'Remark': request.form.get('Remark')
        }
        data_store['Issued to use'].append(entry)
        return redirect(url_for('issued_to_use'))
    return render_template('procure_install.html', active_option='Issued to use', entries=data_store['Issued to use'])

@app.route('/cl_status')
def cl_status():
    return render_template('cl_status.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/important_dates')
def important_dates():
    return render_template('important_dates.html')

@app.route('/device_status')
def device_status():
    return render_template('device_status.html')

if __name__ == '__main__':
    app.run(debug=True)
