class Android:
    def show_features(self):
        print("Android supports customization")
class iPhone:
    def show_features(self):
        print("iPhone supports iOS features")
class WindowsPhone:
    def show_features(self):
        print("Windows Phone supports Windows features")
android=Android()
iphone=iPhone()
windows=WindowsPhone()
android.show_features()
iphone.show_features()
windows.show_features()