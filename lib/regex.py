regex = {
    'Cloudinary'  : r"cloudinary://[0-9]+:[A-Za-z0-9\-_\.]+@[A-Za-z0-9\-_\.]+",
    'artifactory-api-password' : r"(?:\s|=|:|\"|^)AP[\dABCDEF][a-zA-Z0-9]{8,}",
    'jdbc-connection-string': r"jdbc:[a-z:]+://[A-Za-z0-9\.\-_:;=/@?,&]+",
    'artifactory-api-token' : r"(?:\s|=|:|\"|^)AKC[a-zA-Z0-9]{10,}",
    'azure-apim-secretkey' : r"Ocp-Apim-Subscription-Key",
    'bitly-secret-key' : r"R_[0-9a-f]{32}",
    'sonarqube-token': r"sonar.{0,50}(?:\"|'|`)?[0-9a-f]{40}(?:\"|'|`)?",
    'discord-webhook': r"https://discordapp\.com/api/webhooks/[0-9]+/[A-Za-z0-9\-]+",
    'Firebase URL': r".*firebaseio\.com",
    'google_api'     : r'AIza[0-9A-Za-z-_]{35}',
    'firebase'  : r'AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}',
    'google_captcha' : r'6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$',
    'google_oauth'   : r'ya29\.[0-9A-Za-z\-_]+',
    'google-calendar': r"https://www\.google\.com/calendar/embed\?src=[A-Za-z0-9%@&;=\-_\./]+",
    'facebook_access_token' : r'EAACEdEose0cBA[0-9A-Za-z]+',
    'authorization_basic' : r'basic [a-zA-Z0-9=:_\+\/-]{5,100}',
    'authorization_bearer' : r'bearer [a-zA-Z0-9_\-\.=:_\+\/]{5,100}',
    'mailgun_api_key' : r'key-[0-9a-zA-Z]{32}',
    'paypal_braintree_access_token' : r'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}',
    'square_oauth_secret' : r'sq0csp-[ 0-9A-Za-z\-_]{43}|sq0[a-z]{3}-[0-9A-Za-z\-_]{22,43}',
    'square_access_token' : r'sqOatp-[0-9A-Za-z\-_]{22}|EAAA[a-zA-Z0-9]{60}',
    'stripe_standard_api' : r'sk_live_[0-9a-zA-Z]{24}',
    'stripe_restricted_api' : r'rk_live_[0-9a-zA-Z]{24}',
    'github_access_token' : r'[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*',
    'rsa_private_key' : r'-----BEGIN RSA PRIVATE KEY-----',
    'ssh_dsa_private_key' : r'-----BEGIN DSA PRIVATE KEY-----',
    'ssh_dc_private_key' : r'-----BEGIN EC PRIVATE KEY-----',
    'pgp_private_block' : r'-----BEGIN PGP PRIVATE KEY BLOCK-----',
    'json_web_token' : r'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$',
    'slack_token' : r"\b(xox[apb]-[a-zA-Z0-9-]+)\b",
    'SSH_privKey' : r"([-]+BEGIN [^\s]+ PRIVATE KEY[-]+[\s]*[^-]*[-]+END [^\s]+ PRIVATE KEY[-]+)",
    'amazon-mws-auth-token' : r'amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
    'amazon-sns-topic' : r"arn:aws:sns:[a-z0-9\-]+:[0-9]+:[A-Za-z0-9\-_]+",
    'aws-access-key-value' : r"(A3T[A-Z0-9]|AKIA|AGPA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}",
    'aws-access-secret-key' : r"(accessKeyId|secretAccessKey)",
    'possible_creds' : r"(?i)(" \
                    r"password\s*[`=:\"]+\s*[^\s]+|" \
                    r"password is\s*[`=:\"]*\s*[^\s]+|" \
                    r"senha e\s*[`=:\"]*\s*[^\s]+|" \
                    r"senha é\s*[`=:\"]*\s*[^\s]+|" \
                    r"pwd\s*[`=:\"]*\s*[^\s]+|" \
                    r"passwd\s*[`=:\"]+\s*[^\s]+|" \
                    r"senha\s*[`=:\"]+\s*[^\s]+|" \
                    r"senha*[`=:\"]+\s*[^\s]+)",
    
}