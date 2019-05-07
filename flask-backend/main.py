# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Author: Santiago Valencia Corona, 2019

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
colors = ["blue", "yellow", "w_1", "w_2", "w_3", "red", "black"]
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
    print(combinations)
    resp.update( {'A' : dict[rand_response["A"]]} )
    resp.update( {'B' : dict[rand_response["B"]]} )
    resp.update( {'C' : dict[rand_response["C"]]} )
    resp.update( {'D' : dict[rand_response["D"]]} )
    resp.update( {'E' : dict[rand_response["E"]]} )
    resp.update( {'F' : dict[rand_response["F"]]} )
    print(resp)

    p_r1=random.randint(30,180)
    p_r2=random.randint(20,80)
    p_r3=random.randint(20,80)
    p_r4=random.randint(30,120)

    p_w1=random.randint(30,200)
    p_w2=random.randint(30,100)
    p_w3=random.randint(50,150)

    return flask.render_template("index.html",
    name="MONDRIAN",
    a=dict[rand_response["A"]],
    b=dict[rand_response["B"]],
    c=dict[rand_response["C"]],
    d=dict[rand_response["D"]],
    e=dict[rand_response["E"]],
    f=dict[rand_response["F"]],
    r1_1=str(p_r1)+"px",
    r2_1=str(p_r2)+"px",
    r3_1=str(p_r3)+"px",
    c1_1=str(210-p_r1)+"px",
    c2_1=str(200-p_r2-p_r3)+"px",
    p_w1_1=str(p_w1)+"px",
    p_w2_1=str(p_w2)+"px",
    p_w3_1=str(400-p_w1-p_w2)+"px",
    r1_2=str(p_r4)+"px",
    r2_2=str(p_r4)+"px",
    r3_2=str(310-p_r4-p_r4)+"px",
    r4_2=str(p_r3)+"px",
    r5_2=str(320-p_r3)+"px",
    p_w1_2=str(p_w3)+"px",
    p_w2_2=str(p_w2)+"px",
    p_w3_2=str(310-p_w3-p_w2)+"px"
    )

app.run(debug=True)
