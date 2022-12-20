def buildmetadata(da1, fdr):  
    HFda1 = da1.loc[da1['LABEL'] == 'HF']
    TIda1 = da1.loc[da1['LABEL'] == 'TI']
    AUda1 = da1.loc[da1['LABEL'] == 'AU']
    AFFda1 = da1.loc[da1['LABEL'] == 'AFF']
    EMda1 = da1.loc[da1['LABEL'] == 'EM']
    H1da1 = da1.loc[da1['LABEL'] == 'H1']
    H2da1 = da1.loc[da1['LABEL'] == 'H2']
    H3da1 = da1.loc[da1['LABEL'] == 'H3']
    ACKda1 = da1.loc[da1['LABEL'] == 'ACK']
    REda1 = da1.loc[da1['LABEL'] == 'RE']
    FIda1 = da1.loc[da1['LABEL'] == 'FI']
    TAda1 = da1.loc[da1['LABEL'] == 'TA']
    

    HFGda1 = (HFda1.sort_values(by=['filename', 'pageno','top'])).groupby(['filename','top'], as_index = False).agg({'Text': ' '.join})
    FIGda1 = (FIda1.sort_values(by=['filename', 'pageno','top'])).groupby(['filename','top'], as_index = False).agg({'Text': ' '.join})
    TAGda1 = (TAda1.sort_values(by=['filename', 'pageno','top'])).groupby(['filename','top'], as_index = False).agg({'Text': ' '.join})
    H1Gda1 = (H1da1.sort_values(by=['filename', 'pageno','top'])).groupby(['filename','top'], as_index = False).agg({'Text': ' '.join})
    H2Gda1 = (H2da1.sort_values(by=['filename', 'pageno','top'])).groupby(['filename','top'], as_index = False).agg({'Text': ' '.join})
    H3Gda1 = (H3da1.sort_values(by=['filename', 'pageno','top'])).groupby(['filename','top'], as_index = False).agg({'Text': ' '.join})
    
    
    export_csv = HFGda1.to_csv (r'datasets/'+fdr+'HL.csv', index = None, header=True)
    export_csv = TIda1.to_csv (r'datasets/'+fdr+'TI.csv', index = None, header=True)
    export_csv = AUda1.to_csv (r'datasets/'+fdr+'AU.csv', index = None, header=True)
    export_csv = AFFda1.to_csv (r'datasets/'+fdr+'AFF.csv', index = None, header=True)
    export_csv = EMda1.to_csv (r'datasets/'+fdr+'EM.csv', index = None, header=True)
    export_csv = H1Gda1.to_csv (r'datasets/'+fdr+'H1.csv', index = None, header=True)
    export_csv = H2Gda1.to_csv (r'datasets/'+fdr+'H2.csv', index = None, header=True)
    export_csv = H3Gda1.to_csv (r'datasets/'+fdr+'H3.csv', index = None, header=True)
    export_csv = ACKda1.to_csv (r'datasets/'+fdr+'ACK.csv', index = None, header=True)
    export_csv = REda1.to_csv (r'datasets/'+fdr+'RE.csv', index = None, header=True)
    export_csv = FIGda1.to_csv (r'datasets/'+fdr+'FI.csv', index = None, header=True)
    export_csv = TAGda1.to_csv (r'datasets/'+fdr+'TA.csv', index = None, header=True)
    
    export_csv = da1.to_csv (r'datasets/'+fdr+'op.csv', index = None, header=True)