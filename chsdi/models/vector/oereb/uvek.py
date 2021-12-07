# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode

from chsdi.models import register_oereb, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['uvek']


class OerebBase:
    id = Column('stabil_id', Unicode, primary_key=True)
    the_geom = Column(Geometry2D)
    geomType = Column('geom_type', Unicode)
    xmlData = Column('xml_data', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    data_created = Column('data_created', Unicode)


# ASTRA
class ProjektierungszonenNationalstrassenOereb(Base, OerebBase, Vector):
    __tablename__ = 'projektierungszonen_nationalstrassen_oereb'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __bodId__ = 'ch.astra.projektierungszonen-nationalstrassen.oereb'

register_oereb(ProjektierungszonenNationalstrassenOereb.__bodId__, ProjektierungszonenNationalstrassenOereb)


class ProjektierungszonenNationalstrassenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'projektierungszonen_nationalstrassen_v2_0_oereb'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __bodId__ = 'ch.astra.projektierungszonen-nationalstrassen_v2_0.oereb'

register_oereb(ProjektierungszonenNationalstrassenV20Oereb.__bodId__, ProjektierungszonenNationalstrassenV20Oereb)


class BaulinienNationalstrassenOereb(Base, OerebBase, Vector):
    __tablename__ = 'baulinien_nationalstrassen_oereb'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __bodId__ = 'ch.astra.baulinien-nationalstrassen.oereb'

register_oereb(BaulinienNationalstrassenOereb.__bodId__, BaulinienNationalstrassenOereb)


# BAV
class KatasterBelastetenStandorteOevOereb(Base, OerebBase, Vector):
    __tablename__ = 'kataster_belasteter_standorte_oev_oereb'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.kataster-belasteter-standorte-oev.oereb'

register_oereb(KatasterBelastetenStandorteOevOereb.__bodId__, KatasterBelastetenStandorteOevOereb)


class ProjektierungszonenEisenbahnanlagenOereb(Base, OerebBase, Vector):
    __tablename__ = 'projektierungszonen_eisenbahnanlagen_oereb'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.projektierungszonen-eisenbahnanlagen.oereb'

register_oereb(ProjektierungszonenEisenbahnanlagenOereb.__bodId__, ProjektierungszonenEisenbahnanlagenOereb)


class ProjektierungszonenEisenbahnanlagenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'projektierungszonen_eisenbahnanlagen_v2_0_oereb'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.projektierungszonen-eisenbahnanlagen_v2_0.oereb'

register_oereb(ProjektierungszonenEisenbahnanlagenV20Oereb.__bodId__, ProjektierungszonenEisenbahnanlagenV20Oereb)


class BaulinienEisenbahnanlagenOereb(Base, OerebBase, Vector):
    __tablename__ = 'baulinien_eisenbahnanlagen_oereb'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.baulinien-eisenbahnanlagen.oereb'

register_oereb(BaulinienEisenbahnanlagenOereb.__bodId__, BaulinienEisenbahnanlagenOereb)


class BaulinienEisenbahnanlagenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'baulinien_eisenbahnanlagen_v2_0_oereb'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.baulinien-eisenbahnanlagen_v2_0.oereb'

register_oereb(BaulinienEisenbahnanlagenV20Oereb.__bodId__, BaulinienEisenbahnanlagenV20Oereb)


# BAZL
class ProjektierungszonenOereb(Base, OerebBase, Vector):
    __tablename__ = 'projektierungszonen_oereb'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.projektierungszonen-flughafenanlagen.oereb'

register_oereb(ProjektierungszonenOereb.__bodId__, ProjektierungszonenOereb)


class SichereitszonenOereb(Base, OerebBase, Vector):
    __tablename__ = 'sichereitszonen_oereb'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.sicherheitszonenplan.oereb'

register_oereb(SichereitszonenOereb.__bodId__, SichereitszonenOereb)


class KatasterBelastetenStandorteZivflplOereb(Base, OerebBase, Vector):
    __tablename__ = 'kataster_belasteter_standorte_zivflpl_oereb'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.kataster-belasteter-standorte-zivilflugplaetze.oereb'

register_oereb(KatasterBelastetenStandorteZivflplOereb.__bodId__, KatasterBelastetenStandorteZivflplOereb)


class KatasterBelastetenStandorteZivflplV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'kataster_belasteter_standorte_zivflpl_v2_0_oereb'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.kataster-belasteter-standorte-zivilflugplaetze_v2_0.oereb'

register_oereb(KatasterBelastetenStandorteZivflplV20Oereb.__bodId__, KatasterBelastetenStandorteZivflplV20Oereb)


class BaulinienFlughafenanlagenOereb(Base, OerebBase, Vector):
    __tablename__ = 'baulinien_flughafenanlagen_oereb'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.baulinien-flughafenanlagen.oereb'

register_oereb(BaulinienFlughafenanlagenOereb.__bodId__, BaulinienFlughafenanlagenOereb)


class BaulinienFlughafenanlagenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'baulinien_flughafenanlagen_v2_0_oereb'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.baulinien-flughafenanlagen_v2_0.oereb'

register_oereb(BaulinienFlughafenanlagenV20Oereb.__bodId__, BaulinienFlughafenanlagenV20Oereb)
