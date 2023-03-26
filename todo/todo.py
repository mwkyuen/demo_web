import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from todo.db import get_db_conn

bp = Blueprint('todo', __name__)

@bp.route('/')
def index():
    return render_template('base.html')


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        db = get_db_conn()
        db.execute(
            "INSERT INTO todo_db (title, content) VALUES (?, ?)",
            (title, content),
        )
        db.commit()
        
        return redirect(url_for("todo.view"))

    return render_template('create.html')

@bp.route('/view')
def view():
    db = get_db_conn()
    posts = db.execute(
        'SELECT id, title, content, created'
        ' FROM todo_db'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('view.html', posts=posts)


def _get_post(id):
    post = get_db_conn().execute(
        'SELECT id, title, content, created'
        ' FROM todo_db'
        ' WHERE id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    post = _get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        db = get_db_conn()
        db.execute(
            'UPDATE todo_db SET title = ?, content = ?'
            ' WHERE id = ?',
            (title, content, id)
        )
        db.commit()
        
        return redirect(url_for('todo.view'))
        
    return render_template('update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    _get_post(id)
    db = get_db_conn()
    db.execute('DELETE FROM todo_db WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('todo.view'))
