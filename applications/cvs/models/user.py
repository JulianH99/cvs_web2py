# -*- coding: utf-8 -*-


db.define_table('cvs_user',
                Field('document_number', 'string', unique=True),
                Field('picture', 'string'),
                Field('first_name', 'string'),
                Field('last_name', 'string'),
                Field('age', 'integer'),
                Field('birth_date', 'date')
                )

db.define_table('cvs_education',
                Field('ed_type', 'string'),
                Field('institution', 'string'),
                Field('start_year', 'integer'),
                Field('end_year', 'integer'),
                Field('career', 'string'),
                Field('user_id', db.cvs_user)
                )

db.define_table('cvs_skills',
                Field('sk_name', 'string'),
                Field('sk_value', 'string'),
                Field('user_id', db.cvs_user)
                )



