#!/usr/bin/env python3
import os
os.system('pip install pyshorteners')
import pyshorteners as ninja
os.system('pkg install figlet -y')
os.system('pkg install screenfetch -y')
os.system('clear')
os.system('screenfetch')
os.system('figlet -c -t SuperMask')
bpurple="\033[1;35m"
bgreen="\033[1;32m"
logo=f"""{bgreen}                 
                     Created by Anonycodexia{bgreen}"""
print(logo)
url=''


open_redirect=[ '--- URLS with Redirection Notice ---\n',


                'https://www.google.com/url?q=', 
                'https://google.com/url?q='     , 
                'https://facebook.com/l.php?u=', 

                '\n--- URLS with No Redirection Warnings ---\n',
                

                'https://via.hypothes.is/' ,      
                'http://vk.com/away.php?to=',     
                'https://googleweblight.com/i?u=' ,
                'https://l.wl.co/l?u=',              
                'https://tor2web.onionsearchengine.com/index.php?q=', 
                'https://onionengine.com/url.php?u=', 
                'http://raspe.id.au/bypass/miniProxy.php?', 
                'https://www.awin1.com/cread.php?awinmid=6798&awinaffid=673201&ued=', 
                'https://www.anrdoezrs.net/click-6361382-15020510?url=', 
                'https://www.digit.in/flipkart/intermediate?url=', 
                'https://adclick.g.doubleclick.net/pcs/click?xai=AKAOjstFA55hCSrFSTBDNko3225YAz6GkouTQlHjExWXRbT5OPMnSlE8Wh4LAVp-D7jWRr-LcKW0w-HH1g8lCVAK_eU-5azfUXfjqfTiHFOFWV9I8m2ZaGczGlov1iY8kMSnelCX-AHG6VYBmpcZJapT1XbdlOM3B9u9whYqpkxEpFLbkzwDao00-DL8JyS7UIxIApb_JHANRmtKLSuRcM8IWqFaP0cOc8n8jTedmwHc8oAw2MV2tRUaAnN3eaxaESpc8fovDeWslJ0A3duo5g46YzCYxQ8A56RI5MGcQw4TZj6TeWuj6jRjAe7g0X18--IBmztC1sUi6XuHkB1Ew-z_h9bv1XK-s_9L6zeDfQPtMsI3hOqp8T8545VdgCoElxs&sig=Cg0ArKJSzEpZ_YMvCKWCEAE&fbs_aeid=[gw_fbsaeid]&urlfix=1&adurl=', 
                'https://shop-links.co/link?publisher_slug=future&exclusive=1&u1=tomsguide-in-2620345246174741000&url=', 
                'https://meumundomaisdigital.com.br/wp-content/plugins/super-links/application/helpers/super-links-proxy.php?', 
                'http://media.mailadam.com/proxy/index.php?', 
                'http://f2pool.cam/index.php?', 
                'https://www.coinmarketguide.com/index.php?', 
                'https://loja.rarp.com.br/wp-content/plugins/super-links/application/helpers/super-links-proxy.php?', 
                'http://prox.x86.co.uk/index.php?', 
                'https://ersupport.com/plugins/QuickWebProxy/miniProxy.php?', 
                'http://ps-chi.herokuapp.com/index.php?', 
                'http://xlx723.dyndns.org/iproxy/miniProxy.php?', 
                'http://proxy.voracek.net/subdom/proxy/index.php/', 
                
                '\n--- ONION URLs ---\n',


                'http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/redir.php?url=',
                'http://zgphrnyp45suenks3jcscwvc5zllyk3vz4izzw67puwlzabw4wvwufid.onion/url.php?u=', 

                '\n--- Tor Onion URL Redirection [ only works for sites ending with .onion ] ---\n',


                'https://ahmia.fi/search/search/redirect?search_term=cat&redirect_url=', 
                'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/search/redirect?search_term=cat&redirect_url=' 
                ]


addr = input("Enter your Url: ")
sword = ninja.Shortener()
anony = (sword.tinyurl.short(addr))

print("Your TinyUrl Address=>  "  +anony)


def file_w():
  with open('supermasked.txt','w') as f:
     for i in open_redirect:
        if '---' in i:
           f.write(i)
        else:
           f.write('{}{}\n'.format(i,anony))
        
file_w()

x=input( '\n {}/supermasked.txt Generated!!!\n\nPress to continue...'.format(os.getcwd()))

f = open("supermasked.txt", "r")
print(f.read())