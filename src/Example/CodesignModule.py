from Buildrone.base import BaseModule


class CodesignModule(BaseModule):
    def run(self, args):
        print("Codesign module executed")
        print(args)