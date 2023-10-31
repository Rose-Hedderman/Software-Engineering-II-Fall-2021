import json
import sys
from models import app, db, University, Location

def load_json(filename):
	with open(filename) as file:
		print(file)
		jsn = json.load(file)
		file.close()
	return jsn

def create_colleges():
    # load json file
	typCol = load_json("colleges.json")
    # start counting colleges
	count = 0
    # for loop to sort by department 
	for dep in typCol['Departments']:
        # traverse through business schools
        for a in dep['Business Schools']:
            count += 1
            col_id = count
            department = a['Business Schools']
            uni = a['university']
            name = a['name']
            majors = a['majors']
            minors = a['minors']
            nummajors = int(a['nummajors'])
            numminors = int(a['numminors'])
            aRate = a['acceptance rate']
            rank = int(a['rank'])
            college = Colleges(name=name,
                                id = col_id,
                                uni = uni,
                                department = department,
                                majors = majors,
                                minors = minors,
                                nummajors = nummajors,
                                numminors = numminors,
                                aRate = aRate,
                                rank = rank
            db.session.add(college)
            db.session.commit()
        # traverse through engineering schools
        for b in dep['Engineering Schools']:
            count += 1
            col_id = count
            department = b['Engineering Schools']
            uni = b['university']
            name = b['name']
            majors = b['majors']
            minors = b['minors']
            nummajors = int(b['nummajors'])
            numminors = int(b['numminors'])
            aRate = b['acceptance rate']
            rank = int(b['rank'])
            college = Colleges(name=name,
                                id = col_id,
                                uni = uni,
                                department = department,
                                majors = majors,
                                minors = minors,
                                nummajors = nummajors,
                                numminors = numminors,
                                aRate = aRate,
                                rank = rank
            db.session.add(college)
            db.session.commit()
		for c in dep['Liberal Arts Schools']:
            count += 1
            col_id = count
            department = c['Liberal Arts Schools']
            uni = c['university']
            name = c['name']
            majors = c['majors']
            minors = c['minors']
            nummajors = int(c['nummajors'])
            numminors = int(c['numminors'])
            aRate = c['acceptance rate']
            rank = int(c['rank'])
            college = Colleges(name=name,
                                id = col_id,
                                uni = uni,
                                department = department,
                                majors = majors,
                                minors = minors,
                                nummajors = nummajors,
                                numminors = numminors,
                                aRate = aRate,
                                rank = rank
            db.session.add(college)
            db.session.commit()
        for d in dep['Communication Schools']:
            count += 1
            col_id = count
            department = d['Communication Schools']
            uni = d['university']
            name = d['name']
            majors = d['majors']
            minors = d['minors']
            nummajors = int(d['nummajors'])
            numminors = int(d['numminors'])
            aRate = d['acceptance rate']
            rank = int(d['rank'])
            college = Colleges(name=name,
                                id = col_id,
                                uni = uni,
                                department = department,
                                majors = majors,
                                minors = minors,
                                nummajors = nummajors,
                                numminors = numminors,
                                aRate = aRate,
                                rank = rank
            db.session.add(college)
            db.session.commit()
        for e in dep['Education Schools']:
            count += 1
            col_id = count
            department = e['Education Schools']
            uni = e['university']
            name = e['name']
            majors = e['majors']
            minors = e['minors']
            nummajors = int(e['nummajors'])
            numminors = int(e['numminors'])
            aRate = e['acceptance rate']
            rank = int(e['rank'])
            college = Colleges(name=name,
                                id = col_id,
                                uni = uni,
                                department = department,
                                majors = majors,
                                minors = minors,
                                nummajors = nummajors,
                                numminors = numminors,
                                aRate = aRate,
                                rank = rank
            db.session.add(college)
            db.session.commit()
        for f in dep['Architecture Schools']:
            count += 1
            col_id = count
            department = f['Architecture Schools']
            uni = f['university']
            name = f['name']
            majors = f['majors']
            minors = f['minors']
            nummajors = int(f['nummajors'])
            numminors = int(f['numminors'])
            aRate = f['acceptance rate']
            rank = int(f['rank'])
            college = Colleges(name=name,
                                id = col_id,
                                uni = uni,
                                department = department,
                                majors = majors,
                                minors = minors,
                                nummajors = nummajors,
                                numminors = numminors,
                                aRate = aRate,
                                rank = rank
            db.session.add(college)
            db.session.commit()
        for g in dep['Information Schools']:
            count += 1
            col_id = count
            department = g['Information Schools']
            uni = g['university']
            name = g['name']
            majors = g['majors']
            minors = g['minors']
            nummajors = int(g['nummajors'])
            numminors = int(g['numminors'])
            aRate = g['acceptance rate']
            rank = int(g['rank'])
            college = Colleges(name=name,
                                id = col_id,
                                uni = uni,
                                department = department,
                                majors = majors,
                                minors = minors,
                                nummajors = nummajors,
                                numminors = numminors,
                                aRate = aRate,
                                rank = rank
            db.session.add(college)
            db.session.commit()
        for h in dep['Nursing Schools']:
            count += 1
            col_id = count
            department = h['Nursing Schools']
            uni = h['university']
            name = h['name']
            majors = h['majors']
            minors = h['minors']
            nummajors = int(h['nummajors'])
            numminors = int(h['numminors'])
            aRate = h['acceptance rate']
            rank = int(h['rank'])
            college = Colleges(name=name,
                                id = col_id,
                                uni = uni,
                                department = department,
                                majors = majors,
                                minors = minors,
                                nummajors = nummajors,
                                numminors = numminors,
                                aRate = aRate,
                                rank = rank
            db.session.add(college)
            db.session.commit()


create_universities()
create_locations()
create_colleges()
################
class Colleges(db.Model):
	__tablename__ = 'colleges'

	name = db.Column(db.String(120), nullable = False)
	col_id = db.Column(db.Integer, primary_key = True)
    uni = db.Column(db.String(120), nullable = False)
    department = db.Column(db.String(80), nullable = True)
    majors = db.Column(db.String(3000), nullable = False)
    minors = db.Column(db.String(3000), nullable = False)
    nummajors = db.Column(db.Integer, nullable = False)
    numminors = db.Column(db.Integer, nullable = False)
    aRate = db.Column(db.String(80), nullable = True)
    rank = db.Column(db.Integer, nullable = False)

############3
@app.route('/colleges/')
def Colleges():
    college_list = db.session.query(Colleges).all()
    return render_template("Colleges.html", university_list)
