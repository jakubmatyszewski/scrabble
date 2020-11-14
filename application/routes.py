from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
)
from flask_login import current_user, login_required
from datetime import datetime
from .forms import ResultForm
from .models import db, Result

# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = ResultForm()
    if form.validate_on_submit():
        points = form.points.data
        time = form.time.data
        if points and time:
            new_result = Result(
                points=points,
                time=time,
                created=datetime.now()
            )
            db.session.add(new_result)
            db.session.commit()
            return redirect(url_for('main_bp.index'))
    return render_template(
        'results.html',
        form=form,
        results=Result.query.all(),
        current_user=current_user,
    )
