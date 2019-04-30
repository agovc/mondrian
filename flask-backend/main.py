import os
import flask
from pyswip import Prolog
import random

app = flask.Flask("__main__")

dict = {
    "blue": "#35A5E5",
    "yellow": "#FFE357",
    "red": "#F63625",
    "black": "#212121",
    "w_1": "#E1E1E1",
    "w_2": "#E2E2E2",
    "w_3": "#E3E3E3"
}

resp = {}
# colors = ["blue", "yellow", "w_1", "w_2", "w_3", "red", "black"]
# rand_color_1 = colors[random.randrange(6)]
# rand_color_2 = colors[random.randrange(6)]
string = "mondrian([ (a, A), (b, B), (c, C), (d, D), (e, E), (f, F)])"
pl = Prolog()
dir_path = os.path.dirname(os.path.realpath('static/mondrian.pl'))
pl.consult(dir_path + "/mondrian.pl")
response = pl.query(string)
response_list = list(response)
combinations = len(response_list)

@app.route("/")
def my_index():

    rand_response = response_list[random.randrange(combinations)]
    print(rand_response)
    resp.update( {'A' : dict[rand_response["A"]]} )
    resp.update( {'B' : dict[rand_response["B"]]} )
    resp.update( {'C' : dict[rand_response["C"]]} )
    resp.update( {'D' : dict[rand_response["D"]]} )
    resp.update( {'E' : dict[rand_response["E"]]} )
    resp.update( {'F' : dict[rand_response["F"]]} )
    print(resp)

    return flask.render_template("index.html",
    name="MONDRIAN",
    a=dict[rand_response["A"]],
    b=dict[rand_response["B"]],
    c=dict[rand_response["C"]],
    d=dict[rand_response["D"]],
    e=dict[rand_response["E"]],
    f=dict[rand_response["F"]]
    )

app.run(debug=True)
