

from flask import Blueprint, render_template



sivm_bp = Blueprint('sivm', __name__, template_folder='templates')



@sivm_bp.route('/sivm')
def sivm():
    return render_template('public/sivm/sivm.html')