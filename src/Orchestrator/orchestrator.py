class Orchestrator:
    def __init__(self, database_client, cycle_detector, pre_processor, classifier, predictor):
        self.database_client = database_client
        self.cycle_detector = cycle_detector
        self.pre_processor = pre_processor
        self.classifier = classifier
        self.predictor = predictor

    def monitor(self):
        records_by_shovel = self.database_client._get_new_records()
        for shovel in records_by_shovel:
            records = records_by_shovel[shovel]
            self._process_cycle(shovel, records)            
        pass

    def _process_cycle(self, shovel, records):
        cycle = self.cycle_detector.detect_cycle(records)
        life_time = 0
        if cycle is not None:
            self.database_client.register_complete_cycle(shovel, records)
            features = self.pre_processor.pre_process(cycle)
            labels = self.classifier.assign_type(features)
            life_time = self.predictor(labels, features)
        return life_time
    
    