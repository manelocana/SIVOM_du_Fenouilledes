

from flask import Blueprint, render_template


aci_bp = Blueprint('aci', __name__, template_folder='templates')


@aci_bp.route('/aci')
def aci():
    return render_template('public/aci/aci.html')