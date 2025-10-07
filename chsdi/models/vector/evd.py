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

register(Kulturtyp.__bodId__, Kulturtyp)


class Gruendigkeit(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-gruendigkeit'

register(Gruendigkeit.__bodId__, Gruendigkeit)


class Skelettgehalt(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-skelettgehalt'

register(Skelettgehalt.__bodId__, Skelettgehalt)


class Wasserspeichervermoegen(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-wasserspeichervermoegen'

register(Wasserspeichervermoegen.__bodId__, Wasserspeichervermoegen)


class Naehrstoffspeichervermoegen(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-naehrstoffspeichervermoegen'

register(Naehrstoffspeichervermoegen.__bodId__, Naehrstoffspeichervermoegen)


class Wasserdurchlaessigkeit(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-wasserdurchlaessigkeit'

register(Wasserdurchlaessigkeit.__bodId__, Wasserdurchlaessigkeit)


class Vernaessung(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-vernaessung'

register(Vernaessung.__bodId__, Vernaessung)


class Kulturland(Base, Bodeneignung, Vector):
    __bodId__ = 'ch.blw.bodeneignung-kulturland'

register(Kulturland.__bodId__, Kulturland)


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

register(KlimaeignungTyp.__bodId__, KlimaeignungTyp)


class KlimaeignungKoernermais(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-koernermais'

register(KlimaeignungKoernermais.__bodId__, KlimaeignungKoernermais)


class KlimaeignungSpezialkulturen(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-spezialkulturen'

register(KlimaeignungSpezialkulturen.__bodId__, KlimaeignungSpezialkulturen)


class KlimaeignungZwischenfruchtbau(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-zwischenfruchtbau'

register(KlimaeignungZwischenfruchtbau.__bodId__, KlimaeignungZwischenfruchtbau)


class KlimaeignungKartoffeln(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-kartoffeln'

register(KlimaeignungKartoffeln.__bodId__, KlimaeignungKartoffeln)


class KlimaeignungGetreidebau(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-getreidebau'

register(KlimaeignungGetreidebau.__bodId__, KlimaeignungGetreidebau)


class KlimaeignungFutterbau(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-futterbau'

register(KlimaeignungFutterbau.__bodId__, KlimaeignungFutterbau)


class KlimaeignungKulturland(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.klimaeignung-kulturland'

register(KlimaeignungKulturland.__bodId__, KlimaeignungKulturland)


class Niederschlagshaushalt(Base, Klimaeignung, Vector):
    __bodId__ = 'ch.blw.niederschlagshaushalt'

register(Niederschlagshaushalt.__bodId__, Niederschlagshaushalt)


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

register(UrsprungsbezeichnungenFleisch.__bodId__, UrsprungsbezeichnungenFleisch)


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

register(UrsprungsbezeichnungenKaese.__bodId__, UrsprungsbezeichnungenKaese)


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

register(UrsprungsbezeichnungenKonditoreiwaren.__bodId__, UrsprungsbezeichnungenKonditoreiwaren)


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

register(UrsprungsbezeichnungenPflanzen.__bodId__, UrsprungsbezeichnungenPflanzen)


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

register(UrsprungsbezeichnungenSpirituosen.__bodId__, UrsprungsbezeichnungenSpirituosen)


class Milchmarktregionen(Base, Vector):
    __tablename__ = 'highlight_v_milchmarktregionen'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __bodId__ = 'ch.blw.milchmarktregionen'
    __template__ = 'templates/htmlpopup/milchmarktregionen.mako'
    __label__ = 'milchreg'
    id = Column('reg', Integer, primary_key=True)
    milchreg = Column('milchreg', Unicode)
    bez_de = Column('bez_de', Unicode)
    bez_fr = Column('bez_fr', Unicode)
    bez_it = Column('bez_it', Unicode)
    bez_en = Column('bez_en', Unicode)
    bez_rm = Column('bez_rm', Unicode)
    the_geom = Column(Geometry2D)

register(Milchmarktregionen.__bodId__, Milchmarktregionen)


class SachplanCernAnhoerungFac:
    __table_args__ = ({'schema': 'sbfi', 'autoload': False})
    __bodId__ = 'ch.sbfi.sachplan-cern_anhoerung'
    __label__ = 'objname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    fackind_text_de = Column('fackind_text_de', Unicode)
    fackind_text_fr = Column('fackind_text_fr', Unicode)
    fackind_text_it = Column('fackind_text_it', Unicode)
    facstatus_text_de = Column('facstatus_text_de', Unicode)
    facstatus_text_fr = Column('facstatus_text_fr', Unicode)
    facstatus_text_it = Column('facstatus_text_it', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    title_de = Column('title_de', Unicode)
    title_fr = Column('title_fr', Unicode)
    title_it = Column('title_it', Unicode)
    doc_web_de = Column('doc_web_de', Unicode)
    doc_web_fr = Column('doc_web_fr', Unicode)
    doc_web_it = Column('doc_web_it', Unicode)
    the_geom = Column(Geometry2D)


class SachplanCernAnhoerungFacPnt(Base, SachplanCernAnhoerungFac, Vector):
    __tablename__ = 'sachplan_cern_anhoerung_fac_pnt'
    __template__ = 'templates/htmlpopup/sbfi_sachplan_cern_anhoerung_fac_pnt.mako'

register(SachplanCernAnhoerungFacPnt.__bodId__, SachplanCernAnhoerungFacPnt)


class SachplanCernAnhoerungFacLine(Base, SachplanCernAnhoerungFac, Vector):
    __tablename__ = 'sachplan_cern_anhoerung_fac_line'
    __template__ = 'templates/htmlpopup/sbfi_sachplan_cern_anhoerung_fac_line.mako'

register(SachplanCernAnhoerungFacLine.__bodId__, SachplanCernAnhoerungFacLine)


class SachplanCernAnhoerungPlm:
    __table_args__ = ({'schema': 'sbfi', 'autoload': False})
    __bodId__ = 'ch.sbfi.sachplan-cern_anhoerung'
    __label__ = 'plname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_text_de = Column('coordlevel_text_de', Unicode)
    coordlevel_text_fr = Column('coordlevel_text_fr', Unicode)
    coordlevel_text_it = Column('coordlevel_text_it', Unicode)
    plstatus_text_de = Column('plstatus_text_de', Unicode)
    plstatus_text_fr = Column('plstatus_text_fr', Unicode)
    plstatus_text_it = Column('plstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    title_de = Column('title_de', Unicode)
    title_fr = Column('title_fr', Unicode)
    title_it = Column('title_it', Unicode)
    doc_web_de = Column('doc_web_de', Unicode)
    doc_web_fr = Column('doc_web_fr', Unicode)
    doc_web_it = Column('doc_web_it', Unicode)
    the_geom = Column(Geometry2D)


class SachplanCernAnhoerungPlmPoly(Base, SachplanCernAnhoerungPlm, Vector):
    __tablename__ = 'sachplan_cern_anhoerung_plm_poly'
    __template__ = 'templates/htmlpopup/sbfi_sachplan_cern_anhoerung_plm_poly.mako'

register(SachplanCernAnhoerungPlmPoly.__bodId__, SachplanCernAnhoerungPlmPoly)


class LandwirtschaftlicheNutzungsflaechen(Base, Vector):
    __tablename__ = 'landwirtschaftliche_nutzungsflaechen'
    __table_args__ = ({'schema': 'blw', 'autoload': False})
    __bodId__ = 'ch.blw.landwirtschaftliche-nutzungsflaechen'
    __template__ = 'templates/htmlpopup/blw_landwirtschaftliche_nutzungsflaechen.mako'
    __label__ = 't_id'
    id = Column('bgdi_id', Integer, primary_key=True)
    t_id = Column('t_id', Unicode)
    bezugsjahr = Column('bezugsjahr', Integer)
    lnf_code = Column('lnf_code', Integer)
    nutzungsidentifikator = Column('nutzungsidentifikator', Unicode)
    bewirtschaftungsgrad = Column('bewirtschaftungsgrad', Integer)
    flaeche_m2 = Column('flaeche_m2', Integer)
    bff_qualitaet_1 = Column('bff_qualitaet_1', Integer)
    hauptkategorie_de = Column('hauptkategorie_de', Unicode)
    hauptkategorie_fr = Column('hauptkategorie_fr', Unicode)
    hauptkategorie_it = Column('hauptkategorie_it', Unicode)
    nutzung_de = Column('nutzung_de', Unicode)
    nutzung_fr = Column('nutzung_fr', Unicode)
    nutzung_it = Column('nutzung_it', Unicode)
    bur_nr = Column('bur_nr', Unicode)
    the_geom = Column(Geometry2D)

register(LandwirtschaftlicheNutzungsflaechen.__bodId__, LandwirtschaftlicheNutzungsflaechen)
