from types import StringTypes
import pkg_resources


class Version(object):
    def __init__(self, vstring):
        self._components = pkg_resources.parse_version(vstring)
        self.string = vstring
        self._patch = []
        for i, part in enumerate(self._components):
            if '*' in part:
                break
        if len(self._components) > i:
            self._patch = map(lambda x: x.replace('*', ''), self._components[i + 1:-1])
        parts = list(self._components[:i])
        parts.extend('0' * (3 - len(parts)))

        self._parts = map(int, parts)

        self._status = self._components[i][1]

    def same(self, other):
        return self._parts == other._parts

    def __str__(self):
        return self.string

    def __repr__(self):
        return "Version ('%s')" % str(self)

    def __unicode__(self):
        return unicode(str(self))

    def __cmp__(self, other):
        if isinstance(other, StringTypes):
            other = Version(other)
        if not other:
            return None
        return cmp(self._components, other._components)

    @property
    def major(self):
        return self._parts[0]

    @property
    def minor(self):
        return self._parts[1]

    @property
    def release(self):
        return self._parts[2]

    @property
    def patch(self):
        return ".".join(self._patch)

    @property
    def status(self):
        if self._status == '@':
            return "nighlybuild"
        return self._status

    @property
    def version(self):
        return self._parts + [self.status] + [self.patch]
