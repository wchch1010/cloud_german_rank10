config_dict={}
config_dict['data_root_dir']='../data/'
config_dict['preprocess_dir']='../preprocess_dir/'
config_dict['pretrained']=None
config_dict['backbone']='se50'##can be 'se50','xcep','incepres'
config_dict['model_outdir'] ='../saved_models_se50_128size/'
config_dict['commit_outdir']='../submit/'
config_dict['batch_size']=256
config_dict['baselr']=4*1e-4
config_dict['weight_decay']=0.0
config_dict['epoches']=30
config_dict['early_stop_n']=5
config_dict['mixup_max_n']=4
config_dict['with_mixup']=False
config_dict['val_after_epoch']=0
config_dict['label_smooth_lambda']=0.1
config_dict['img_size']=128
