from typing import Dict, List

class Preprocess():
    def __init__(self, freqItemSet, rules):
        self.freqItemSet = freqItemSet
        self.rules = rules

    def preprocess_itemset(
        self, 
        sample_list: List = None
    ) -> Dict:

        result = [
            {
                'frequent_item_sets': list(item) 
            }
            
            for item in (self.freqItemSet if not sample_list else sample_list)
        ]

        return result
    
    def preprocess_rules(
        self,
        rules: List = None
    ):
        result = [
            {
                'antecedent': antecedent,
                'consequent': consequent,
                'confidence': confidence
            }

            for antecedent, consequent, confidence in (self.rules if not rules else rules)
        ]

        return result