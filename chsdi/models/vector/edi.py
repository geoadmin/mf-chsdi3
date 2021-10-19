# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Unicode, SmallInteger, BigInteger, Float, DateTime

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

from chsdi.models.types import DateTimeChsdi

Base = bases['edi']


class Gebaeuderegister(Base, Vector):
    __tablename__ = 'gwr_chsdi'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/gebaeuderegister.mako'
    __bodId__ = 'ch.bfs.gebaeude_wohnungs_register'
    __label__ = 'strname_deinr'
    __extended_info__ = True
    # basic tooltip -> gebaeude_eingang
    id = Column('egid_edid', Unicode, primary_key=True)
    egid = Column('egid', Unicode)
    strname_deinr = Column('strname_deinr', Unicode)
    plz_plz6 = Column('plz_plz6', Unicode)
    dplzname = Column('dplzname', Unicode)
    ggdename = Column('ggdename', Unicode)
    ggdenr = Column('ggdenr', SmallInteger)
    gexpdat = Column('gexpdat', DateTimeChsdi)
    gdekt = Column('gdekt', Unicode)
    the_geom = Column(Geometry2D)
    # extended tooltip -> gebaeude
    egrid = Column('egrid', Unicode)
    lgbkr = Column('lgbkr', SmallInteger)
    lparz = Column('lparz', Unicode)
    lparzsx = Column('lparzsx', BigInteger)
    ltyp = Column('ltyp', SmallInteger)
    gebnr = Column('gebnr', Unicode)
    gbez = Column('gbez', Unicode)
    gkode = Column('gkode', Float)
    gkodn = Column('gkodn', Float)
    gksce = Column('gksce', SmallInteger)
    gstat = Column('gstat', SmallInteger)
    gkat = Column('gkat', SmallInteger)
    gklas = Column('gklas', SmallInteger)
    gbauj = Column('gbauj', SmallInteger)
    gbaum = Column('gbaum', SmallInteger)
    gbaup = Column('gbaup', SmallInteger)
    gabbj = Column('gabbj', SmallInteger)
    garea = Column('garea', Integer)
    gvol = Column('gvol', Integer)
    gvolnorm = Column('gvolnorm', SmallInteger)
    gvolsce = Column('gvolsce', SmallInteger)
    gastw = Column('gastw', SmallInteger)
    ganzwhg = Column('ganzwhg', SmallInteger)
    gazzi = Column('gazzi', SmallInteger)
    # extended tooltip -> eingang
    edid = Column('edid', SmallInteger, nullable=False)
    egaid = Column('egaid', Integer)
    deinr = Column('deinr', Unicode)
    esid = Column('esid', Integer)
    strname = Column('strname', Unicode)
    strnamk = Column('strnamk', Unicode)
    strindx = Column('strindx', Unicode)
    strsp = Column('strsp', Unicode)
    stroffiziel = Column('stroffiziel', Unicode)
    dplz4 = Column('dplz4', SmallInteger)
    dplzz = Column('dplzz', SmallInteger)
    dplzname = Column('dplzname', Unicode)
    dkode = Column('dkode', Float)
    dkodn = Column('dkodn', Float)
    doffadr = Column('doffadr', SmallInteger)
    dexpdat = Column('dexpdat', DateTimeChsdi)
    # extended tooltip -> wohnung
    ewid = Column('ewid', SmallInteger, nullable=False)
    whgnr = Column('whgnr', Unicode)
    wstwk = Column('wstwk', SmallInteger)
    wmehrg = Column('wmehrg', SmallInteger)
    weinr = Column('weinr', Unicode)
    wbez = Column('wbez', Unicode)
    wstat = Column('wstat', SmallInteger)
    wexpdat = Column('wexpdat', DateTime)

register('ch.bfs.gebaeude_wohnungs_register', Gebaeuderegister)


class Arealstatistik(Base, Vector):
    __tablename__ = 'arealstatistik_std'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_std.mako'
    __bodId__ = 'ch.bfs.arealstatistik'
    # __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    survey = Column('survey', Integer)
    fj = Column('fj', Integer)
    as_72 = Column('as_72', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik', Arealstatistik)


class ArealstatistikBodenbedeckung(Base, Vector):
    __tablename__ = 'arealstatistik_nolc'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_nolc.mako'
    __bodId__ = 'ch.bfs.arealstatistik-bodenbedeckung'
    #  __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    survey = Column('survey', Integer)
    fj = Column('fj', Integer)
    lc_27 = Column('lc_27', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik-bodenbedeckung', ArealstatistikBodenbedeckung)


class ArealstatistikBodennutzung(Base, Vector):
    __tablename__ = 'arealstatistik_nolu_2009'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_nolu.mako'
    __bodId__ = 'ch.bfs.arealstatistik-bodennutzung'
    # __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    fj85 = Column('fj85', Integer)
    fj97 = Column('fj97', Integer)
    fj09 = Column('fj09', Integer)
    id_arealstatistik_nolu_85 = Column('id_arealstatistik_nolu_85', Integer)
    id_arealstatistik_nolu_97 = Column('id_arealstatistik_nolu_97', Integer)
    id_arealstatistik_nolu_09 = Column('id_arealstatistik_nolu_09', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik-bodennutzung', ArealstatistikBodennutzung)


class ArealstatistikBodennutzung1997(Base, Vector):
    __tablename__ = 'arealstatistik_nolu_1997'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_nolu.mako'
    __bodId__ = 'ch.bfs.arealstatistik-bodennutzung-1997'
    # __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    fj85 = Column('fj85', Integer)
    fj97 = Column('fj97', Integer)
    fj09 = Column('fj09', Integer)
    id_arealstatistik_nolu_85 = Column('id_arealstatistik_nolu_85', Integer)
    id_arealstatistik_nolu_97 = Column('id_arealstatistik_nolu_97', Integer)
    id_arealstatistik_nolu_09 = Column('id_arealstatistik_nolu_09', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik-bodennutzung-1997', ArealstatistikBodennutzung1997)


class ArealstatistikBodennutzung1985(Base, Vector):
    __tablename__ = 'arealstatistik_nolu_1985'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_nolu.mako'
    __bodId__ = 'ch.bfs.arealstatistik-bodennutzung-1985'
    # __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    fj85 = Column('fj85', Integer)
    fj97 = Column('fj97', Integer)
    fj09 = Column('fj09', Integer)
    id_arealstatistik_nolu_85 = Column('id_arealstatistik_nolu_85', Integer)
    id_arealstatistik_nolu_97 = Column('id_arealstatistik_nolu_97', Integer)
    id_arealstatistik_nolu_09 = Column('id_arealstatistik_nolu_09', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik-bodennutzung-1985', ArealstatistikBodennutzung1985)


class RadonKarte(Base, Vector):
    __tablename__ = 'radonkarte'
    __table_args__ = ({'schema': 'bag', 'autoload': False})
    __template__ = 'templates/htmlpopup/radonkarte.mako'
    __bodId__ = 'ch.bag.radonkarte'
    __label__ = 'probability_prozent'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)
    probability_prozent = Column('probability_prozent', Integer)
    confidence = Column('confidence', Float)

register('ch.bag.radonkarte', RadonKarte)


class FsmeFaelle(Base, Vector):
    __tablename__ = 'fsme_faelle'
    __table_args__ = ({'schema': 'bag', 'autoload': False})
    __template__ = 'templates/htmlpopup/fsme.mako'
    __bodId__ = 'ch.bag.zecken-fsme-faelle'
    __label__ = 'gemname'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)
    gemname = Column('gemname', Integer)
    bfsnr = Column('bfsnr', Integer)

register('ch.bag.zecken-fsme-faelle', FsmeFaelle)


class FsmeImpfung(Base, Vector):
    __tablename__ = 'fsme_impfung'
    __table_args__ = ({'schema': 'bag', 'autoload': False})
    __template__ = 'templates/htmlpopup/fsme.mako'
    __bodId__ = 'ch.bag.zecken-fsme-impfung'
    __label__ = 'gemname'
    id = Column('bgdi_id', Integer, primary_key=True)
    gemname = Column('gemname', Integer)
    bfsnr = Column('bfsnr', Integer)
    the_geom = Column(Geometry2D)

register('ch.bag.zecken-fsme-impfung', FsmeImpfung)


class RadioaktivitaetAtmosphaere(Base, Vector):
    __tablename__ = 'radioaktivitaet'
    __table_args__ = ({'schema': 'bag', 'autoload': False})
    __template__ = 'templates/htmlpopup/radioaktivitaet_atmosphaere.mako'
    __bodId__ = 'ch.bag.radioaktivitaet-atmosphaere'
    __label__ = 'station'
    id = Column('bgdi_id', Integer, primary_key=True)
    station = Column('station', Unicode)
    period = Column('period', Unicode)
    nuc1 = Column('nuc1', Unicode)
    nuc2 = Column('nuc2', Unicode)
    nuc3 = Column('nuc3', Unicode)
    nuc4 = Column('nuc4', Unicode)
    nuc5 = Column('nuc5', Unicode)
    stationlink = Column('stationlink', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bag.radioaktivitaet-atmosphaere', RadioaktivitaetAtmosphaere)


class VolkBetriebZaehlung:
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/volk_betrieb_zaehlung.mako'
    __label__ = 'reli'
    __timeInstant__ = 'i_year'
    id = Column('bgdi_id', Integer, primary_key=True)
    i_year = Column('i_year', Unicode)
    reli = Column('reli', Integer)
    number = Column('i_number', Integer)
    the_geom = Column(Geometry2D)


class VolkszaehlungBevEinwohner(Base, VolkBetriebZaehlung, Vector):
    __tablename__ = 'v_volkszaehlung_bevoelkerung_einwohner'
    __bodId__ = 'ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner'

register(VolkszaehlungBevEinwohner.__bodId__, VolkszaehlungBevEinwohner)


class VolkszaehlungGebaeudeGebaude(Base, VolkBetriebZaehlung, Vector):
    __tablename__ = 'v_volkszaehlung_gebaeude_gebaeude'
    __bodId__ = 'ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude'

register(VolkszaehlungGebaeudeGebaude.__bodId__, VolkszaehlungGebaeudeGebaude)


class VolkszaehlungGebaudeWohnungen(Base, VolkBetriebZaehlung, Vector):
    __tablename__ = 'v_volkszaehlung_gebaeude_wohnungen'
    __bodId__ = 'ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen'

register(VolkszaehlungGebaudeWohnungen.__bodId__, VolkszaehlungGebaudeWohnungen)


class VolkszaehlungBetriebArbeitstaetten(Base, VolkBetriebZaehlung, Vector):
    __tablename__ = 'v_betriebsszaehlung_arbeitsstaetten'
    __bodId__ = 'ch.bfs.betriebszaehlungen-arbeitsstaetten'

register(VolkszaehlungBetriebArbeitstaetten.__bodId__, VolkszaehlungBetriebArbeitstaetten)


class VolkszaehlungBetriebBeschaeftigte(Base, VolkBetriebZaehlung, Vector):
    __tablename__ = 'v_betriebsszaehlung_beschaeft_voll'
    __bodId__ = 'ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente'

register(VolkszaehlungBetriebBeschaeftigte.__bodId__, VolkszaehlungBetriebBeschaeftigte)


class GenGrenzenAgglo:
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/gen_grenzen_agglo.mako'
    __label__ = 'gmd_nr'
    id = Column('bgdi_id', Integer, primary_key=True)
    gmd_name = Column('gmd_name', Unicode)
    gmd_nr = Column('gmd_nr', Integer)
    acode = Column('acode', Integer)
    aname = Column('aname', Unicode)
    area_ha = Column('area_ha', Float)
    the_geom = Column(Geometry2D)


class GenGrenzenAggloG1(Base, GenGrenzenAgglo, Vector):
    __tablename__ = 'gen_grenzen_agglo_g1'
    __bodId__ = 'ch.bfs.generalisierte-grenzen_agglomerationen_g1'

register(GenGrenzenAggloG1.__bodId__, GenGrenzenAggloG1)


class GenGrenzenAggloG2(Base, GenGrenzenAgglo, Vector):
    __tablename__ = 'gen_grenzen_agglo_g2'
    __bodId__ = 'ch.bfs.generalisierte-grenzen_agglomerationen_g2'

register(GenGrenzenAggloG2.__bodId__, GenGrenzenAggloG2)


class Landschaftswandel(Base, Vector):
    __tablename__ = 'landschaftswandel'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/landschaftswandel.mako'
    __bodId__ = 'ch.bfs.landschaftswandel'
    __label__ = 'haupttyp'
    id = Column('bgdi_id', Integer, primary_key=True)
    gmde = Column('gmde', Unicode)
    swissnames = Column('swissnames', Unicode)
    haupttyp = Column('haupttyp', Unicode)
    typ1 = Column('typ1', Unicode)
    typ2 = Column('typ2', Unicode)
    typ3 = Column('typ3', Unicode)
    typ4 = Column('typ4', Unicode)
    typ1_de = Column('typ1_de', Unicode)
    typ2_de = Column('typ2_de', Unicode)
    typ3_de = Column('typ3_de', Unicode)
    typ4_de = Column('typ4_de', Unicode)
    typ1_fr = Column('typ1_fr', Unicode)
    typ2_fr = Column('typ2_fr', Unicode)
    typ3_fr = Column('typ3_fr', Unicode)
    typ4_fr = Column('typ4_fr', Unicode)
    typ1_it = Column('typ1_it', Unicode)
    typ2_it = Column('typ2_it', Unicode)
    typ3_it = Column('typ3_it', Unicode)
    typ4_it = Column('typ4_it', Unicode)
    typ1_en = Column('typ1_en', Unicode)
    typ2_en = Column('typ2_en', Unicode)
    typ3_en = Column('typ3_en', Unicode)
    typ4_en = Column('typ4_en', Unicode)
    linkdownload_de = Column('linkdownload_de', Unicode)
    linkdownload_fr = Column('linkdownload_fr', Unicode)
    linkdownload_it = Column('linkdownload_it', Unicode)
    linkdownload_en = Column('linkdownload_en', Unicode)
    linkbild = Column('linkbild', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfs.landschaftswandel', Landschaftswandel)
