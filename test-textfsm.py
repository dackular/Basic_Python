import argparse
import fnmatch
import textfsm
import pandas as pd
import io
import os
from sqlalchemy import create_engine

def read_textfile(base_dir=None, template_file=None):
    # Load the input file to a variable
    output = list()
    # entries = os.listdir(base_dir)
    entries = fnmatch.filter(os.listdir(base_dir), '*.log')
    for entry in entries:
        host = entry.split('.log')[0]
        input_file = open("%s/%s" % (base_dir, entry), mode='r', encoding='utf-8')
        raw_text_data = input_file.read()
        input_file.close()

        # Run the text through the FSM. 
        template = open(template_file)
        re_table = textfsm.TextFSM(template)
        fsm_results = re_table.ParseText(raw_text_data)

        for result in fsm_results:
            result.insert(0, host)
        
        output.extend(fsm_results)
    
    header = re_table.header
    header.insert(0, 'HOST')

    return header, output

def textfile_to_df(base_dir=None, template_file=None):
    header, results = read_textfile(base_dir=base_dir, template_file=template_file)
    df = pd.DataFrame(results, columns=header)

    return df

def textfile_to_csv(base_dir=None, template_file=None, dest_file=None):
    df = textfile_to_df(base_dir=base_dir, template_file=template_file)
    df.to_csv(dest_file, index=False, sep=',')



#ipsec_base_dir = './logs/ipsec_status/ios'
#ipsec_template_file = './scripts/cisco_ios_show_crypto_ipsec_sa.textfsm'
#ipsec_df = textfile_to_df(base_dir=ipsec_base_dir, template_file=ipsec_template_file)

ikev2_base_dir = open('./'
ikev2_template_file = './cisco_ios_show_crypto_ikev2_sa.textfsm'
ikev2_df = textfile_to_df(base_dir=ikev2_base_dir, template_file=ikev2_template_file)
        
#print(ipsec_df)
print(ikev2_df)