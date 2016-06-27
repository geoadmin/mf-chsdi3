# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Integer

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['evd']


class BODENEIGNUNG(Base, Vector):
    __tablename__ = 'bodeneignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/bodeneignung-kulurtyp.mako'
    __bodId__ = 'ch.blw.bodeneignung-kulturtyp'
    # __queryable_attributes__ = ['farbe']
    __label__ = 'symb_color'
    id = Column('bgdi_id', Integer, primary_key=True)
    farbe = Column('farbe', Integer)
    eignungsei = Column('eignungsei', Text)
    symb_color = Column('symb_color', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.bodeneignung-kulturtyp', BODENEIGNUNG)


class Bodeneignung_gruendigkeit(Base, Vector):
    __tablename__ = 'bodeneignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bodeneignung.mako'
    __bodId__ = 'ch.blw.bodeneignung-gruendigkeit'
    __label__ = 'farbe'
    id = Column('bgdi_id', Integer, primary_key=True)
    farbe = Column('farbe', Integer)
    eignungsei = Column('eignungsei', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.bodeneignung-gruendigkeit', Bodeneignung_gruendigkeit)


class Bodeneignung_skelettgehalt(Base, Vector):
    __tablename__ = 'bodeneignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bodeneignung.mako'
    __bodId__ = 'ch.blw.bodeneignung-skelettgehalt'
    __label__ = 'farbe'
    id = Column('bgdi_id', Integer, primary_key=True)
    farbe = Column('farbe', Integer)
    eignungsei = Column('eignungsei', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.bodeneignung-skelettgehalt', Bodeneignung_skelettgehalt)


class Bodeneignung_wasserspeichervermoegen(Base, Vector):
    __tablename__ = 'bodeneignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bodeneignung.mako'
    __bodId__ = 'ch.blw.bodeneignung-wasserspeichervermoegen'
    __label__ = 'farbe'
    id = Column('bgdi_id', Integer, primary_key=True)
    farbe = Column('farbe', Integer)
    eignungsei = Column('eignungsei', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.bodeneignung-wasserspeichervermoegen', Bodeneignung_wasserspeichervermoegen)


class Bodeneignung_naehrstoffspeichervermoegen(Base, Vector):
    __tablename__ = 'bodeneignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bodeneignung.mako'
    __bodId__ = 'ch.blw.bodeneignung-naehrstoffspeichervermoegen'
    __label__ = 'farbe'
    id = Column('bgdi_id', Integer, primary_key=True)
    farbe = Column('farbe', Integer)
    eignungsei = Column('eignungsei', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.bodeneignung-naehrstoffspeichervermoegen', Bodeneignung_naehrstoffspeichervermoegen)


class Bodeneignung_wasserdurchlaessigkeit(Base, Vector):
    __tablename__ = 'bodeneignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bodeneignung.mako'
    __bodId__ = 'ch.blw.bodeneignung-wasserdurchlaessigkeit'
    __label__ = 'farbe'
    id = Column('bgdi_id', Integer, primary_key=True)
    farbe = Column('farbe', Integer)
    eignungsei = Column('eignungsei', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.bodeneignung-wasserdurchlaessigkeit', Bodeneignung_wasserdurchlaessigkeit)


class Bodeneignung_vernaessung(Base, Vector):
    __tablename__ = 'bodeneignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bodeneignung.mako'
    __bodId__ = 'ch.blw.bodeneignung-vernaessung'
    __label__ = 'farbe'
    id = Column('bgdi_id', Integer, primary_key=True)
    farbe = Column('farbe', Integer)
    eignungsei = Column('eignungsei', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.bodeneignung-vernaessung', Bodeneignung_vernaessung)


class Bodeneignung_kulturland(Base, Vector):
    __tablename__ = 'bodeneignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bodeneignung.mako'
    __bodId__ = 'ch.blw.bodeneignung-kulturland'
    __label__ = 'farbe'
    id = Column('bgdi_id', Integer, primary_key=True)
    farbe = Column('farbe', Integer)
    eignungsei = Column('eignungsei', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.bodeneignung-kulturland', Bodeneignung_kulturland)


class klimaeignung_typ(Base, Vector):
    __tablename__ = 'klimaeignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klimaeignung.mako'
    __bodId__ = 'ch.blw.klimaeignung-typ'
    __label__ = 'klimeig_be'
    id = Column('bgdi_id', Integer, primary_key=True)
    klimeig_be = Column('klimeig_be', Text)
    zone = Column('zone', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.klimaeignung-typ', klimaeignung_typ)


class klimaeignung_koernermais(Base, Vector):
    __tablename__ = 'klimaeignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klimaeignung.mako'
    __bodId__ = 'ch.blw.klimaeignung-koernermais'
    __label__ = 'klimeig_be'
    id = Column('bgdi_id', Integer, primary_key=True)
    klimeig_be = Column('klimeig_be', Text)
    zone = Column('zone', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.klimaeignung-koernermais', klimaeignung_koernermais)


class klimaeignung_spezialkulturen(Base, Vector):
    __tablename__ = 'klimaeignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klimaeignung.mako'
    __bodId__ = 'ch.blw.klimaeignung-spezialkulturen'
    __label__ = 'klimeig_be'
    id = Column('bgdi_id', Integer, primary_key=True)
    klimeig_be = Column('klimeig_be', Text)
    zone = Column('zone', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.klimaeignung-spezialkulturen', klimaeignung_spezialkulturen)


class klimaeignung_zwischenfruchtbau(Base, Vector):
    __tablename__ = 'klimaeignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klimaeignung.mako'
    __bodId__ = 'ch.blw.klimaeignung-zwischenfruchtbau'
    __label__ = 'klimeig_be'
    id = Column('bgdi_id', Integer, primary_key=True)
    klimeig_be = Column('klimeig_be', Text)
    zone = Column('zone', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.klimaeignung-zwischenfruchtbau', klimaeignung_zwischenfruchtbau)


class klimaeignung_kartoffeln(Base, Vector):
    __tablename__ = 'klimaeignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klimaeignung.mako'
    __bodId__ = 'ch.blw.klimaeignung-kartoffeln'
    __label__ = 'klimeig_be'
    id = Column('bgdi_id', Integer, primary_key=True)
    klimeig_be = Column('klimeig_be', Text)
    zone = Column('zone', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.klimaeignung-kartoffeln', klimaeignung_kartoffeln)


class klimaeignung_getreidebau(Base, Vector):
    __tablename__ = 'klimaeignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klimaeignung.mako'
    __bodId__ = 'ch.blw.klimaeignung-getreidebau'
    __label__ = 'klimeig_be'
    id = Column('bgdi_id', Integer, primary_key=True)
    klimeig_be = Column('klimeig_be', Text)
    zone = Column('zone', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.klimaeignung-getreidebau', klimaeignung_getreidebau)


class klimaeignung_futterbau(Base, Vector):
    __tablename__ = 'klimaeignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klimaeignung.mako'
    __bodId__ = 'ch.blw.klimaeignung-futterbau'
    __label__ = 'klimeig_be'
    id = Column('bgdi_id', Integer, primary_key=True)
    klimeig_be = Column('klimeig_be', Text)
    zone = Column('zone', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.klimaeignung-futterbau', klimaeignung_futterbau)


class klimaeignung_kulturland(Base, Vector):
    __tablename__ = 'klimaeignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klimaeignung.mako'
    __bodId__ = 'ch.blw.klimaeignung-kulturland'
    __label__ = 'klimeig_be'
    id = Column('bgdi_id', Integer, primary_key=True)
    klimeig_be = Column('klimeig_be', Text)
    zone = Column('zone', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.klimaeignung-kulturland', klimaeignung_kulturland)


class niederschlagshaushalt(Base, Vector):
    __tablename__ = 'klimaeignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klimaeignung.mako'
    __bodId__ = 'ch.blw.niederschlagshaushalt'
    __label__ = 'klimeig_be'
    id = Column('bgdi_id', Integer, primary_key=True)
    klimeig_be = Column('klimeig_be', Text)
    zone = Column('zone', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.niederschlagshaushalt', niederschlagshaushalt)


class emapis_beizugsgebiet(Base, Vector):
    __tablename__ = 'emapis_beizugsgebiet'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-beizugsgebiet'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-beizugsgebiet', emapis_beizugsgebiet)


class emapis_bewaesserung(Base, Vector):
    __tablename__ = 'emapis_bewaesserung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-bewaesserung'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-bewaesserung', emapis_bewaesserung)


class emapis_elektrizitaetsversorgung(Base, Vector):
    __tablename__ = 'emapis_elektrizitaetsversorgung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-elektrizitaetsversorgung'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-elektrizitaetsversorgung', emapis_elektrizitaetsversorgung)


class emapis_entwaesserung(Base, Vector):
    __tablename__ = 'emapis_entwaesserung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-entwaesserung'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-entwaesserung', emapis_entwaesserung)


class emapis_hochbau(Base, Vector):
    __tablename__ = 'emapis_hochbau'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-hochbau'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-hochbau', emapis_hochbau)


class emapis_milchleitung(Base, Vector):
    __tablename__ = 'emapis_milchleitung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-milchleitung'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-milchleitung', emapis_milchleitung)


class emapis_oekologie(Base, Vector):
    __tablename__ = 'emapis_oekologie'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-oekologie'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-oekologie', emapis_oekologie)


class emapis_projektschwerpunkt(Base, Vector):
    __tablename__ = 'emapis_projektschwerpunkt'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-projektschwerpunkt'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-projektschwerpunkt', emapis_projektschwerpunkt)


class emapis_seilbahnen(Base, Vector):
    __tablename__ = 'emapis_seilbahnen'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-seilbahnen'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-seilbahnen', emapis_seilbahnen)


class emapis_wasserversorgung(Base, Vector):
    __tablename__ = 'emapis_wasserversorgung'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-wasserversorgung'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-wasserversorgung', emapis_wasserversorgung)


class emapis_wegebau(Base, Vector):
    __tablename__ = 'emapis_wegebau'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __template__ = 'templates/htmlpopup/emapis.mako'
    __bodId__ = 'ch.blw.emapis-wegebau'
    __label__ = 'typ'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    geschaeftsnummer = Column('geschaeftsnummer', Text)
    the_geom = Column(Geometry2D)

register('ch.blw.emapis-wegebau', emapis_wegebau)
