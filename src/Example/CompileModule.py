from Buildrone.base import BaseModule


class CompileModule(BaseModule):
    def run(self, args):
        print("Compile module executed")
        print(args)