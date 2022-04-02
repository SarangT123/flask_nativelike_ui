from website import app
from flask import render_template, url_for, flash, redirect, session, request
from website.auth import current_user, login_required
from website.models import User, Admin_users
import tkinter
from tkinter.messagebox import askyesno
import os


def prompt():
    root = tkinter.Tk()
    root.withdraw()

    answer = askyesno(title='confirmation',
                      message='Are you sure that you want to quit?')
    if answer:
        root.destroy()
        os.system('pkill flask')
        os.system('pkill python3')
        exit()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/stop')
@app.route('/stop/<int:id>')
@login_required
def stop(id=0):
    if Admin_users.query.filter_by(user_id=current_user.id).first() != None:
        prompt()
        return "Confirm on the server to stop the server"
    return redirect(url_for('home'))
