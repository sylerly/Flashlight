import urllib, json

def results(parsed, original_query):
	search_specs = [
		 ["IMDB", "~imdbquery", "http://m.imdb.com/find?q=", "http://imdb.com/find?q="]
	]
	for name, key, mobile_url, url in search_specs:
		if key in parsed:
			mobile_search_url = mobile_url + urllib.quote_plus(parsed[key])
			search_url = url + urllib.quote_plus(parsed[key])
			return {
				"title": "Search {0} for '{1}'".format(name, parsed[key]),
				"run_args": [search_url],
				"html": """
				<script>
				setTimeout(function() {
					window.location = %s
				}, 500);
				</script>
				"""%(json.dumps(mobile_search_url)),
				"webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
				"webview_links_open_in_browser": True
			}

def run(url):
	import os
	os.system('open "{0}"'.format(url))
