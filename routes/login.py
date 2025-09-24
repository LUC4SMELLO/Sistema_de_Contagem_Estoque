from flask import Blueprint, request, flash, redirect, url_for, render_template


login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    
    return render_template("login.html")