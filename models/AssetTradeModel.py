# encoding:utf8

from __future__ import unicode_literals

from sqlalchemy import Integer

from models.CommonModel import *

__all__ = ['AssetTrade']


class AssetTrade(MixinBase):
    asset_class = Column(String(50), default='')
    amount = Column(Float, default=0.0)
    type = Column(Integer, default=1)

    def __init__(self, asset_class='', amount=0.0, type=1):
        MixinBase.__init__(self)
        self.asset_class = asset_class
        self.amount = amount
        self.type = type

    def __repr__(self):
        return '<AssetTrade id=%s, asset_class=%s, amount=%s, type=%s>' % (
            self.id, self.asset_class, self.amount, self.type)