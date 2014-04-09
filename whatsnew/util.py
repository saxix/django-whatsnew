import pkg_resources


def get_version(package_name):
    version = None
    try:
        version = pkg_resources.require(package_name)[0].version
    except pkg_resources.DistributionNotFound:
        module = __import__(package_name)
        try:
            func = getattr(module, 'get_version')
            version = func()
        except:
            for attempt in ('version', 'VERSION', '__version__'):
                try:
                    version = getattr(module, attempt)
                    if isinstance(version, (list, tuple)):
                        version = ".".join(version)
                except AttributeError:
                    pass

    if version:
        return str(version)
    else:
        raise pkg_resources.DistributionNotFound
