from wtforms import Form, StringField, FloatField, IntegerField


class SubmissionForm(Form):
    position = StringField('position')
    school = StringField('school')
    height = StringField('height')
    weight = StringField('weight')
    bench = FloatField('bench')
    vert = FloatField('vert')
    broad = IntegerField('broad')
    gp = IntegerField('gp')
    fgm = FloatField('fgm')
    three = FloatField('three')
