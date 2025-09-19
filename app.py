from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from forms import PetSearchForm
import petfinder_api

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Used to protect session data
csrf = CSRFProtect(app)

@app.route("/", methods=["GET", "POST"])
def index():
    form = PetSearchForm()

    if form.validate_on_submit():
        # Collect data from the form
        animal_type = form.animal_type.data
        location = form.location.data
        breed = form.breed.data
        age_range = form.age_range.data
        gender = form.gender.data
        include_photos = form.include_photos.data

        # Fetch matching pets from the API
        pets = petfinder_api.get_pet_data(
            animal_type, location, breed, age_range, gender, include_photos
        )

        # Show results or a friendly message if nothing was found
        if not pets:
            return render_template("results.html", pets=[], message="No pets found matching your search.")

        return render_template("results.html", pets=pets, message="")

    return render_template("form.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
