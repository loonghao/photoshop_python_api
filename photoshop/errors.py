from comtypes import COMError


class PhotoshopPythonAPIError(Exception):
    pass


class PhotoshopPythonAPICOMError(COMError):
    pass
