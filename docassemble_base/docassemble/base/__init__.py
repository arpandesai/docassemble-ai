try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
__version__ = "1.7.7"
