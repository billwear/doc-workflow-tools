||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/api-authentication-snap-2-7-cli/2298) ~ [UI](/t/api-authentication-snap-2-7-ui/2299)|[CLI](/t/api-authentication-snap-2-8-cli/2300) ~ [UI](/t/api-authentication-snap-2-8-ui/2301)|[CLI](/t/api-authentication-snap-2-9-cli/2302) ~ [UI](/t/api-authentication-snap-2-9-ui/2303)|[CLI](/t/api-authentication-snap-3-0-cli/3825) ~ [UI](/t/api-authentication-snap-3-0-ui/3826)|
Packages|[CLI](/t/api-authentication-deb-2-7-cli/2304) ~ [UI](/t/api-authentication-deb-2-7-ui/2305)|[CLI](/t/api-authentication-deb-2-8-cli/2306) ~ [UI](/t/api-authentication-deb-2-8-ui/2307)|[CLI](/t/api-authentication-deb-2-9-cli/2308) ~ [UI](/t/api-authentication-deb-2-9-ui/2309)|[CLI](/t/api-authentication-deb-3-0-cli/3827) ~ [UI](/t/api-authentication-deb-3-0-ui/3828)|
MAAS's API uses [OAuth](http://en.wikipedia.org/wiki/OAuth) as its authentication mechanism. This isn't third-party (3-legged) OAuth, so the process used is what's commonly referred to as 0-legged OAuth: the consumer accesses protected resources by submitting OAuth signed requests.

Note that some API endpoints support unauthenticated requests (i.e. anonymous access). See the [API documentation](https://maas.io/docs/api) for details. 

#### Two questions you may have:

1. [How can I perform authenticated requests in python?](#heading--python)
2. [How can I perform authenticated requests in ruby?](#heading--ruby)

Here are two examples on how to perform an authenticated GET request to retrieve the list of nodes. The &lt;key&gt;, &lt;secret&gt;, &lt;consumer_key&gt; tokens are the three elements that compose the API key (API key = '&lt;consumer_key&gt;:&lt;key&gt;:&lt;secret&gt;').

<a href="#heading--python"><h2 id="heading--python">Python</h2></a>

``` python
import oauth.oauth as oauth
import httplib2
import uuid

def perform_API_request(site, uri, method, key, secret, consumer_key):
    resource_tok_string = "oauth_token_secret=%s&oauth_token=%s" % (
        secret, key)
    resource_token = oauth.OAuthToken.from_string(resource_tok_string)
    consumer_token = oauth.OAuthConsumer(consumer_key, "")

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(
        consumer_token, token=resource_token, http_url=site,
        parameters={'oauth_nonce': uuid.uuid4().hex})
    oauth_request.sign_request(
        oauth.OAuthSignatureMethod_PLAINTEXT(), consumer_token,
        resource_token)
    headers = oauth_request.to_header()
    url = "%s%s" % (site, uri)
    http = httplib2.Http()
    return http.request(url, method, body=None, headers=headers)

# API key = '<consumer_key>:<key>:<secret>'
response = perform_API_request(
    'http://server/MAAS/api/1.0', '/nodes/?op=list', 'GET', '<key>', '<secret>',
    '<consumer_key>')
```

<a href="#heading--ruby"><h2 id="heading--ruby">Ruby</h2></a>

``` ruby
require 'oauth'
require 'oauth/signature/plaintext'

def perform_API_request(site, uri, key, secret, consumer_key)
    consumer = OAuth::Consumer.new(
        consumer_key, "",
        { :site => "http://localhost/MAAS/api/1.0",
          :scheme => :header, :signature_method => "PLAINTEXT"})
    access_token = OAuth::AccessToken.new(consumer, key, secret)
    return access_token.request(:get, "/nodes/?op=list")
end

# API key = "<consumer_key>:<key>:<secret>"
response = perform_API_request(
     "http://server/MAAS/api/1.0", "/nodes/?op=list", "<key>", "<secret>",
     "consumer_key>")
```
