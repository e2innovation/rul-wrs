class Orchestrator:
    def __init__(self, storage, cycle_detector, pre_processor, classifier, predictor):
        self.storage = storage
        self.cycle_detector = cycle_detector
        self.pre_processor = pre_processor
        self.classifier = classifier
        self.predictor = predictor

    def monitor(self):
        enabled_machines = self.storage.get_enabled_machines()
        return enabled_machines

    """
    def _process_cycle(self, shovel, records):
        cycle = self.cycle_detector.detect_cycle(records)
        life_time = 0
        if cycle is not None:
            self.database_client.register_complete_cycle(shovel, records)
            features = self.pre_processor.pre_process(cycle)
            labels = self.classifier.assign_type(features)
            life_time = self.predictor(labels, features)
        return life_time
    """    
    