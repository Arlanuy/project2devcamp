from helpers import functions
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
import time

def add_message():
    """Registers a new message for the user."""
    if 'user_id' not in session:
        abort(401)
    if request.form['text']:
        db = functions.get_db()
        #db.execute()
        db.commit()
        flash('Your message was recorded')
    return redirect(functions.url_for('/'))
