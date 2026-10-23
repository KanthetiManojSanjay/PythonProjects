class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()


class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")


class BoeingEngine:
    def start(self):
        print("Starting Boeing Engine")


ab = AirbusEngine()
f2 = Flight(ab)
f2.startEngine()

be = BoeingEngine()
f2 = Flight(be)
f2.startEngine()
