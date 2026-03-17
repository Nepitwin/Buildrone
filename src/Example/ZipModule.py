from Buildrone.base import BaseModule


class ZipModule(BaseModule):
    def run(self, args):
        print("Zip module executed")
        print(args)