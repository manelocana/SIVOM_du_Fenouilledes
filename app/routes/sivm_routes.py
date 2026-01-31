

from flask import Blueprint, render_template



sivm_bp = Blueprint('sivm', __name__)



@sivm_bp.route('/sivm')
def sivm():
    return render_template('sivm/estefan.html')