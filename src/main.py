import pandas as pd

from column_functions import (
    clean_col_spaces,
    delete_cols,
    convert_to_date,
    start_pipeline
)

if __name__=="__main__":
    #Applying functions
    df = pd.read_csv("dataset.csv") 
    columns_to_delete = ['Country', 'CountryCode', 'Borrower',
                        'Region', 'EndofPeriod', 'CreditNumber',
                        'ExchangeAdjustment',
                        'Sold3rdParty', 'Repaid3rdParty','Due3rdParty',
                        'UndisbursedAmount',"Borrower'sObligation",
                        'LastDisbursementDate',
                    'FirstRepaymentDate', 'LastDisbursementDate']
    date_columns = ['BoardApprovalDate', 'ClosedDate(MostRecent)',
                    'AgreementSigningDate', 'EffectiveDate(MostRecent)'
                    , 'LastRepaymentDate']


    clean_df = (df
                .pipe(start_pipeline)
                .pipe(clean_col_spaces)
                .pipe(delete_cols,columns_to_delete)
                .pipe(convert_to_date,date_columns))

    # Dumping the CSV file for data analysis.            
    clean_df.to_csv('processed.csv', index=False)
