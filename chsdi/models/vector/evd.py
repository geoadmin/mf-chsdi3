# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode, Integer

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['evd']


class Bodeneignung:
    __tablename__ = 'bodeneignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bodeneignung.mako'
    __label__ = 'farbe'
    id = Column('bgdi_id', Integer, primary_key=True)
    farbe = Column('farbe', Integer)
    eignungsei = Column('eignungsei', Unicode)
    the_geom = Column(Geometry2D)


class Kulturtyp(Base, Bodeneignung, Vector):
    __template__ = 'templates/htmlpopup/bodeneignung-kulurtyp.mako'
    __bodId__ = 'ch.blw.bodeneignung-kulturtyp'
    __label__ = 'symb_color'
    symb_color = Column('symb_color', Unicode)

register('ch.blw.bodeneignung-kulturtyp', Kulturtyp)


class Gruendigkeit(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-gruendigkeit'

register('ch.blw.bodeneignung-gruendigkeit', Gruendigkeit)


class Skelettgehalt(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-skelettgehalt'

register('ch.blw.bodeneignung-skelettgehalt', Skelettgehalt)


class Wasserspeichervermoegen(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-wasserspeichervermoegen'

register('ch.blw.bodeneignung-wasserspeichervermoegen', Wasserspeichervermoegen)


class Naehrstoffspeichervermoegen(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-naehrstoffspeichervermoegen'

register('ch.blw.bodeneignung-naehrstoffspeichervermoegen', Naehrstoffspeichervermoegen)


class Wasserdurchlaessigkeit(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-wasserdurchlaessigkeit'

register('ch.blw.bodeneignung-wasserdurchlaessigkeit', Wasserdurchlaessigkeit)


class Vernaessung(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-vernaessung'

register('ch.blw.bodeneignung-vernaessung', Vernaessung)


class Kulturland(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-kulturland'

register('ch.blw.bodeneignung-kulturland', Kulturland)


class Klimaeignung:
    __tablename__ = 'klimaeignung'
    __table_args__ = ({'schema': 'blw', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klimaeignung.mako'
    __label__ = 'klimeig_be'
    id = Column('bgdi_id', Integer, primary_key=True)
    klimeig_be = Column('klimeig_be', Unicode)
    zone = Column('zone', Unicode)
    the_geom = Column(Geometry2D)


class KlimaeignungTyp(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-typ'

register('ch.blw.klimaeignung-typ', KlimaeignungTyp)


class KlimaeignungKoernermais(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-koernermais'

register('ch.blw.klimaeignung-koernermais', KlimaeignungKoernermais)


class KlimaeignungSpezialkulturen(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-spezialkulturen'

register('ch.blw.klimaeignung-spezialkulturen', KlimaeignungSpezialkulturen)


class KlimaeignungZwischenfruchtbau(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-zwischenfruchtbau'

register('ch.blw.klimaeignung-zwischenfruchtbau', KlimaeignungZwischenfruchtbau)


class KlimaeignungKartoffeln(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-kartoffeln'

register('ch.blw.klimaeignung-kartoffeln', KlimaeignungKartoffeln)


class KlimaeignungGetreidebau(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-getreidebau'

register('ch.blw.klimaeignung-getreidebau', KlimaeignungGetreidebau)


class KlimaeignungFutterbau(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-futterbau'

register('ch.blw.klimaeignung-futterbau', KlimaeignungFutterbau)


class KlimaeignungKulturland(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-kulturland'

register('ch.blw.klimaeignung-kulturland', KlimaeignungKulturland)


class Niederschlagshaushalt(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.niederschlagshaushalt'

register('ch.blw.niederschlagshaushalt', Niederschlagshaushalt)


class UrsprungsbezeichnungenFleisch(Base, Vector):
    __tablename__ = 'ursprungsbezeichnungen_fleisch'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __bodId__ = 'ch.blw.ursprungsbezeichnungen-fleisch'
    __template__ = 'templates/htmlpopup/ursprungsbezeichnungen.mako'
    __label__ = 'objektcode'
    id = Column('bgdi_id', Integer, primary_key=True)
    objektcode = Column('objektcode', Integer)
    objekt_d = Column('objekt_d', Unicode)
    objekt_f = Column('objekt_f', Unicode)
    objekt_i = Column('objekt_i', Unicode)
    the_geom = Column(Geometry2D)

register('ch.blw.ursprungsbezeichnungen-fleisch', UrsprungsbezeichnungenFleisch)


class UrsprungsbezeichnungenKaese(Base, Vector):
    __tablename__ = 'ursprungsbezeichnungen_kaese'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __bodId__ = 'ch.blw.ursprungsbezeichnungen-kaese'
    __template__ = 'templates/htmlpopup/ursprungsbezeichnungen.mako'
    __label__ = 'objektcode'
    id = Column('bgdi_id', Integer, primary_key=True)
    objektcode = Column('objektcode', Integer)
    objekt_d = Column('objekt_d', Unicode)
    objekt_f = Column('objekt_f', Unicode)
    objekt_i = Column('objekt_i', Unicode)
    the_geom = Column(Geometry2D)

register('ch.blw.ursprungsbezeichnungen-kaese', UrsprungsbezeichnungenKaese)


class UrsprungsbezeichnungenKonditoreiwaren(Base, Vector):
    __tablename__ = 'ursprungsbezeichnungen_konditoreiwaren'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __bodId__ = 'ch.blw.ursprungsbezeichnungen-konditoreiwaren'
    __template__ = 'templates/htmlpopup/ursprungsbezeichnungen.mako'
    __label__ = 'objektcode'
    id = Column('bgdi_id', Integer, primary_key=True)
    objektcode = Column('objektcode', Integer)
    objekt_d = Column('objekt_d', Unicode)
    objekt_f = Column('objekt_f', Unicode)
    objekt_i = Column('objekt_i', Unicode)
    the_geom = Column(Geometry2D)

register('ch.blw.ursprungsbezeichnungen-konditoreiwaren', UrsprungsbezeichnungenKonditoreiwaren)


class UrsprungsbezeichnungenPflanzen(Base, Vector):
    __tablename__ = 'ursprungsbezeichnungen_pflanzen'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __bodId__ = 'ch.blw.ursprungsbezeichnungen-pflanzen'
    __template__ = 'templates/htmlpopup/ursprungsbezeichnungen.mako'
    __label__ = 'objektcode'
    id = Column('bgdi_id', Integer, primary_key=True)
    objektcode = Column('objektcode', Integer)
    objekt_d = Column('objekt_d', Unicode)
    objekt_f = Column('objekt_f', Unicode)
    objekt_i = Column('objekt_i', Unicode)
    the_geom = Column(Geometry2D)

register('ch.blw.ursprungsbezeichnungen-pflanzen', UrsprungsbezeichnungenPflanzen)


class UrsprungsbezeichnungenSpirituosen(Base, Vector):
    __tablename__ = 'ursprungsbezeichnungen_spirituosen'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __bodId__ = 'ch.blw.ursprungsbezeichnungen-spirituosen'
    __template__ = 'templates/htmlpopup/ursprungsbezeichnungen.mako'
    __label__ = 'objektcode'
    id = Column('bgdi_id', Integer, primary_key=True)
    objektcode = Column('objektcode', Integer)
    objekt_d = Column('objekt_d', Unicode)
    objekt_f = Column('objekt_f', Unicode)
    objekt_i = Column('objekt_i', Unicode)
    the_geom = Column(Geometry2D)

register('ch.blw.ursprungsbezeichnungen-spirituosen', UrsprungsbezeichnungenSpirituosen)
