from flask import render_template
from app.forms import MyForm
from app import app

@app.route('/myform', methods=['GET', 'POST'])
def my_form():
    form = MyForm()
    
    if form.validate_on_submit():
        # Process the form data
        name = form.name.data
        email = form.email.data
        
        # Perform actions with the data (e.g., save to a database)
        # database.save(name, email)
        
        return f'Form submitted: Name - {name}, Email - {email}'

    return render_template('form.html', form=form)
