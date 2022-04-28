from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route('/')
def main_page():
    """ Главная страница """

    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>')
def candidate_page(candidate_id):
    """ Страница кандидата """

    candidates = utils.get_candidate(candidate_id)
    return render_template('card.html', candidate=candidates)


@app.route('/search/<string:candidate_name>')
def search_page(candidate_name):
    """ Страница поиска кандидатов по имени """

    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, candidates_count=len(candidates))


@app.route('/skill/<string:skill_name>')
def skill_page(skill_name):
    """  Страница поиска кандидатов по скиллам """

    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skills.html', candidates=candidates, skill=skill_name, candidates_count=len(candidates))


app.run()
