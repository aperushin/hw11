from flask import Flask, abort, render_template, request

import utils
from config import CANDIDATES_FILE


app = Flask(__name__)


@app.route('/')
def page_home():
    """Display all candidates"""
    candidates = utils.load_candidates(CANDIDATES_FILE)
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>')
def page_candidate(candidate_id):
    """Display candidate with given id"""
    candidate = utils.get_candidate(candidate_id)
    if candidate:
        return render_template('single.html', candidate=candidate)
    return abort(404)


@app.route('/skills')
def page_skill():
    """Display all candidates with given skill"""
    skill = request.args.get('search_arg')
    candidates = utils.get_candidates_by_skill(skill)
    result_count = len(candidates)
    return render_template('skill.html', candidates=candidates, result_count=result_count)


@app.route('/search')
def get_candidates_by_name():
    name = request.args.get('search_arg')
    candidates = utils.get_candidates_by_name(name)
    result_count = len(candidates)
    return render_template('search.html', candidates=candidates, result_count=result_count)


if __name__ == '__main__':
    app.run()
