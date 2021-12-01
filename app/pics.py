import os
from flask import Blueprint, session , redirect, render_template
from flask_login import login_required, current_user
import Main
from app import uploads
import app

pics_bp = Blueprint("pics", __name__, template_folder="templates", static_folder="uploads")



@pics_bp.route("/testing", methods=["GET", "POST"])
@login_required
def testing():
    #: data = os.listdir(os.path.join(uploads))
    #: pic = os.path.join(uploads, "27.png")
    return render_template("/testing.html")
