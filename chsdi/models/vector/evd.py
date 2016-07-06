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
    # __queryable_attributes__ = ['farbe']
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


class Emapis:
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __label__ = 'typ'
    __template__ = 'templates/htmlpopup/emapis.mako'
    id = Column('xtf_id', Integer, primary_key=True)
    typ = Column('typ', Unicode)
    typ_de = Column('typ_de', Unicode)
    typ_fr = Column('typ_fr', Unicode)
    typ_it = Column('typ_it', Unicode)
    status_de = Column('status_de', Unicode)
    status_fr = Column('status_fr', Unicode)
    status_it = Column('status_it', Unicode)
    geschaeftsnummer = Column('geschaeftsnummer', Unicode)
    the_geom = Column(Geometry2D)


class EmapisBeizugsgebiet(Base, Emapis, Vector):
    __tablename__ = 'emapis_beizugsgebiet'
    __bodId__ = 'ch.blw.emapis-beizugsgebiet'

register('ch.blw.emapis-beizugsgebiet', EmapisBeizugsgebiet)


class EmapisBewaesserung(Base, Emapis, Vector):
    __tablename__ = 'emapis_bewaesserung'
    __bodId__ = 'ch.blw.emapis-bewaesserung'

register('ch.blw.emapis-bewaesserung', EmapisBewaesserung)


class EmapisElektrizitaetsversorgung(Base, Emapis, Vector):
    __tablename__ = 'emapis_elektrizitaetsversorgung'
    __bodId__ = 'ch.blw.emapis-elektrizitaetsversorgung'

register('ch.blw.emapis-elektrizitaetsversorgung', EmapisElektrizitaetsversorgung)


class EmapisEntwaesserung(Base, Emapis, Vector):
    __tablename__ = 'emapis_entwaesserung'
    __bodId__ = 'ch.blw.emapis-entwaesserung'

register('ch.blw.emapis-entwaesserung', EmapisEntwaesserung)


class EmapisHochbau(Base, Emapis, Vector):
    __tablename__ = 'emapis_hochbau'
    __bodId__ = 'ch.blw.emapis-hochbau'

register('ch.blw.emapis-hochbau', EmapisHochbau)


class EmapisMilchleitung(Base, Emapis, Vector):
    __tablename__ = 'emapis_milchleitung'
    __bodId__ = 'ch.blw.emapis-milchleitung'

register('ch.blw.emapis-milchleitung', EmapisMilchleitung)


class EmapisOekologie(Base, Emapis, Vector):
    __tablename__ = 'emapis_oekologie'
    __bodId__ = 'ch.blw.emapis-oekologie'

register('ch.blw.emapis-oekologie', EmapisOekologie)


class EmapisProjektschwerpunkt(Base, Emapis, Vector):
    __tablename__ = 'emapis_projektschwerpunkt'
    __bodId__ = 'ch.blw.emapis-projektschwerpunkt'

register('ch.blw.emapis-projektschwerpunkt', EmapisProjektschwerpunkt)


class EmapisSeilbahnen(Base, Emapis, Vector):
    __tablename__ = 'emapis_seilbahnen'
    __bodId__ = 'ch.blw.emapis-seilbahnen'

register('ch.blw.emapis-seilbahnen', EmapisSeilbahnen)


class EmapisWasserversorgung(Base, Emapis, Vector):
    __tablename__ = 'emapis_wasserversorgung'
    __bodId__ = 'ch.blw.emapis-wasserversorgung'

register('ch.blw.emapis-wasserversorgung', EmapisWasserversorgung)


class EmapisWegebau(Base, Emapis, Vector):
    __tablename__ = 'emapis_wegebau'
    __bodId__ = 'ch.blw.emapis-wegebau'

register('ch.blw.emapis-wegebau', EmapisWegebau)
