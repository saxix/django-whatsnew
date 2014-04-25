# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django_dynamic_fixture import G
import pytest

from whatsnew import get_version
from whatsnew.models import WhatsNew
from whatsnew.templatetags.whatsnew import whatsnew
from whatsnew.version import Version
from django.test.client import RequestFactory


def test_version():
    v100 = Version('1.0.0')
    v10 = Version('1.0')
    v11 = Version('1.1')
    v10a = Version('1.0alpha')
    v10b = Version('1.0beta')
    v10dev = Version('1.0dev')
    v10rc = Version('1.0rc')

    v001 = Version('0.0.1')

    assert v10 > v001
    assert v100 == v10
    assert v10 < v11
    assert v11 > v10
    assert v10a < v10
    assert v10b < v10
    assert v10dev < v10
    assert v10rc < v10


@pytest.mark.django_db
def test_templatetag():
    current = get_version()
    factory = RequestFactory()

    G(WhatsNew, version=current, enabled=True, expire=None)
    factory.cookies['whatsnew-whatsnew'] = '0.0'
    request = factory.get('/')
    ret = whatsnew({'request': request}, 'whatsnew')

    assert ret['display']

    factory.cookies['whatsnew-whatsnew'] = current
    request = factory.get('/')
    ret = whatsnew({'request': request}, 'whatsnew')

    assert not ret['display']

    factory.cookies['whatsnew-whatsnew'] = current + '.1'
    request = factory.get('/')
    ret = whatsnew({'request': request}, 'whatsnew')

    assert not ret['display']


@pytest.mark.django_db
def test_ordering():
    G(WhatsNew, version='0.1', enabled=True, expire=None)
    G(WhatsNew, version='0.3', enabled=True, expire=None)
    assert list(WhatsNew.objects.values_list('pk', flat=True)) == [2, 1]

    G(WhatsNew, version='0.2', enabled=True, expire=None)
    assert list(WhatsNew.objects.values_list('pk', flat=True)) == [2, 3, 1]
    assert WhatsNew.objects.latest().pk == 2
