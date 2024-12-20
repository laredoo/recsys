import pandas as pd

from .preprocess import Preprocess
from schemas import ModelSchema

from fpgrowth_py import fpgrowth
from typing import Tuple, List

class Model:
    def __init__(self, schema: ModelSchema):
        self.sample = schema.sample

    def run_model(self, sample: List = None) -> Tuple[List, List]:

        model_sample = sample if sample else self.sample

        freq_itemset_sample, rules_sample = fpgrowth(model_sample, minSupRatio=0.05, minConf=0.15)

        return freq_itemset_sample, rules_sample
    
    def format_model_results(
        self, 
        freq_itemset_sample: List, 
        rules_sample: List
    ) -> Tuple[List, List]:

        pre_process_entity = Preprocess(freq_itemset_sample, rules_sample)

        freq_itemset = pre_process_entity.preprocess_itemset()
        rules = pre_process_entity.preprocess_rules()

        return freq_itemset, rules
    
    def generate_model_df(
        self, 
        freq_itemset: List,
        rules: List
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        
        rules_df = pd.DataFrame(rules)
        freq_itemset_df = pd.DataFrame(freq_itemset)

        return rules_df, freq_itemset_df
    
    def get_model_df(
        self,
        freq_itemset_sample: List, 
        rules_sample: List
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        
        freq_itemset, rules = self.format_model_results(freq_itemset_sample, rules_sample)

        rules_df, freq_itemset_df = self.generate_model_df(freq_itemset, rules)

        return rules_df, freq_itemset_df