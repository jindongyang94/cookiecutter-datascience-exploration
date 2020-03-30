"""
This file will contain all environmental variables and any common settings variables needed to be imported more conveniently across all 
model confguration files.

E.g. if you need all label columns for each model, it will easier to define it here BUT reference the each model config file instead of hardcoding it:
AD_LABEL = config.get('model1')['label_col']
FP_LABEL = config.get('model2')['label_col']

There should not be any hardcoded variables here if it is possible to hardcode it in the model_config.yaml files. 
"""