class Orchestrator:
    def __init__(self, storage, cycle_detector, pre_processor, classifier, predictor):
        self.storage = storage
        self.cycle_detector = cycle_detector
        self.pre_processor = pre_processor
        self.classifier = classifier
        self.predictor = predictor

    def monitor(self):
        machines = self.storage.get_equipo_pesado()
        for machine in machines:
            records = self.storage.get_input_records(machine)
            (is_cycle, status_machine) = self.cycle_detector.is_cycle(records)
            if status_machine == "no_working":
                self.storage.turn_off_equipo_pesado(machine)
            if is_cycle:
                new_cycle = self.storage.create_cycle(machine, records)
                features = self.pre_processor.get_features(records)
                self.storage.save_features(new_cycle, features)