import twitter
api = twitter.Api(consumer_key='kNI4jfjC0oKhuRuVukGKhXQ2A',
                  consumer_secret='48jYr5tqQx1pvokXOV6lRAWapWdjhbXuCfjcEYpWX17bKq3EjT',
                  access_token_key='918302203911208961-Ub48HAsc8TskqIJOV2zyHEPibUrL96i',
                  access_token_secret='5MnNYQI7wHWNc92OiS4VBVwbVfT6ow5x5shk0YmaHpGB8')

search = api.GetSearch(term='pizza', lang='en', result_type='recent', count=100, max_id='', since = 2017-12-06)
for t in search:
 print t.user.screen_name + ' (' + t.created_at + ')'
 #Add the .encode to force encoding
 print t.text.encode('utf-8')
 print ''