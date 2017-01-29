
class PackageInfo:
    def __init__(self, packageName, label):
        self.packageName = packageName
        self.label = label

class GooglePalyConstants:
    _URL_PREFIX = 'https://play.google.com/store/apps/'
    COLLECTION_TOPSELLING_FREE = '/collection/topselling_free'
    COLLECTION_TOPSELLING_PAID = '/collection/topselling_paid'
    COLLECTION_TOPGROSSING = '/collection/topgrossing'
    _CATEGORY_PREFIX = 'category/'
    CATEGORY_GAME = _CATEGORY_PREFIX+'GAME'
    CATEGORY_COMMUNICATION = _CATEGORY_PREFIX+'COMMUNICATION'
    CATEGORY_SOCIAL = _CATEGORY_PREFIX+'SOCIAL'
    @staticmethod
    def url(category, collection):
        url = GooglePalyConstants._URL_PREFIX+category+collection
        return url

if __name__ == '__main__':
    pInfo = PackageInfo('testPkgName','testPkgLabel')
    print("PackageInfo:"+pInfo.packageName+"|"+pInfo.label)
    cats = [GooglePalyConstants.CATEGORY_COMMUNICATION, GooglePalyConstants.CATEGORY_GAME, GooglePalyConstants.CATEGORY_SOCIAL]
    collections = [GooglePalyConstants.COLLECTION_TOPGROSSING, GooglePalyConstants.COLLECTION_TOPSELLING_FREE, GooglePalyConstants.COLLECTION_TOPSELLING_PAID]
    for cat in cats:
        for collection in collections:
            print(GooglePalyConstants.url(cat, collection))