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
class ProjektierungszonenNationalstrassenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'projektierungszonen_nationalstrassen_v2_0_oereb'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __bodId__ = 'ch.astra.projektierungszonen-nationalstrassen_v2_0.oereb'

register_oereb(ProjektierungszonenNationalstrassenV20Oereb.__bodId__, ProjektierungszonenNationalstrassenV20Oereb)


class BaulinienNationalstrassenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'baulinien_nationalstrassen_v2_0_oereb'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __bodId__ = 'ch.astra.baulinien-nationalstrassen_v2_0.oereb'

register_oereb(BaulinienNationalstrassenV20Oereb.__bodId__, BaulinienNationalstrassenV20Oereb)


# class BaulinienNationalstrasseniAenderungV20Oereb(Base, OerebBase, Vector):
#     __tablename__ = 'baulinien_nationalstrassen_aenderung_v2_0_oereb'
#     __table_args__ = ({'schema': 'astra', 'autoload': False})
#     __bodId__ = 'ch.astra.baulinien-nationalstrassen_aenderung_v2_0.oereb'
#
# register_oereb(BaulinienNationalstrassenV20Oereb.__bodId__, BaulinienNationalstrassenV20Oereb)

# BFE
class BaulinienStarkstromV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'baulinien_starkstromanlagen_v2_0_oereb'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __bodId__ = 'ch.bfe.baulinien-starkstromanlagen_v2_0.oereb'

register_oereb(BaulinienStarkstromV20Oereb.__bodId__, BaulinienStarkstromV20Oereb)


class ProjektierungStarkstromV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'projektierungszonen_starkstromanlagen_v2_0_oereb'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __bodId__ = 'ch.bfe.projektierungszonen-starkstromanlagen_v2_0.oereb'

register_oereb(ProjektierungStarkstromV20Oereb.__bodId__, ProjektierungStarkstromV20Oereb)


# BAV
class KatasterBelastetenStandorteOevV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'kataster_belasteter_standorte_oev_v2_0_oereb'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.kataster-belasteter-standorte-oev_v2_0.oereb'

register_oereb(KatasterBelastetenStandorteOevV20Oereb.__bodId__, KatasterBelastetenStandorteOevV20Oereb)


class ProjektierungszonenEisenbahnanlagenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'projektierungszonen_eisenbahnanlagen_v2_0_oereb'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.projektierungszonen-eisenbahnanlagen_v2_0.oereb'

register_oereb(ProjektierungszonenEisenbahnanlagenV20Oereb.__bodId__, ProjektierungszonenEisenbahnanlagenV20Oereb)


class BaulinienEisenbahnanlagenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'baulinien_eisenbahnanlagen_v2_0_oereb'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.baulinien-eisenbahnanlagen_v2_0.oereb'

register_oereb(BaulinienEisenbahnanlagenV20Oereb.__bodId__, BaulinienEisenbahnanlagenV20Oereb)


# BAZL
class ProjektierungszonenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'projektierungszonen_v2_0_oereb'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.projektierungszonen-flughafenanlagen_v2_0.oereb'

register_oereb(ProjektierungszonenV20Oereb.__bodId__, ProjektierungszonenV20Oereb)


class SichereitszonenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'sichereitszonen_v2_0_oereb'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.sicherheitszonenplan_v2_0.oereb'

register_oereb(SichereitszonenV20Oereb.__bodId__, SichereitszonenV20Oereb)


# class SichereitszonenAenderungV20Oereb(Base, OerebBase, Vector):
#     __tablename__ = 'sichereitszonen_v2_0_oereb'
#     __table_args__ = ({'schema': 'bazl', 'autoload': False})
#     __bodId__ = 'ch.bazl.sicherheitszonenplan_aenderun_v2_0.oereb'
#
# register_oereb(SichereitszonenAenderungV20Oereb.__bodId__, SichereitszonenAenderungV20Oereb)


class KatasterBelastetenStandorteZivflplV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'kataster_belasteter_standorte_zivflpl_v2_0_oereb'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.kataster-belasteter-standorte-zivilflugplaetze_v2_0.oereb'

register_oereb(KatasterBelastetenStandorteZivflplV20Oereb.__bodId__, KatasterBelastetenStandorteZivflplV20Oereb)


class BaulinienFlughafenanlagenV20Oereb(Base, OerebBase, Vector):
    __tablename__ = 'baulinien_flughafenanlagen_v2_0_oereb'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.baulinien-flughafenanlagen_v2_0.oereb'

register_oereb(BaulinienFlughafenanlagenV20Oereb.__bodId__, BaulinienFlughafenanlagenV20Oereb)
