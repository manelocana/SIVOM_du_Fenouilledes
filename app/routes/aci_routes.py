

from flask import Blueprint, render_template


aci_bp = Blueprint('aci', __name__)


@aci_bp.route('/aci')
def aci():
    return render_template('aci/julien.html')