from wtforms import Form, StringField, FloatField, IntegerField, validators


class SubmissionForm(Form):
    position = StringField('position', [validators.Length(min=1, max=30)])
    school = StringField('school', [validators.Length(min=1, max=30)])
    height = StringField('height', [validators.Length(min=1, max=5)])
    weight = StringField('weight', [validators.Length(min=1, max=5)])
    bench = FloatField('bench', [validators.Length(min=1, max=5)])
    vert = FloatField('vert', [validators.Length(min=1, max=5)])
    broad = IntegerField('broad', [validators.Length(min=1, max=5)])
    gp = IntegerField('gp', [validators.Length(min=1, max=5)])
    fgm = FloatField('fgm', [validators.Length(min=1, max=5)])
    three = FloatField('three', [validators.Length(min=1, max=5)])
