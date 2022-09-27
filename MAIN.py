
import gspread
import streamlit as st

credentials = {
  "type": "service_account",
  "project_id": "quick-district-311815",
  "private_key_id": "c95eb6af3c8ba18a8337dd4ff13d1ea23c21019e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDGAYaa0jsZ0khN\nYSz2lY+0kUU4zZPcxj9L/+WubzwdBBQWNoyy220aRPgw43pbTdvdHktLbSG9ThQK\n2FALY0zRy1bxx+nQ3XxtVH2KPEgeNJQ9GR81AIsTIGpW1eqOgM1iksh9N+VoNt34\nkZrjwa3vwhkFI2ixD+o2Zdxb6lWoxjXw5ff5vRco7lNNerM3bn/8bIY+pIqoEbUC\n5bWsd6miJdk+hHmKcJvrwNV3i0T+4fC4sSsc80qiSfBpNmuhNkFFeSmkHYn8zSvr\n31fzrur1mrvyhzTTLsjCKQq7UkrMh6/kU+aNokyiy4tSoUocHnWNJjtTg9yunG5k\nYVqWlSllAgMBAAECggEAAaz7B63Lui6ECUNXxYFDIAwdODlps02VAcC/wfbLXROi\nQmsQ5hiaCDTZJt3VcH1f095VVNymJIx+T4dzuF4EzaWXIRP28QoSjTQMnWeCu0TX\nx2NkePxCKITHvmhScydJ1a+PuawZIPQ42dHITkqrnzPsSJ4D7k2MJNlgs98aH3tZ\n12KSA0eeCqElQ+0HA7UYNMpTjPCqyt298zUAItk1wkPyiAhKRBnpx/DpcGIGVwCC\nh/PiGEIWuGOQY/nBXFmiMsouhxTmWYdccJ2AHA358yXwRBA7kXI08VC5arBu2n7v\nqAUnl7lnhmTVu7+yNr+VCIsbVJGXXniscd1LKnY3RwKBgQD/Q2/8R/rfpAw/fGsP\nKvlO4IBO6zJo+jiIM662msEtxj9ohzYzkvSVoKcMnnQcE2/DSBY0K/TNxMfTH8mE\nk7aBO/ctmGrMHDkGp2Pki/zlI0hVlEw1L2Cva+S1mUJr45xbjzuY8VT3B4aTjanF\nnhbijHgorxaai/4MU9RqubWRvwKBgQDGk8rZzsMJsdh6rqGxR5CaQsWEm4y314rq\nrNXouN7t1L41ZhNY8OynqaH8j6wJA1zqMQqExugobKG9vV10PkoIPv8+3dodPTHU\nwCHxEGtyfmI9kJKW29XbxOtriycs7pX+Ffp29hP8M7J0QuY17bcOA34NIVT+SW6e\nb3I6pEdF2wKBgCOgivHALiCmqdr2h46/Zbp/lQjuxMNoIRnJdNohsVKtN85kCMmb\n+i0kFgyp1PTSNagg2JCBjhJmI6mw5xRs9W0GLJKdklJYohDurf+JFkv457CiGRzX\nNvxk56/86wtZ4knZLO1EyaIM19iiTg656OHHz0GGZnY9kcCwtpYKw2/LAoGBAKR7\n1QHXRyynmKX+MsbSfY+ZkVxHMCczrci3QzRSta2Qk8FNfOcmIRC77QZzx09r7rG5\nz3mt/K1HVi4BRgC8e7wa2ngrcbjYcIdGYpb4P9gFocBXGWVGUP2KPmrFR7zrH2jo\nsZ+KM4GrHL06kM/IyOEduXKM0ocTMkKgE6FJZBQTAoGBAOPfwxB2yYu4swK1k7rw\nCGJzLgKVq7Rx9poEa0O5Uv23uqNIWrxnrn7rKwEnyQTxc5RD6vDXG2BoUeWnDxLk\nc1ut3ydw5o2gPwUxHdbRP6WKVM1S45AQAWfe/GngQeVYjrjpALbfkVCeEBkqoprl\nQOLEf7MRHKiT4yhmlxeNSNpr\n-----END PRIVATE KEY-----\n",
  "client_email": "main-52@quick-district-311815.iam.gserviceaccount.com",
  "client_id": "100921030068569251803",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/main-52%40quick-district-311815.iam.gserviceaccount.com"
}

gc = gspread.service_account_from_dict(credentials)

sh = gc.open("MAIN")

st.table(sh.sheet1.get('A1'))
