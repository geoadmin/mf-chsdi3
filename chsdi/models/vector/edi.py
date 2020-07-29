# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Float, Unicode

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['edi']


class Arealstatistik2009(Base, Vector):
    __tablename__ = 'arealstatistik_std_2009'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_std.mako'
    __bodId__ = 'ch.bfs.arealstatistik'
    # __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    fj85 = Column('fj85', Integer)
    fj97 = Column('fj97', Integer)
    fj09 = Column('fj09', Integer)
    id_arealstatistik_85 = Column('id_arealstatistik_85', Integer)
    id_arealstatistik_97 = Column('id_arealstatistik_97', Integer)
    id_arealstatistik_09 = Column('id_arealstatistik_09', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik', Arealstatistik2009)


class Arealstatistik1985(Base, Vector):
    __tablename__ = 'arealstatistik_std_1985'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_std.mako'
    __bodId__ = 'ch.bfs.arealstatistik-1985'
    # __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    fj85 = Column('fj85', Integer)
    fj97 = Column('fj97', Integer)
    fj09 = Column('fj09', Integer)
    id_arealstatistik_85 = Column('id_arealstatistik_85', Integer)
    id_arealstatistik_97 = Column('id_arealstatistik_97', Integer)
    id_arealstatistik_09 = Column('id_arealstatistik_09', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik-1985', Arealstatistik1985)


class Arealstatistik1997(Base, Vector):
    __tablename__ = 'arealstatistik_std_1997'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_std.mako'
    __bodId__ = 'ch.bfs.arealstatistik-1997'
    # __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    fj85 = Column('fj85', Integer)
    fj97 = Column('fj97', Integer)
    fj09 = Column('fj09', Integer)
    id_arealstatistik_85 = Column('id_arealstatistik_85', Integer)
    id_arealstatistik_97 = Column('id_arealstatistik_97', Integer)
    id_arealstatistik_09 = Column('id_arealstatistik_09', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik-1997', Arealstatistik1997)


class ArealstatistikBodenbedeckung2009(Base, Vector):
    __tablename__ = 'arealstatistik_nolc_2009'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_nolc.mako'
    __bodId__ = 'ch.bfs.arealstatistik-bodenbedeckung'
    #  __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    fj85 = Column('fj85', Integer)
    fj97 = Column('fj97', Integer)
    fj09 = Column('fj09', Integer)
    id_arealstatistik_nolc_85 = Column('id_arealstatistik_nolc_85', Integer)
    id_arealstatistik_nolc_97 = Column('id_arealstatistik_nolc_97', Integer)
    id_arealstatistik_nolc_09 = Column('id_arealstatistik_nolc_09', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik-bodenbedeckung', ArealstatistikBodenbedeckung2009)


class ArealstatistikBodenbedeckung1997(Base, Vector):
    __tablename__ = 'arealstatistik_nolc_1997'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_nolc.mako'
    __bodId__ = 'ch.bfs.arealstatistik-bodenbedeckung-1997'
    # __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    fj85 = Column('fj85', Integer)
    fj97 = Column('fj97', Integer)
    fj09 = Column('fj09', Integer)
    id_arealstatistik_nolc_85 = Column('id_arealstatistik_nolc_85', Integer)
    id_arealstatistik_nolc_97 = Column('id_arealstatistik_nolc_97', Integer)
    id_arealstatistik_nolc_09 = Column('id_arealstatistik_nolc_09', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik-bodenbedeckung-1997', ArealstatistikBodenbedeckung1997)


class ArealstatistikBodenbedeckung1985(Base, Vector):
    __tablename__ = 'arealstatistik_nolc_1985'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/arealstatistik_nolc.mako'
    __bodId__ = 'ch.bfs.arealstatistik-bodenbedeckung-1985'
    # __minscale__ = 5001
    __maxscale__ = 50000
    # specially big layer
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    fj85 = Column('fj85', Integer)
    fj97 = Column('fj97', Integer)
    fj09 = Column('fj09', Integer)
    id_arealstatistik_nolc_85 = Column('id_arealstatistik_nolc_85', Integer)
    id_arealstatistik_nolc_97 = Column('id_arealstatistik_nolc_97', Integer)
    id_arealstatistik_nolc_09 = Column('id_arealstatistik_nolc_09', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfs.arealstatistik-bodenbedeckung-1985', ArealstatistikBodenbedeckung1985)


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
    __label__ = 'n'
    id = Column('bgdi_id', Integer, primary_key=True)
    haupttype = Column('haupttype', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfs.landschaftswandel', Landschaftswandel)
