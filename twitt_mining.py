
# coding: utf-8

# # Mining (together with a bit of web scraping) of large social networks from Twitter using Python (and Ruby)
# ## By Moses Boudourides and Sergios Lenis 
# ## University of Patras, Greece

''' run it with python twitt_mining.py -s search_term
    more options with python twitt_mining.py -h
'''

import argparse
import pandas as pd
import json 
import os
import imp


# !pip install python-twitter
# import twitter
# input_dir='/home/mab/github_repos/TwitterMining'
# output_dir='/home/mab/Desktop/twitTemp'
cred_dic='/home/mosesboudourides/Dropbox/Python Projects/DublinNovemer2016/credentials/auth_cred.txt'

# cred_dic=None

# pp = get_ipython().getoutput(u'pwd')
# os.chdir(input_dir)
# print os.getcwd()


from test_class_tpa import create_df
import collect_tweets_notebook as ctn

# os.chdir(pp[0])

def create_beaker_com_dict(sps):
    nsps={}
    for k,v in sps.items():
        nsps[k]=[]
        if k=='date_split':
            for kk in sorted(v.keys()):
                nsps[k].append(v[kk].strftime('%Y%m%d'))
        else:
            for kk in sorted(v.keys()):
                nsps[k].append(v[kk])

    return nsps

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=(
        'Collect tweets matching a text pattern and store them'
    'continuously in JSON-formatted lines of a local file.'))
    parser.add_argument('-o', '--output',nargs='?', metavar='Output FILE', type=str,
        default='Out_json', help='output folder name')
    # parser.add_argument('-o', '--output',nargs=1, metavar='Output FILE', type=str,
    #     default='Out_json', help='output folder name')
    parser.add_argument('-s', '--search',nargs='?', metavar='Search term', type=str,
        required=True, help='Search term')

    parser.add_argument('-c', '--auth_dict',nargs='?', metavar='credentials dict', type=str,
        default=None, help='credentials dictionary file name') 
    parser.add_argument('-d', '--auth',nargs='?', metavar='credentials file', type=str,
        default=cred_dic, help='credentials file name') 
    argsr = parser.parse_args()
    # if args.search is None:
    #     print ''

    # print argsr
    fil=unicode(argsr.search,'utf-8')+'.json'
    # print aaa
    try:
        os.stat(argsr.output)
    except:
        os.mkdir(argsr.output)

    vv=ctn.UserAuth(auth_file=cred_dic)

    vv.login()

    vv.check_login()
    twi_api=vv.get_auth()

    # search_term='@MediaGovGr'
    sea=ctn.TwitterSearch(twi_api,search_text=argsr.search,working_path=argsr.output,out_file_dir=None,
    max_pages=10,results_per_page=100,sin_id=None,max_id=None,verbose=True)

    sea.streamsearch()


