from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    # def to_dict(self):
    #     # Method 1.
    #     dictionary = {}
    #     # Loop through each column in the data record
    #     for column in self.__table__.columns:
    #         # Create a new dictionary entry;
    #         # where the key is the name of the column
    #         # and the value is the value of the column
    #         dictionary[column.name] = getattr(self, column.name)
    #     return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random():
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random())).scalar()
    random_cafe.__dict__.pop("_sa_instance_state")
    return jsonify(cafe=random_cafe.__dict__)
    # return jsonify(cafe={"can_take_calls":random_cafe.can_take_calls,
    #                "coffee_price":random_cafe.coffee_price,
    #                "has_sockets":random_cafe.has_sockets,
    #                "has_toilet":random_cafe.has_toilet,
    #                "has_wifi":random_cafe.has_wifi,
    #                "id":random_cafe.id,
    #                "img_url":random_cafe.img_url,
    #                "location":random_cafe.location,
    #                "map_url":random_cafe.map_url,
    #                "name":random_cafe.name,
    #                "seats":random_cafe.seats})

def to_json(cafes):
    cafes_list = []
    for cafe in cafes:
        cafe.__dict__.pop("_sa_instance_state")
        cafes_list.append(cafe.__dict__)
    return jsonify(cafes=cafes_list)

@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return to_json(all_cafes)

@app.route("/search")
def search_cafe_by_location():
    location_to_search = request.args.get("loc", type=str)
    cafes_by_loc = db.session.execute(db.select(Cafe).filter_by(location=location_to_search)).scalars().all()
    if not cafes_by_loc:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    return to_json(cafes_by_loc)

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 200


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price", type=str)
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."}), 200

SECRET_API="TopSecretAPIKey"

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    # Accept both api_key and api-key for compatibility with different clients.
    api_key = request.args.get("api_key", type=str) or request.args.get("api-key", type=str)
    if api_key != SECRET_API:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed, make sure you have the correct api_key."}), 403
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully deleted the cafe."}), 200

if __name__ == '__main__':
    app.run(debug=True)
